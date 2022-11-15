import ctypes
import pathlib
def overwrite():
    if __name__ == "__main__":
    libname = pathlib.Path().absolute() / "mbroverwrite.cpp"
    c_lib = ctypes.CDLL(libname)