def responde(msg):
	from vo_re import trigger, audio_recognize
	from tts import fala
	fala(msg)
	trigger(audio_recognize())

