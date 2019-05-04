
def type_rele(acao, mode):
	if acao == "1":
		acao = acao.replace("1", "ligar")
	elif acao == "0":
		acao = acao.replace("0", "desligar")

	if acao =="ligar" and mode == False:
		print("concluido;{}".format("True"))
		return "concluido;{}".format("True")
	elif acao =="ligar" and mode == True:
		return "rendundancia;{}".format(mode)
	elif acao =="desligar" and mode == True:
		return "concluido;{}".format("False")
	elif acao =="desligar" and mode == False:
		return "rendundancia;{}".format(mode)
	else:
		return "mode;{}".format("-1")




