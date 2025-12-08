def solution()-> int:
    with open("./day_5/input.txt") as file:
        ranges = list()
        available = list()
        fresh = 0
        next_line = ""
        while next_line != "\n":
            next_line = file.readline()
            if next_line.strip():
                ranges.append(next_line.strip().split("-"))
        
        while next_line:
            next_line = file.readline().strip()
            if next_line:
                available.append(next_line)
        print(ranges)
        for product in available:
            for interval in ranges:
                if int(interval[0]) <= int(product) and  int(product) <= int(interval[1]):
                    fresh += 1
                    break
        return fresh
     
       
print(solution())