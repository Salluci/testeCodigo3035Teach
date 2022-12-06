diasDaSemana = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]

import datetime

def getDiaDaSemana(string):
    intArr = string.split("/")
    data = datetime.datetime(int(intArr[2]),int(intArr[0]),int(intArr[1]))
    return diasDaSemana[data.weekday()]

if __name__ == '__main__':
    stringData = "12/06/2022"
    print("Dia da semana para " + stringData + ": " + getDiaDaSemana(stringData))