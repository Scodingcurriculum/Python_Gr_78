import cx_Freeze
import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("weather.py", base=base, icon="climate.png")]

setup(
    name="Live Weather App",
    options={"build_exe":{"packages":["tkinter","requests","PIL"],"include_files":["climate.png"]}},
    version="0.1",
    description="A simple live weather app for kids",
    executables=executables,
)
