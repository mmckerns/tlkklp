klepto: Unified Persistent Storage to Memory, Disk, or Database
=================================================================

`klepto` is a new python package that provides a unified programming interface to caching and archiving to memory, disk, or database. `klepto` provides a dictionary interface to caches and archives, where all caches can also be applied to any python callable as a decorator. `klepto` can be used to create dual caching strategies for speed and robustness, with design abstractions for things like multiple python processes using local memory caching asynchronously coupled to longer-term centralized storage on disk.

In this talk, I'll introduce klepto, a new python package that provides a unified abstraction layer on memory caching and archival storage. klepto provides a dictionary interface to the encoding and storage of objects into hierarchical containers (i.e. files on a file-system, tables within a database, or "folders" within an HDF5 file). klepto facilitates the asynchronous decoupling of computational workflows and provides built-in object provenance by providing direct object storage and retrieval.

First I'll demonstrate how klepto enables python objects to be serialized and stored in an archive, where one can simply store a given object in a database and then recover it later with the same state. klepto provides both standard and 'safe' caching, where safe caches are slower but can recover from most hashing errors. Then I'll discuss different programming abstractions for custom interpolation strategies in archive lookups, and caching strategies for automated exchange between cache and archive (i.e. alternates to the python standard `lru_cache`).

I'll show how klepto provides a decorator interface that facilitates the saving of function evaluations, where caches and archive can be queried and results retrieved as opposed to recalculating. klepto converts a function's input signature to a unique dictionary entry, and the function's results are the dictionary value. Thus for `y = f(x)`, `y` will be stored in `cache[x]` (e.g. `{x:y}`). I'll demonstrate using different encoding algorithms for dictionary keys and values, including raw objects, serialized objects, object hashes, and strings of object representations. klepto also provides useful decorators for simple, shallow, or deep rounding of objects in function arguments -- as well as cryptographic key generation, and the masking (i.e. ignoring) of selected arguments.

The audience should gain an understanding of how to use klepto to augment their data analytics. I will demonstrate the acceleration of scientific workflows through caching and archiving, including the use of klepto in a new fast n-dimensional search algorithm.



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
    dill >= 0.2.4,
    klepto >= 0.1.1,
    mystic >= 0.2a2.dev0

and optionally::

    sqlalchemy >= 0.8.4,
    pathos >= 0.2.0


Installation
--------------

All packages can be installed with `pip`::

    >$ pip install setuptools
    >$ pip install numpy
    >$ pip install git+https://github.com/uqfoundation/mystic.git@master
    >$ pip install matplotlib
    >$ pip install scipy


and optionally::

    >$ pip install sqlalchemy
    >$ pip install pathos


The `pip` installs of `numpy`, `matplotlib`, and `scipy` often fail.
A more stable choice for installing these three packages is to use a
scientific python distribution such as `canopy` or `anaconda`.

