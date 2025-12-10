def solution()-> None: 
    with open("./day_7/input.txt") as file:
        lines = file.read().splitlines()
        s_found = False
        splits = 0
        
        beam_indexes = set()
        for j in range(len(lines)):
            for i in range(len(lines[j])):
                if not s_found:
                    if lines[j][i] == "S":
                        s_found = True
                        beam_indexes.add(i)
                else:
                    if i in beam_indexes:
                        if lines[j][i] == "^":
                            splits += 1
                            beam_indexes.remove(i)
                            beam_indexes.add(i+1)
                            beam_indexes.add(i-1)
                        else:
                            newLine = lines[j][:i] + "|" + lines[j][i+1:]
                            lines[j] = newLine
                            
        print("\n".join(lines))  
        print(splits)  
        
def solution2()-> None: 
    with open("./day_7/input.txt") as file:
        lines = file.read().splitlines()
        summary = [0] * len(lines[-1])
        s_found = False
        for j in range(len(lines)):
            for i in range(len(lines[j])):
                if not s_found:
                    if lines[j][i] == "S":
                        s_found = True
                        summary[i] = 1
                else:
                    if summary[i] != 0 and lines[j][i] == "^":
                        if summary[i-1] != 0:
                            summary[i-1] = summary[i-1] + summary[i]
                        else:
                            summary[i-1] = summary[i]

                        if summary[i+1] != 0:
                            summary[i+1] = summary[i] + summary[i+1]
                        else: 
                            summary[i+1] = summary[i]
                        
                        summary[i] = 0
                            
        print(sum(summary))      
        
solution2()