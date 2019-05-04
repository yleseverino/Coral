
import speech_recognition as sr

with open("credenciais/GCloudKey.json.json") as crendenciais_google:   ####Congigurações
	crendenciais_google = crendenciais_google.read()

def audio_recognize():  # Ler audio do microfone
	rec = sr.Recognizer()
	with sr.Microphone() as source:
		audio = rec.listen(source)
		print("Aguardando comando:")
		try:
			voz = rec.recognize_google_cloud(audio, credentials_json=crendenciais_google, language="pt-BR")
			voz = voz.lower()
			return voz
		except sr.UnknownValueError:
			print("Google não entendeu o áudio")
			return "-1"
		except sr.RequestError as e:
			print("não foi possível requisitar de Google Cloud Speech service; {0}".format(e))
			return "-2"


def audio_monitor():
	hotword = "coral"
	while True:
		voz = audio_recognize()
		if hotword in voz:
			from tts import fala
			fala("Um momento!")
			return trigger(voz)
			break


def trigger(voz):
	if not voz == "-1" or "-2":
		import Triggers
		return Triggers.executa_comandos(voz)
	else:
		import erro
		return erro.trata_erro("voz", voz)








