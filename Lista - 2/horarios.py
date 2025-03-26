horario1 = input() 
listaHorario1 = horario1.split(":") 
segundo1 = int(listaHorario1[2])
minuto1 = int(listaHorario1[1]) 
hora1 = int(listaHorario1[0])
minuto1 = minuto1 * 60 
hora1 = hora1 * 3600 
segundo1 = hora1 + minuto1 + segundo1 

horario2 = input() 
listaHorario2 = horario2.split(":")
segundo2 = int(listaHorario2[2])
minuto2 = int(listaHorario2[1])
hora2 = int(listaHorario2[0]) 
minuto2 = minuto2 * 60 
hora2 = hora2 * 3600 
segundo2 = hora2 + minuto2 + segundo2 

segundosTotais = segundo2 - segundo1 
print(segundosTotais)