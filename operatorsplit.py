import re

def splitOperator(filename):
    f = open(filename, "r")
    input = f.read()
    f.close()

    # split the target string on the occurance of one or more whitespace characters
    output = re.split(r'\s+', input)
    print(output)

    operator = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\(', r'\)']
    
    # split the target string with the following pattern
    for oper in operator:
        temp = []    
        for statement in output:
            elmt = re.split(r'[A..z]*(' + oper + r')[A..z]*', statement)
            
            for splitted in elmt:
                temp.append(splitted) 
        output = temp
    print(output)

    # remove the blank characters from the output
    for statement in output:
        if statement == '':
            output.remove(statement)

    print(output)

splitOperator("tes.txt")