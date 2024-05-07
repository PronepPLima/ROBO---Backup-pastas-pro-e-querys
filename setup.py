#27/11/2023
#@PLima
#setup para criacao de exe do ROBO - MICROSOFT TEAMS

import sys
from cx_Freeze import setup, Executable

#Dependencies are automatically detected, but it might need fine tuning
build_exe_options = {"packages": ["os"], "includes": ["pyautogui", "datetime", "time", "os", "tkinter", "threading"], 'include_files': ["BACKUP.png"]   }


# GUI applications require a different base on Windows (the default is for  
#a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
setup(
    name = "ROBO - BACKUP DE PASTAS PIETRO",
    version = "1.0",
    description = "Robo para que seja realizado backup das pastas de Pietro para a Nuvem do Pietro.",
    options = {"build_exe": build_exe_options},
    executables=[Executable("ROBO - Backup pastas proj e querys.py", base=base, icon ="icone.ico")]
)