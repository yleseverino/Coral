from gtts import gTTS
from subprocess import call


def cria_audio(mensagem):
    tts = gTTS(mensagem, lang='pt-br')
    tts.save('audios/{}.mp3'.format(mensagem))
    print('CORAL: ', mensagem)
    call(['afplay', 'audios/mensagem.mp3'])


def fala(arquivo):
    call(['afplay', "audios/{}.mp3".format(arquivo)])




