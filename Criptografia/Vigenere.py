
import Cesar


def desplazar(mensaje, clave, signo):

    mensaje = mensaje.upper()
    clave = clave.upper()

    cript = ""


    cursor = 0
    for letra in mensaje:

        letra_cifrar = clave[cursor % len(clave)]

        letra_nueva = ord(letra) - 65
        desp_nueva = ord(letra_cifrar) - 65

        letra_nueva = letra_nueva + desp_nueva * signo

        letra_nueva = letra_nueva % 26
        letra_nueva += 65
        cript += chr(letra_nueva)

        cursor += 1

    return cript

def encriptar(mensaje, clave):

    return desplazar(mensaje, clave, 1)

def desencriptar(mensaje, clave):
    return desplazar(mensaje, clave, -1)


def criptoanalisis(mensaje):

#Calcula periodo más probable y busca clave

    mensaje = mensaje.upper()

    periodos_mas_probables = prob_periodo(mensaje)
    print("Periodos más probables: ", periodos_mas_probables[0], periodos_mas_probables[1])

    claves = []
    cursor = 0

    for cl in periodos_mas_probables:
        claves.append(crPeriodo(mensaje, cl))

    return claves

def crPeriodo(mensaje, periodo):

    l_mens = dividir(mensaje, periodo)

    clave = ""
    for palabra in l_mens:
        clave += chr(Cesar.criptoanalisis(palabra) + 65)

    return clave

def mejor_por_periodo(mensaje):

    max = 10
    for i in range(1, max):
        print(crPeriodo(mensaje, i))

def dividir(mensaje, frecuencia):

    cursor = 0
    l_mens = []

    for i in range(0, frecuencia):
        l_mens.append("")

    for i in mensaje:

        l_mens[cursor] += i

        cursor += 1
        cursor %= frecuencia

    return l_mens

def prob_periodo(mensaje):

    probs_por_periodo = {}

    max_clave = 10

    for i in range(2, max_clave):
        l_mens = dividir(mensaje, i)

        acc = 0
        for m in l_mens:
            if len(m) > 3:
                acc += ic_periodo(m, i)

        probs_por_periodo[i] = acc

#    newValue = value
 #   answer = min(dict.items(), key=lambda (_, value): abs(value - newValue))

    ic_espanol = 0.0744

    clave_mas_cercana = min(probs_por_periodo.keys(), key=lambda x: abs(probs_por_periodo[x] - ic_espanol))

    return (clave_mas_cercana, max(probs_por_periodo, key = probs_por_periodo.get))





def ic_periodo(mensaje, periodo):

    frecs_letras = {}

    for letra in mensaje:
        if frecs_letras.get(letra) != None:
            frecs_letras[letra] += 1
        else:
            frecs_letras[letra] = 0

    acc = 0
    for frec in frecs_letras.values():
        acc += frec * (frec - 1)

    acc /= (periodo * (periodo - 1))
    return acc




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
    return cuenta_relativa_esp

