vogais = ['a', 'e', 'i', 'o', 'u']

def getVogais(string):
    newString = ""
    for x in string:
        if (x in vogais):
            newString += x
    return newString

if __name__ == '__main__':
    testString = "teste de audio em uma turma"
    print("String normal: " + testString)
    print("String apenas com vogais: " + getVogais(testString))