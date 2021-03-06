
name = "PySide"

@early()
def version():
    return this.__version + "-native"

description = \
    """
    Python binding of the cross-platform GUI toolkit Qt.
    """

@early()
def requires():
    from rez.package_py_utils import find_site_python
    py_package = find_site_python("PySide")
    return [py_package.qualified_name]

build_command = False

uuid = "recipes.pyside"

def commands():
    # Qt.py support
    env.QT_PREFERRED_BINDING = "PySide"

_native = True


# --- internals

def _version():
    from rez.package_py_utils import exec_python

    return exec_python(
        "_version",
        ["import PySide",
         "print PySide.__version__"])


__version = _version()
