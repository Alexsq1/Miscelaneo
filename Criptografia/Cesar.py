#Toma mensaje como string, devuelve encriptado como string

def encriptar(mensaje, clave):

    mensaje = mensaje.upper()

    cript = ""

    for letra in mensaje:

        letra_nueva = ord(letra) - 65
        letra_nueva = (letra_nueva + clave) % 26
        letra_nueva = letra_nueva + 65

        cript = cript + chr(letra_nueva)

    return cript


def desencriptar(mensaje, clave):

    clave_nueva = 26 - clave % 26
    return encriptar(mensaje, clave_nueva)

def criptoanalisis(mensaje):

    ji_por_clave = {}
    mensaje = mensaje.upper()

    cuenta_relativa_esp, cuenta_relativa_texto = cuentas_relativas()

    for clave in range (0,27):

        cuenta_relativa_texto = cuenta_relativa_texto.fromkeys(cuenta_relativa_texto, 0)


        mensaje_intento = desencriptar(mensaje, clave)

        for letra in mensaje_intento:
            cuenta_relativa_texto[letra] = cuenta_relativa_texto[letra] + (1 / len(mensaje))


        acc = 0
        for letra in cuenta_relativa_esp:
            acc = acc + (cuenta_relativa_esp[letra] - cuenta_relativa_texto[letra]) ** 2 / cuenta_relativa_esp[letra]

        ji_por_clave[clave] = acc


    return min(ji_por_clave, key = ji_por_clave.get)


def cuentas_relativas():


    cuenta_relativa_esp = {}

    cuenta_relativa_esp["A"] = 0.1253
    cuenta_relativa_esp["B"] = 0.0142
    cuenta_relativa_esp["C"] = 0.0468
    cuenta_relativa_esp["D"] = 0.0586
    cuenta_relativa_esp["E"] = 0.1368
    cuenta_relativa_esp["F"] = 0.0069
    cuenta_relativa_esp["G"] = 0.0101
    cuenta_relativa_esp["H"] = 0.0070
    cuenta_relativa_esp["I"] = 0.0625
    cuenta_relativa_esp["J"] = 0.0044
    cuenta_relativa_esp["K"] = 0.0002
    cuenta_relativa_esp["L"] = 0.0497
    cuenta_relativa_esp["M"] = 0.0315
    cuenta_relativa_esp["N"] = 0.0671
    cuenta_relativa_esp["?"] = 0.0031
    cuenta_relativa_esp["O"] = 0.0868
    cuenta_relativa_esp["P"] = 0.0251
    cuenta_relativa_esp["Q"] = 0.0088
    cuenta_relativa_esp["R"] = 0.0687
    cuenta_relativa_esp["S"] = 0.0798
    cuenta_relativa_esp["T"] = 0.0463
    cuenta_relativa_esp["U"] = 0.0393
    cuenta_relativa_esp["V"] = 0.0090
    cuenta_relativa_esp["W"] = 0.0001
    cuenta_relativa_esp["X"] = 0.0022
    cuenta_relativa_esp["Y"] = 0.0090
    cuenta_relativa_esp["Z"] = 0.0052

    cuenta_relativa_texto = {}
    cuenta_relativa_texto["A"] = 0
    cuenta_relativa_texto["B"] = 0
    cuenta_relativa_texto["C"] = 0
    cuenta_relativa_texto["D"] = 0
    cuenta_relativa_texto["E"] = 0
    cuenta_relativa_texto["F"] = 0
    cuenta_relativa_texto["G"] = 0
    cuenta_relativa_texto["H"] = 0
    cuenta_relativa_texto["I"] = 0
    cuenta_relativa_texto["J"] = 0
    cuenta_relativa_texto["K"] = 0
    cuenta_relativa_texto["L"] = 0
    cuenta_relativa_texto["M"] = 0
    cuenta_relativa_texto["N"] = 0
    cuenta_relativa_texto["?"] = 0
    cuenta_relativa_texto["O"] = 0
    cuenta_relativa_texto["P"] = 0
    cuenta_relativa_texto["Q"] = 0
    cuenta_relativa_texto["R"] = 0
    cuenta_relativa_texto["S"] = 0
    cuenta_relativa_texto["T"] = 0
    cuenta_relativa_texto["U"] = 0
    cuenta_relativa_texto["V"] = 0
    cuenta_relativa_texto["W"] = 0
    cuenta_relativa_texto["X"] = 0
    cuenta_relativa_texto["Y"] = 0
    cuenta_relativa_texto["Z"] = 0

    return (cuenta_relativa_esp, cuenta_relativa_texto)






