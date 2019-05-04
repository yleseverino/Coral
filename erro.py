def trata_erro(modulo,tipo, mode):
	if modulo == "rele":
		if str(tipo) == "redundancia":
			if mode == "False":
				mode = mode.replace("False", "desligado")
			elif mode == "True":
				mode = mode.replace("True", "ligado")
			from tts import cria_audio
			msg = "o dispositivo já se encontra {}!".format(mode)
			cria_audio(msg)
			return msg
		elif str(tipo) == "-1":
			from Speech import responde
			msg = "Nesse dispositivo só existe o modo ligar e desligar, diga novamente o comando."
			responde(msg)
			return msg
		else:
			return "-41"
	else:
		return "-42"
