cd ..
pyinstaller --noconfirm --onefile --console --icon "favicon.ico" --name "Athene"  "athene/__main__.py"

mv "dist/Athene" "bin"
rm -rf "dist"

rm -rf "build"
rm "Athene.spec"
