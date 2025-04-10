DOMINGO = 1 
SEGUNDA = 2 
QUARTA = 4 
SEXTA = 6 
SABADO = 7 
FERIADO = "domingo" 
FALTA = "falta" 
JEANS = "jeans" 
MACAQUINHO = "macaquinho" 
SHORTS = "shorts"
VESTIDO = "vestido" 
VETOREA = "vetorea" 

def decide(dia , temp): 
    if dia == DOMINGO: 
        return FERIADO 
    elif temp > 30: 
        return FALTA 
    elif temp < 20:
        return JEANS
    elif dia == QUARTA or dia == SEXTA or dia == SABADO: 
        if dia == QUARTA and temp > 22: 
            return MACAQUINHO 
        else: 
            return VESTIDO 
    elif dia == SEGUNDA and temp > 22:
        return MACAQUINHO 
    elif temp >= 25: 
        return SHORTS 
    else: return VETOREA

    caso = eval(input()) 
    while caso != (): 
        dia , temp = caso 
        print(decide(dia , temp))
        caso = eval(input()) 
