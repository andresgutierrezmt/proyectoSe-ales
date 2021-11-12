import speech_recognition as sr
import os

r = sr.Recognizer()

""" Clase que se encargara de recopilar los audios """
class Hablador():
    hablador=""

    def tomarAudios(self):
        with sr.Microphone() as source:
            print("->")
            audio = r.listen(source)
            try:
                self.hablador= r.recognize_google(audio, language='es-ES')
                return True
            except:
                print("Lo siento no pude procesar el audio, vuelve a intentarlo nuevamente")
                return False


""" Funciones importantes """

def verificarIgualdad(audio1, audio2):
    if(audio1 == audio2):
        return True
    else:
        return False

""" Hablador 1 """
print("Hablador 1 menciona algo")
hablador1 = Hablador()
comprobacion = hablador1.tomarAudios()
while(comprobacion == False):
    comprobacion = hablador1.tomarAudios()

os.system("cls") #Limpiar consola 

""" Hablador 2 """
print(f"Es tu turno hablador 2 menciona algo")
hablador2 = Hablador()
comprobacion = hablador2.tomarAudios()
while(comprobacion == False):
    comprobacion = hablador2.tomarAudios()

os.system("cls") #Limpiar consola 

""" Verificar si la palabra es igual """

verificador = verificarIgualdad(hablador1.hablador,hablador2.hablador)

""" Ver lo que dijeron """
print(f"El hablador 1 dijo: {hablador1.hablador}")
print(f"El hablador 2 dijo: {hablador2.hablador}")
if(verificador):
    print("Los audios son iguales")
else:
    print("los audios no son iguales")