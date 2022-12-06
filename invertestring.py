def reverseStringSolution1(string):
    return string[::-1]

def reverseStringSolution2(string):
    newString = ""
    for x in range(len(string)+1, 0, -1):
        newString += string[x]
    return newString

if __name__ == '__main__':
    testString = "batata"
    print("String normal: " + testString)
    print("String reversa: " + reverseStringSolution2(testString))