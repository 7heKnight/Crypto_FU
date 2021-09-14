# Row Transposition Cipher
import string
import re

alphabet = string.ascii_uppercase
special_char = string.punctuation

def getPos(key):
    key = key.replace(' ', '').upper()
    keyTable = {}
    pos = 1
    record = ""
    for alp in alphabet:
        if alp not in record:
            for charPos in key:
                if charPos == alp:
                    record += charPos
                    tmp = {charPos: pos}
                    keyTable.update(tmp)
                    pos += 1
                    break
    for i in key:
        print(f"\t{i}-{keyTable.get(i)}", end="\t")
    print()
    return keyTable

def checkEO(number):
    if number == int(number):
        return number
    return False

def insertText(key, plaintext):
    tmpText = ""
    result = []
    count = 0
    for i in plaintext:
        if count == len(key):
            result.append(tmpText.upper())
            tmpText = ""
            count = 0
        tmpText += i
        count += 1
    missingText = len(key)-len(tmpText)
    tmpText += alphabet[len(alphabet)-missingText::]
    result.append(tmpText.upper())
    return result

def removeSC(string):
    return re.sub(fr'[{special_char} ]', '', string)

def checkDupChar(string):
    newString = ""
    for i in string:
        if i not in newString:
            newString += i
    return newString

if __name__ == '__main__':
    print(f' ====== Row Transposition Cipher ======')
    # key = input('[*] Enter your key: ').upper()
    key = "tests"
    key = removeSC(checkDupChar(key))
    # plaintext = input('[*] Enter your plaintext: ').upper()
    plaintext = "This is Plaintext for the tests"
    plaintext = removeSC(plaintext)
    keyTable = getPos(key)
    cal = len(plaintext) / len(key)
    rows = checkEO(cal)
    if rows == False:
        rows = int(cal) + 1
    result = insertText(key, plaintext)
    for i in result:
        for j in i:
            print("\t " + j, end="\t")
        print()
