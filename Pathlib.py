from pathlib import Path, PureWindowsPath
carpeta = Path("E:\\UDEMY\\PYTHON\\mi_archivo.txt")
address_ach = Path("E:/UDEMY/PYTHON/archive_10.txt")
ruta_win = PureWindowsPath(address_ach)

print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print("Este archivo existe")
else:
    print("Existe")

print(ruta_win) #E:\UDEMY\PYTHON\archive_10.txt