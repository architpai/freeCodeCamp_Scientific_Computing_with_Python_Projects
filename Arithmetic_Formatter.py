def arithmetic_arranger(problems,answerval=False):
    topelements = []
    bottomelements = []
    operands = []
    answers = []
    topstr = ""
    bottomstr = ""
    linestr = ""
    ansstr = ""
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        for i in problems:
            elements = i.split()
            if elements[1] == "+" or elements[1] == "-":
                if elements[0].isdigit() and elements[2].isdigit():
                    if len(elements[0]) < 5 and len(elements[2]) < 5:
                        topelements.append(elements[0])
                        bottomelements.append(elements[2])
                        operands.append(elements[1])
                        answers.append(str(int(elements[0])+int(elements[2])))
                    else:
                        return "Error: Numbers cannot be more than four digits."
                else:
                    return "Error: Numbers must only contain digits."
            else:
                return "Error: Operator must be '+' or '-'."
    for i in range(0,len(problems)):
        golen = max([len(topelements[i]),len(bottomelements[i])])
        maxlen = golen + 2
        topstr = topstr + " "*(maxlen - len(topelements[i])) + str(topelements[i]) + " "*4
        bottomstr = bottomstr + " "*(maxlen - (len(bottomelements[i])+2))+str(elements[1]) + " " + str(bottomelements[i]) + " "*4
        linestr = linestr + "-"*maxlen + " "*4
        ansstr = ansstr + " "*(maxlen - len(answers[i])) + str(answers[i]) + " "*4
    if answerval :
        arranged_problems = topstr.rstrip()+'\n'+bottomstr.rstrip()+'\n'+linestr.rstrip()+'\n'+ansstr.rstrip()
    else:
        arranged_problems = topstr.rstrip() + '\n' + bottomstr.rstrip() + '\n' + linestr.rstrip() + '\n'
    return arranged_problems
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"],True))
