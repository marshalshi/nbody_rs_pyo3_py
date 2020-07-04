Performance Comparison: Rust vs PyO3 vs Python
----------------------------------------------

I am using `n-body <https://benchmarksgame-team.pages.debian.net/benchmarksgame/description/nbody.html#nbody>`_ to compare the performance among Rust, PyO3 and Python.

This repo includes three parts of code:

- `rnbody` is Rust version, source code from `benchmarksgame Rust <https://benchmarksgame-team.pages.debian.net/benchmarksgame/program/nbody-rust-1.html>`_ .
- `rnbody_pyo3` is python using pyo3 version, the main function `advance` is using rust code to calculate.
- `pnbody.py` is python version, source code from `benchmarksgame Python <https://benchmarksgame-team.pages.debian.net/benchmarksgame/program/nbody-python3-1.html>`_ with slightly update on `BODIES` data type.

How to Use
^^^^^^^^^^

- `rnbody`: Make sure installed rust and cargo. And then run `cargo run 10000` (`10000` is steps which used in calculating nbody) in `rbody` folder.
- `rnbody_pyo3`:
  - Install rust nightly. Currently `master` branch of PyO3 is able to use stable rust version. But I am using `0.10.1` of `pyo3 <https://github.com/PyO3/PyO3>`_ .
  - Install `setuptools-rust <https://github.com/PyO3/setuptools-rust>`_ .
  - In folder `rnbody_pyo3` do `python setup.py develop`.
  - Run `./pnbody_pyo3 10000` (using `Planet` struct to representing planet data) or `./pnbody_pyo3 10000 --list` (using `vec` to representing planet data)
- `pnbody.py`: Run `./pnbody.py 10000`.

Performance
^^^^^^^^^^^

TODO: add soon
