import re

def total_caracteres( texto):
    return len(texto)

def total_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def total_oraciones(texto):
    oraciones = re.split(r'[.!?]+', texto)
    oraciones = [o.strip() for o in oraciones if o.strip()]
    return len(oraciones)

def palabra_mas_larga(texto):
    palabras = texto.split()
    if not palabras:
        return ""
    return max(palabras, key=len)

def palabra_mas_corta(texto):
    palabras = [p for p in texto.split() if p]
    if not palabras:
        return ""
    return min(palabras, key=len)

def numero_vocales(texto):
    vocales = "aeiouAEIOU"
    return sum(1 for c in texto if c in vocales)

def numero_consonantes(texto):
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for c in texto if c in consonantes)

def main():
    texto = input("Ingrese un texto para analizar: ").strip()
    if not texto:
        print("El texto no puede estar vacío.")
        return

    print("\nEstadísticas del texto:")
    print(f"Total de caracteres: {total_caracteres(texto)}")
    print(f"Total de palabras: {total_palabras(texto)}")
    print(f"Total de oraciones: {total_oraciones(texto)}")
    print(f"Palabra más larga: '{palabra_mas_larga(texto)}'")
    print(f"Palabra más corta: '{palabra_mas_corta(texto)}'")
    print(f"Número de vocales: {numero_vocales(texto)}")
    print(f"Número de consonantes: {numero_consonantes(texto)}")

if __name__ == "__main__":
    main()
