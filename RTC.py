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
    print(f' ====== Row Transposition Cipher ======')
    key = get_input('[*] Enter your key: ')
    key = removeD(checkDupChar(key))
    plaintext = get_input('[*] Enter your plaintext: ')
    keyTable = getPos(key)
    result = insertText(key, plaintext)
    answer = []
    for i in key:
        answer.append("")
    for row in result:
        for charPos in range(len(row)):
            answer[charPos] += row[charPos]
            print("\t " + row[charPos], end="\t")
        print()
    string = "".join(answer[keyTable.get(i)-1] for i in keyTable)
    print(f"[+] Answer: {string}")
