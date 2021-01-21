def arithmetic_arranger(problems, answ=False):
    number=len(problems)

    if(number>5):
        return "Error: Too many problems."

    line_1 = list()
    line_2 = list()
    signs = list()
    lengths = list()
    answers = list()

    for i in range(number):
        if "+" in problems[i]:
            a=problems[i].split(" + ")

            if not (a[0].isdigit()):
                return "Error: Numbers must only contain digits."
            elif not (a[1].isdigit()):
                return "Error: Numbers must only contain digits."

            if (len(a[0])>4) or (len(a[1])>4):
                return "Error: Numbers cannot be more than four digits."

            line_1.append(a[0])
            line_2.append(a[1])
            signs.append("+")

            if (len(a[0])>len(a[1])):
                lengths.append(len(a[0])+2)
            else:
                lengths.append(len(a[1])+2)

            answers.append(int(a[0])+int(a[1]))
        elif "-" in problems[i]:
            a=problems[i].split(" - ")

            if not (a[0].isdigit()):
                return "Error: Numbers must only contain digits."
            elif not (a[1].isdigit()):
                return "Error: Numbers must only contain digits."

            if (len(a[0])>4) or (len(a[1])>4):
                return "Error: Numbers cannot be more than four digits."

            line_1.append(a[0])
            line_2.append(a[1])
            signs.append("-")

            if (len(a[0])>len(a[1])):
                lengths.append(len(a[0])+2)
            else:
                lengths.append(len(a[1])+2)

            answers.append(int(a[0])-int(a[1]))
        elif ("/" in problems[i]) or ("x" in problems[i]) or ("*" in problems[i]):
            return "Error: Operator must be '+' or '-'."

    arranged_problems=""

    for x in range(number):
        if(x<(number-1)):
            arranged_problems+=(lengths[x] - len(line_1[x]))*" " + line_1[x] + 4*" "
        else:
            arranged_problems+=(lengths[x] - len(line_1[x]))*" " + line_1[x]

    arranged_problems+="\n"

    for x in range(number):
        if(x<(number-1)):
            arranged_problems+=signs[x] + (lengths[x] - ((len(line_2[x]))+1))*" " + line_2[x] + 4*" "
        else:
            arranged_problems+=signs[x] + (lengths[x] - ((len(line_2[x]))+1))*" " + line_2[x]

    arranged_problems+="\n"

    for x in range(number):
        if(x<(number-1)):
            arranged_problems+=lengths[x]*"-" + 4*" "
        else:
            arranged_problems+=lengths[x]*"-"

    if(answ):
        arranged_problems+="\n"
        for x in range(number):
            if(x<(number-1)):
                arranged_problems+= (lengths[x] - len(str(answers[x])))*" " + str(answers[x]) + 4*" "
            else:
                arranged_problems+= (lengths[x] - len(str(answers[x])))*" " + str(answers[x])

    return arranged_problems