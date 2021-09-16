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
        print(f"    {i}-{keyTable.get(i)}", end=" ")
    print()
    return keyTable

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

def get_answer(key, result, keyTable):
    answer = []
    for i in key:
        answer.append("")
    for row in result:
        for charPos in range(len(row)):
            answer[charPos] += row[charPos]
            print("     " + row[charPos], end="  ")
        print()
    string = ""
    for i in keyTable:
        for j in range(len(key)):
            if key[j] == i:
                string += answer[j]
                break
    return string

def checkDupChar(string):
    newString = ""
    for i in string:
        if i not in newString:
            newString += i
    return newString

def get_input(string):
    user_input = input(string).upper()
    user_input = removeSC(user_input)
    return user_input

def checkEO(number):
    if number == int(number):
        return number
    return False

def removeSC(string):
    return re.sub(fr'[{special_char} ]', '', string)

def removeD(string):
    return re.sub('\d+', '', string)

if __name__ == '__main__':
    print(' ============ Row Transposition Cipher ============')
    key = removeD(checkDupChar(get_input('[*] Enter your key: ')))
    plaintext = get_input('[*] Enter your plaintext: ')
    keyTable = getPos(key)
    result = insertText(key, plaintext)
    string = get_answer(key,result, keyTable)
    print(f"[+] Answer: {string}")
