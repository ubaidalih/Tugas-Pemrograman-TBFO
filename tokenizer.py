import re

def tokenizeInput(inputFilename):
    f = open(inputFilename, "r")
    input = f.read()
    f.close()

    input = input.split()
    output = input

    operators = [':', ',', '=', '<', '>', '>=', '<=', '==', '!=', r'\+', '-', r'\*', '/', r'\*\*', r'\(', r'\)',r'\'\'\'', r'\'', r'\"']

    for operator in operators:
        temp = []
        for statement in output:
            formatting = r"[A..z]*(" + operator + r")[A..z]*"
            elmt = re.split(formatting, statement)
            
            for splitStatement in elmt:
                temp.append(splitStatement) 
        output = temp

    temp = []
    for statement in output:
        checkStrip = statement.split()
        for splitStatement in checkStrip: 
            temp.append(splitStatement)

    output = temp
    output = [string for string in output]

    print(output)

tokenizeInput("tes.txt")