from pathlib import Path
import shutil

def parentpath(path='.', f=0):
    return Path(path).resolve().parents[f]

def cp(file, file2):
    if not file.startswith('/'):
        file = str(Path(__file__).resolve().parent / file)
    if Path(file2).is_dir():
        print('installing', file, file2)
        shutil.copy(file, file2)

# 
cp('js/matter.js', '/usr/local/share/jupyter/nbextensions/google.colab/')