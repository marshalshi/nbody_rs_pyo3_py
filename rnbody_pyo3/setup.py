#!/usr/bin/env python

from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="rnbody_pyo3",
    version="1.0",
    rust_extensions=[RustExtension("rnbody_pyo3.rnbody_pyo3", binding=Binding.PyO3)],
    packages=["rnbody_pyo3"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)
