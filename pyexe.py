import PyInstaller.__main__
import shutil

PyInstaller.__main__.run([
    'app/main.py',
    '--icon=app/images/taligent.ico',
    #for MacOS
    #'--icon=app/images/taligent.icns',
    #'--windowed'
    '--onefile',
    '--noconsole',
], )

shutil.copytree('app/', 'dist/app')