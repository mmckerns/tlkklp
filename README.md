klepto: Unified Persistent Storage to Memory, Database, or Disk
=================================================================

`klepto` is a new python package that provides a unified programming interface to caching and archiving to memory, disk, or database. `klepto` provides a dictionary interface to caches and archives, where all caches can also be applied to any python callable as a decorator. `klepto` can be used to create dual caching strategies for speed and robustness, with design abstractions for things like multiple python processes using local memory caching asynchronously coupled to longer-term centralized storage on disk.



Content
---------

All talk content can be obtained from this repository either with
`git, or by downloading the repository content as a zip file.  If you use
git, you can clone this repostory with::

    $ git clone https://github.com/mmckerns/tlkklp.git


or, download and unzip the zipfile.



Requirements
--------------

To be able to run the examples, demos, and exercises in this talk,
the following packages must be installed::

    numpy >= 1.0,
    scipy >= 0.6.0,
    matplotlib >= 0.91,
    dill >= 0.2.4.dev0,
    klepto >= 0.1.1,
    mystic >= 0.2a2.dev0

and optionally::

    sqlalchemy >= 0.8.4,
    pathos >= 0.2a1.dev0


Installation
--------------

All packages can be installed with `pip`::

    >$ pip install setuptools
    >$ pip install numpy
    >$ pip install git+https://github.com/uqfoundation/dill.git@master
    >$ pip install git+https://github.com/uqfoundation/mystic.git@master
    >$ pip install matplotlib
    >$ pip install scipy


and optionally::

    >$ pip install sqlalchemy
    >$ pip install git+https://github.com/uqfoundation/pox.git@master
    >$ pip install git+https://github.com/uqfoundation/pathos.git@master


The `pip` installs of `numpy`, `matplotlib`, and `scipy` often fail.
A more stable choice for installing these three packages is to use a
scientific python distribution such as `canopy` or `anaconda`.

