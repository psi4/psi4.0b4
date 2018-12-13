/*
 * @BEGIN LICENSE
 *
 * Psi4: an open-source quantum chemistry software package
 *
 * Copyright (c) 2007-2018 The Psi4 Developers.
 *
 * The copyrights for code used from other parties are included in
 * the corresponding files.
 *
 * This file is part of Psi4.
 *
 * Psi4 is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, version 3.
 *
 * Psi4 is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License along
 * with Psi4; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * @END LICENSE
 */

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/pytypes.h>
#include <pybind11/stl.h>

#include <string>
#include <vector>

#include "psi4/libmints/dimension.h"
#include "psi4/libmints/linalg.h"
#include "psi4/libmints/vector.h"
#include "psi4/libpsi4util/exception.h"

using namespace psi;
namespace py = pybind11;
using namespace pybind11::literals;

auto docstring = [](const std::string& s1, const std::string& s2) { return (s1 + " " + s2).c_str(); };

namespace {
template <size_t Rank>
struct bind_special_ctors final {
    template <typename PyClass, size_t Rank_ = Rank, typename = std::enable_if_t<detail::is_rank1_v<Rank_>>>
    void operator()(PyClass& c) {
        c.def(py::init<int>());
        c.def(py::init<const std::string&, int>());
    }

    template <typename PyClass, size_t Rank_ = Rank, typename = std::enable_if_t<detail::is_rank2_v<Rank_>>>
    void operator()(PyClass& c, int /* dummy */ = 0) {
        c.def(py::init<int, int>());
        c.def(py::init<const std::string&, int, int>());
    }
};

template <typename T, size_t Rank>
void declareTensor(py::module& mod, const std::string& suffix) {
    using Class = Tensor<T, Rank>;
    using PyClass = py::class_<Class, std::shared_ptr<Class>>;
    auto binder = bind_special_ctors<Rank>();

    std::string name = "Tensor_" + suffix;

    PyClass cls(mod, name.c_str());

    cls.def(py::init<const std::string&, size_t, const std::array<Dimension, Rank>&>());
    binder(cls);
    cls.def_property_readonly("dim", &Class::dim, ("Total dimension of " + name).c_str());
    cls.def_property_readonly("nirrep", &Class::nirrep, ("Number of irreps in " + name).c_str());
    cls.def_property("name", &Class::name, &Class::set_name, ("The name of " + name).c_str());
    // cls.def_property_readonly("dimpi", py::overload_cast<>(&Class::dimpi),
    //                          ("Returns the Dimension object of " + name).c_str());
    cls.def("axes_dimpi", &Class::axes_dimpi, ("Returns the Dimension object of " + name + " for given axis").c_str(),
            "axis"_a);
}
}  // namespace

void export_linalg(py::module& mod) {
    // Rank-1 tensor aka blocked vector
    declareTensor<double, 1>(mod, "D_1");
    // Rank-2 tensore aka blocked matrix
    declareTensor<double, 2>(mod, "D_2");

    using Class = Vector;
    using PyClass = py::class_<Vector, std::shared_ptr<Vector>>;

    PyClass cls(mod, "Vector", "Class for creating and manipulating vectors", py::dynamic_attr());
    cls.def(py::init<int>())
        .def(py::init<const Dimension&>())
        .def(py::init<const std::string&, int>())
        .def(py::init<const std::string&, const Dimension&>())
        .def_property("name", py::cpp_function(&Vector::name), py::cpp_function(&Vector::set_name),
                      "The name of the Vector. Used in printing.")
        .def("get", py::overload_cast<int>(&Vector::get, py::const_), "Returns a single element value located at m",
             "m"_a)

        .def("get", py::overload_cast<int, int>(&Vector::get, py::const_),
             "Returns a single element value located at m in irrep h", "h"_a, "m"_a)
        .def("set", py::overload_cast<int, double>(&Vector::set), "Sets a single element value located at m", "m"_a,
             "val"_a)
        .def("set", py::overload_cast<int, int, double>(&Vector::set),
             "Sets a single element value located at m in irrep h", "h"_a, "m"_a, "val"_a)
        .def("print_out", &Vector::print_out, "Prints the vector to the output file")
        .def("scale", &Vector::scale, "Scales the elements of a vector by sc", "sc"_a)
        .def("dim", &Vector::dim, "Returns the dimensions of the vector per irrep h", "h"_a = 0)
        .def("nirrep", &Vector::nirrep, "Returns the number of irreps")
        .def("get_block", &Vector::get_block, "Get a vector block", "slice"_a)
        .def("set_block", &Vector::set_block, "Set a vector block", "slice"_a, "block"_a)
        .def("dimpi", &Vector::dimpi, "Returns the Dimension object")
        .def("array_interface",
             [](Vector& v) {

                 // Build a list of NumPy views, used for the .np and .nph accessors.Vy
                 py::list ret;

                 // If we set a NumPy shape
                 if (v.numpy_shape().size()) {
                     if (v.nirrep() > 1) {
                         throw PSIEXCEPTION(
                             "Vector::array_interface numpy shape with more than one irrep is not "
                             "valid.");
                     }

                     // Cast the NumPy shape vector
                     std::vector<size_t> shape;
                     for (int val : v.numpy_shape()) {
                         shape.push_back((size_t)val);
                     }

                     // Build the array
                     py::array arr(shape, v.pointer(0), py::cast(&v));
                     ret.append(arr);

                 } else {
                     for (size_t h = 0; h < v.nirrep(); h++) {
                         // Hmm, sometimes we need to handle empty ptr's correctly
                         double* ptr = nullptr;
                         if (v.dim(h) != 0) {
                             ptr = v.pointer(h);
                         }

                         // Build the array
                         std::vector<size_t> shape{(size_t)v.dim(h)};
                         py::array arr(shape, ptr, py::cast(&v));
                         ret.append(arr);
                     }
                 }

                 return ret;
             },
             py::return_value_policy::reference_internal);
}
