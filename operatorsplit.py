import re
import variable_fa as fa

def splitOperator(filename):
    f = open(filename, "r")
    inputfile = f.read()
    f.close()

    # split the target string on the occurance of one or more whitespace characters
    output = re.split(r'\s+', inputfile)
    #print(output)

    operator = ['!=', '==', '>=', '<=', '<', '>', ':', ',', '/', '-', r'\+', r'\*', r'\*\*', r'\'', r'\"', r'\'\'\'', r'\(', r'\)', 'none', 'not', 'true', 'false', r'\{', r'\}', r'\[', r'\]', 'for', '#', 'elif', 'else', 'while', 'break', 'continue', 'pass', 'def', 'return', 'range', 'raise', 'class', 'from', 'import', 'with', 'open', 'print']
    
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

    # split the variables
    temp = []
    for statement in output:
        if statement in operator:
            temp.append(statement)
        else:
            if statement == 'as' or statement == 'is' or statement == 'or' or statement == 'in' or statement == 'if' or statement == 'and':
                temp.append(statement)
            else:
                split = list(statement)
                temp.extend(split)
                # print(statement)
                # if(fa.isVariable(statement)):
                #     split = list(statement)
                #     temp.extend(split)
                # elif(fa.isNumber(statement)):
                #     split = list(statement)
                #     temp.extend(split)
                # else :
                #     print("Variable Name Error")
            
    return temp