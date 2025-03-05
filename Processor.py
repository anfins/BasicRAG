import sys


def getContent(fileName):
    '''
    Input : fileName (string)
    Output : content (string)
    This function takes a file name as input and returns the content of the file.
    '''
    with open(fileName, "r") as file:
        content = file.read()
    return content

def getTokens(content):
    '''
    Input : content (string)
    Output : tokens (list of strings
    This function takes a string as input and returns a list of tokens.
    '''
    tokens = content.split()
    return tokens
        

def parseContent(content):
    '''
    Input : content (string)
    Output : None
    This function takes a string as input and prints the sentences
    '''
    sentences = content.split(".")
    print(sentences)


if __name__ == "__main__":
    parseContent(getContent(sys.argv[1]))
 

    
