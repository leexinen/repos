from MyQueue import MyQueue
from MyStack import MyStack

dictionary = []

def readFromDictionary(fileName):
    global dictionary

    f = open(fileName, "r")
    
    for line in f:
        line = line.replace("\n", "", )
        line = line.lower()
        dictionary.append(line)
    dictionary = list(set(dictionary))
    dictionary.sort()
    f.close()

def findWords(firstWord, lastWord):
    #---------------Enter your source code here----------------#
    #Print a shortest word ladder for the firstWord and lastWord and return 1 if such a ladder can be found
    #Return -1 if there exists no word ladder for the firstWord and lastWord

    global dictionary
    stackList = []
    stack = MyStack()
    stack.push(firstWord)
    queue = MyQueue()
    queue.enqueue(stack)
    wordFound = 1
    
    while(wordFound == 1 and queue.isEmpty() == False):
        s = queue.dequeue()
        word = s.peek()
        
        for dictWord in dictionary:
            findDiff = diffWord(word,dictWord)
            
            if (findDiff == None):
                continue
            
            else:
                if findDiff not in stackList:
                    stackList.append(findDiff)
                    #print word + "--->" + dictWord
                    createStack = MyStack()
                    createStack.copyFrom(s)
                    createStack.push(findDiff)
                    #createStack.toString()
                    queue.enqueue(createStack)
                    #print queue.size()
                    
        if (word != lastWord):
            wordFound = 1;
            
        else:
            return s.toString()
            
    return -1


def diffWord(wordToCompare,dictWord):
    global dictionary
    dictList = []
    
    if (len(dictWord) == len(wordToCompare)):
        count = 0
        
        for i in range(0,len(dictWord)):
            
            if i == len(dictWord):
                count = 0
                #print dictWord[i]
                
            elif wordToCompare[i] != dictWord[i]:
                count += 1
                
        if count == 1:
            return dictWord
            
    
                
                
                
def test(firstWord, lastWord):
    result = findWords(firstWord, lastWord)
    if result == -1: print("No Ladder for ", firstWord, "->", lastWord)

readFromDictionary('dictionary.txt')
test('stone','money')
test('babies','sleepy')
test('devil','angel')
test('monk','perl')
test('blue','pink')
test('heart','heart')
test('slow', 'fast')
test('atlas','zebra')
test('babes','child')
test('train','bikes')
test('brewing','whiskey')
test('men','can')
#More challenging test cases
test('money','smart')
test('mumbo','ghost')
#No solution test cases
test('snow', 'stop')





