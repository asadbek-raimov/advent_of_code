import re


def solution() -> None:
    with open("./day_6/input.txt") as file:
        content = file.read()
        lines = content.splitlines()
        operands = list()
        operations = list()
        for i in range(len(lines)):
            
            if i == len(lines) - 1:
                operations.extend(s.strip() for s in lines[i].strip().split("  ") if s.strip())                
            else:
                operands.append(tuple(s for s in lines[i].strip().split(" ") if s.strip()))
        total = 0
        for i in range(len(operations)):
            current = int(operands[0][i])
            for j in range(1, len(operands)):
                match operations[i]:
                    case "*":
                        current *= int(operands[j][i])
                    case "+":
                        current += int(operands[j][i])
                    case "-":
                        current -= int(operands[j][i])
                    case "/":
                        current /= int(operands[j][i])
            total += current
        print(total)

def solution2() -> None:
    with open("./day_6/input.txt") as file:
        content = file.read()
        lines = content.splitlines()
        operands = list()
        operations = list()
        for i in range(len(lines)):
            
            if i == len(lines) - 1:
                operations.extend(s.strip() for s in lines[i].strip().split("  ") if s.strip())                
            else:
                operands.append(lines[i])
        total = 0
        
        numbers = list()
        current = list()
        for j in range(len(operands[0])-1,-1, -1):
            empty = 0
            num = ""
            for line in operands:
                if line[j] == " ":
                    empty += 1
                else:
                    num += line[j]

                if empty >= len(operands):
                    if len(current):
                        numbers.append(current)
                    current = list()
            if num:
                current.append(int(num))

        if len(current):
                numbers.append(current)
        print(numbers)
        operations.reverse()
        for i in range(len(operations)):
            current = int(numbers[i][0])
            for j in range(1, len(numbers[i])):
                match operations[i]:
                    case "*":
                        current *= numbers[i][j]
                    case "+":
                        current += numbers[i][j]
            total += current
        print('TOTAL:', total)


solution2()