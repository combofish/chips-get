from cx_Freeze import setup, Executable

build_exe_options = {
    "include_files": ["config.ini"]
    }

setup(
    name="CoordinateConversion",
    version="1.0",
    description="CoordinateConversion",
    author="combofish",
    options={"build_exe":build_exe_options},
    executables=[Executable(script="CoordinateConversion.py",base="win32gui",icon="well.ico")])