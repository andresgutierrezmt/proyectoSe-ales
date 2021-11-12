import speech_recognition as sr
import time
import os

r = sr.Recognizer()

""" Configuraciones del programador """

class Procesamiento():
    Audio1 =""
    Audio2 = ""

    lectura1 =""
    lectura2 =""

    def __init__(self, Audio1, Audio2):
        os.system("cls")
        self.Audio1 = Audio1
        self.Audio2 = Audio2
        self.ordenar()
        self.procesar()
        self.imprimir()
    
    def ordenar(self):
        self.Audio1 = f"audios/{self.Audio1}.wav" 
        self.Audio2 = f"audios/{self.Audio2}.wav" 

    def procesar(self):
        print("proccesando Audios....!")
        self.lectura1 = self.obtenerTexto(self.Audio1, 1)
        self.lectura2 = self.obtenerTexto(self.Audio2, 2)
        print("Completado! ... :)")
        time.sleep(1)
    
    def obtenerTexto(self, Audio, numero):
        try:
            with sr.AudioFile(Audio) as source:
                lectura = r.listen(source)
                time.sleep(1.5)
                try:
                    return r.recognize_google(lectura, language='es-ES')
                except:
                    return f"Lo siento no pude procesar lo que dice el audio {numero} :("
        except (FileNotFoundError):
                print(f"no encontre el Audio {numero}")
                return "ERROR - el audio no existe verifique el nombre del archivo"
    
    def validar(self):
        if(self.lectura1 == self.lectura2):
            return f"Por lo tanto los audios son iguales"
        else:
            return f"Por lo tanto los audios no son iguales"

    def imprimir(self):
        os.system("cls")
        print(f"El audio 1 dice: {self.lectura1}")
        print(f"El audio 2 dice: {self.lectura2}")
        print(self.validar())

""" Configuraciones del usuario """

nombreAudio1 = "audio1ejemplo"
nombreAudio2 = "audio1ejemplo2"

procesador = Procesamiento(nombreAudio1,nombreAudio2)