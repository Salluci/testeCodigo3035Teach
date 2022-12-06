def returnSecondHighest(array):
    maisAlto = testArray[0]
    segundoMaisAlto = testArray[0]
    for x in array:
        if x > maisAlto:
            maisAlto = x
    for x in array:
        if x < maisAlto and x > segundoMaisAlto:
            segundoMaisAlto = x
    return segundoMaisAlto

if __name__ == '__main__':
    testArray = [1, 2, 3, 4, 5, 6, 6]
    print("Segundo mais alto: " + str(returnSecondHighest(testArray)))