from django.shortcuts import render

# Create your views here.
def encipher(word):
    word = word.lower()
    wordList = word.split(' ')
    for i in range(len(wordList)):
        for j in range(len(wordList[i])):
            if wordList[i][j] == 'a':
                wordList[i][j] = 'e'
            elif wordList[i][j] == 'o':
                wordList[i][j] = 'u'
            elif wordList[i][j] == 'p':
                wordList[i][j] = 'b'
            elif wordList[i][j] == 't':
                wordList[i][j] = 'd'
            elif wordList[i][j] == 's':
                wordList[i][j] = 'j'
            elif wordList[i][j] == 'o':
                wordList[i][j] = 'g'
            elif wordList[i][j] == 'm':
                wordList[i][j] = 'n'
            elif wordList[i][j] == wordList[i][j+1]:
                wordList.remove(wordList[i][j])
                wordList[i][j+1].upper()
    for item in wordList:
        result = item + ' '
    return result


    def decipher(word):
        word = word.lower()
        wordList = word.split(' ')
        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                if wordList[i][j] == 'e':
                    wordList[i][j] = 'a'
                elif wordList[i][j] == 'u':
                    wordList[i][j] = 'o'
                elif wordList[i][j] == 'b':
                    wordList[i][j] = 'p'
                elif wordList[i][j] == 'd':
                    wordList[i][j] = 't'
                elif wordList[i][j] == 'j':
                    wordList[i][j] = 's'
                elif wordList[i][j] == 'g':
                    wordList[i][j] = 'o'
                elif wordList[i][j] == 'n':
                    wordList[i][j] = 'm'
                elif wordList[i][j] == wordList[i][j+1]:
                    wordList.remove(wordList[i][j])
                    wordList[i][j+1].upper()
        for item in wordList:
            result = item + ' '
        return result
