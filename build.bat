@echo off
pyinstaller --noconfirm --onefile --console --icon "favicon.ico" --name "Athene"  "athene\__main__.py"

move "dist\Athene.exe" "bin"
rmdir dist

rmdir /S /Q "build"
del "Athene.spec"