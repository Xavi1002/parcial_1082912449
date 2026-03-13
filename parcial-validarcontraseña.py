def longitud_minima(contraseña):
    return len(contraseña) >= 8

def longitud_maxima(contraseña):
    return len(contraseña) <= 20

def tiene_mayuscula(contraseña):
    return any(c.isupper() for c in contraseña)

def tiene_minuscula(contraseña):
    return any(c.islower() for c in contraseña)

def tiene_numero(contraseña):
    return any(c.isdigit() for c in contraseña)

def tiene_especial(contraseña):
    especiales = "!@#$%^&*"
    return any(c in especiales for c in contraseña)

def validar_contraseña(contraseña):
    criterios = [
        longitud_minima(contraseña),
        longitud_maxima(contraseña),
        tiene_mayuscula(contraseña),
        tiene_minuscula(contraseña),
        tiene_numero(contraseña),
        tiene_especial(contraseña)
    ]
    return all(criterios)

def obtener_errores(contraseña):
    errores = []
    if not longitud_minima(contraseña):
        errores.append("Debe tener al menos 8 caracteres")
    if not longitud_maxima(contraseña):
        errores.append("Debe tener máximo 20 caracteres")
    if not tiene_mayuscula(contraseña):
        errores.append("Debe tener al menos una mayúscula")
    if not tiene_minuscula(contraseña):
        errores.append("Debe tener al menos una minúscula")
    if not tiene_numero(contraseña):
        errores.append("Debe tener al menos un número")
    if not tiene_especial(contraseña):
        errores.append("Debe tener al menos un carácter especial: !@#$%^&*")
    return errores

def main():
    while True:
        contraseña = input("Ingrese una contraseña: ")
        if validar_contraseña(contraseña):
            print("Contraseña válida.")
            break
        else:
            errores = obtener_errores(contraseña)
            print("Contraseña inválida. Le falta:")
            for error in errores:
                print(f"- {error}")

if __name__ == "__main__":
    main()
   