from Pathlib import Path
base = Path.home()

guia = Path(base,"España", Path("Barcelona", "Sagrada_FAMILIA.txt"))
guia2 = guia.with_name("Texto2.txt")
print(base)
print(guia)
print(guia2.parent)


