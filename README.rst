Performance Comparison: Rust vs PyO3 vs Python
----------------------------------------------

I am using `n-body <https://benchmarksgame-team.pages.debian.net/benchmarksgame/description/nbody.html#nbody>`_ to compare the performance among Rust, PyO3 and Python.

This repo includes three parts of code:

- :code:`rnbody` is Rust version, source code from `benchmarksgame Rust <https://benchmarksgame-team.pages.debian.net/benchmarksgame/program/nbody-rust-1.html>`_ .
- :code:`rnbody_pyo3` is python using pyo3 version, the main function :code:`advance` is using rust code to calculate.
- :code:`pnbody.py` is python version, source code from `benchmarksgame Python <https://benchmarksgame-team.pages.debian.net/benchmarksgame/program/nbody-python3-1.html>`_ with slightly update on :code:`BODIES` data type.

How to Use
^^^^^^^^^^

- :code:`rnbody`: Make sure installed :code:`rust` and :code:`cargo`. And then run :bash:`cargo run 10000` (:code:`10000` is steps which used in calculating nbody) in :code:`rbody` folder.
- :code:`rnbody_pyo3`:
  - Install rust nightly. Currently :code:`master` branch of PyO3 is able to use stable rust version. But I am using :code:`0.10.1` of `pyo3 <https://github.com/PyO3/PyO3>`_ .
  - Install `setuptools-rust <https://github.com/PyO3/setuptools-rust>`_ .
  - In folder :code:`rnbody_pyo3` run :bash:`python setup.py develop`.
  - Run :bash:`./pnbody_pyo3 10000` (using :code:`Planet` struct to representing planet data) or :bash:`./pnbody_pyo3 10000 --list` (using :code:`vec` to representing planet data)
- :code:`pnbody.py`: Run :bash:`./pnbody.py 10000`.

Performance
^^^^^^^^^^^

TODO: add soon
