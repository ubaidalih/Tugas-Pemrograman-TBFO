import re

def splitOperator(filename):
    f = open(filename, "r")
    input = f.read()
    f.close()

    # split the target string on the occurance of one or more whitespace characters
    output = re.split(r'\s+', input)
    #print(output)

    operator = ['=', '!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\(', r'\)', 'none', 'and', 'not', 'true', 'false', r'\{', r'\}', r'\[', r'\]', 'for', '#', 'elif', 'else', 'while', 'break', 'continue', 'pass', 'def', 'return', 'range', 'raise', 'class', 'from', 'import', 'with', 'open', 'print']
    
    # split the target string with the following pattern
    for oper in operator:
        temp = []    
        for statement in output:
            elmt = re.split(r'[A..z]*(' + oper + r')[A..z]*', statement)
            
            for splitted in elmt:
                temp.append(splitted) 
        output = temp
    #print(output)

    # remove the blank characters from the output
    for statement in output:
        if statement == '':
            output.remove(statement)

    temp = []
    for statement in output:
        if statement in operator:
            temp.append(statement)
        else:
            if statement == 'as' or statement == 'is' or statement == 'or' or statement == 'in' or statement == 'if':
                temp.append(statement)
            else:
                split = list(statement)
                temp.extend(split)
            
    return temp

tes = splitOperator("tes.txt")
print(tes)