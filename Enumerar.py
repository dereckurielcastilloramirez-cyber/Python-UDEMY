from pathlib import Path

guia = Path(Path.home(), "Europa")
for txt in Path(guia).glob("**/*.txt"):
    print(txt)

guia2 = Path("Europa", "España", "Barcelona", "SagradaFamilia.txt")
en_europa = guia2.relative_to(Path("Europa"))
en_espania = guia2.relative_to(Path("Europa","España"))

print(en_espania)
print(en_europa)