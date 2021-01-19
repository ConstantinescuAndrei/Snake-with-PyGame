import cx_Freeze

executables = [cx_Freeze.Executable("app.py")]

cx_Freeze.setup(
    name="Simple Snake",
    options={"build.exe": {"packages":["pygame"],
                            "include files": [""]}},

    executables = executables
)