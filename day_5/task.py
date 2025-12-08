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
     
def solution2() -> int:
     with open("./day_5/input.txt") as file:
        ranges = list()
        next_line = ""
        while next_line != "\n":
            next_line = file.readline()
            if next_line.strip():
                st, en = next_line.strip().split("-")
                ranges.append((int(st), int(en)))
        
        ranges.sort()
        fresh = 0
        current = -1
        for (start, end) in ranges:
                if current >= start:
                    start = current + 1
                if start <= end:
                    fresh += end - start + 1
                current = max(current, end)
                    
        
        return fresh

print(solution2())