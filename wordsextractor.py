#Counts amount of words in text no matter how many spaces are between them
#Everything that is not a space(or space-same character) counts as a word
def countAmountOfWordsInText(text : str) -> int:
    amount : int = 0;
    isInWord : bool = False;
    for i in text:
        if i == " ":
            if isInWord:
                isInWord = False;
        else:
            if not isInWord:
                isInWord = True;
                amount+=1;
    return amount;

#Imagine full text as a list(or array) of words. It allows you to get specific word from the text via list-like indexing logic
def getWordFromTextAtPosition(text : str, position : int) -> str:
    word : str = "";
    if position < 0:
        position += countAmountOfWordsInText(text);
    amount : int = 0;
    isInWord : bool = False;
    foundPosition : bool = False;
    for i in text:
        if not foundPosition:
            if i == " ":
                if isInWord:
                    isInWord = False;
            else:
                if not isInWord:
                    isInWord = True;
                    amount+=1;
                    if amount - 1 == position:
                        foundPosition = True;
                        word += i;
        else:
            if i != " ":
                word += i;
            else:
                break;
    return word;

#Opposite logic of mixing getting a signle word and counting all words in text - it counts spaces after stated index of the word
#It is used to get exact amount of spaces between words in text
def countAmountOfSpacesAfterWordAtPosition(text : str, position : int) -> int:
    amount : int = 0;
    if position < 0:
        position += countAmountOfWordsInText(text);
    isInWord : bool = False;
    wordCount : int = 0;
    foundStart : bool = False;
    for i in text:
        if not foundStart:
            if i == " ":
                if isInWord:
                    isInWord = False;
                    if wordCount - 1 == position:
                        foundStart = True;
                        amount += 1;
            else:
                if not isInWord:
                    isInWord = True;
                    wordCount+=1;
        else:
            if i == " ":
                amount += 1;
            else:
                break;
    return amount;