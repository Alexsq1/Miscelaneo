import Cesar

mensaje = "UTILIZANDOPALABRASMASLARGASDELESPANOL"

clave = 4
encriptado = Cesar.encriptar(mensaje, clave)

print("PROBANDO CÓDIGO CÉSAR")
print("Texto encriptado: ", encriptado)
print("Texto desencriptado", Cesar.desencriptar(encriptado, clave))

clave_prob = Cesar.criptoanalisis(encriptado)

print("La clave más probable es ", clave_prob)
print("El mensaje más probable es", Cesar.desencriptar(encriptado, clave_prob))

import Vigenere

clave = "CATANA"
mensaje = "NOSENCONTRAMOSREALIZANDOELCRIPTOANALISISDELCIFRADOELCUALESCOMPLETAMENTESECRETOYCIFRADO"

print("PROBANDO CÓDIGO VIGÈNERE")
encriptado = Vigenere.encriptar(mensaje, clave)
desencriptado = Vigenere.desencriptar(encriptado, clave)
print("Mensaje encriptado:   ", encriptado)
print("Mensaje desecriptado: ", desencriptado)

claves = Vigenere.criptoanalisis(encriptado)

print("Claves más probables: ", claves[0], claves[1])
print("Mensajes más probable: ", Vigenere.desencriptar(encriptado, clave[0]), Vigenere.desencriptar(encriptado, clave[1]))

#clave_mas_probable = Vigenere.crPeriodo(encriptado, 8)
#print("Clave más probable con periodo dado: ", clave_mas_probable)

Vigenere.mejor_por_periodo(encriptado)
