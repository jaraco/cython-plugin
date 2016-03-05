cython-plugin
=============

A setuptools plugin to allow installation and invocation of Cython at build time.

To use this plugin, simply add the following to your setup.py::

    setup(
        use_cython=True,
        install_requires=['cython-plugin'],
    )

If you use this plugin, it will cause setuptools to use Cython's build_ext
command instead of the default command, but does not require Cython to be
present at the time setup.py is invoked.
