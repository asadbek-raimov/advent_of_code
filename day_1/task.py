class Solution:
    
    
    def __init__(self, current) -> None:
        self.current = current
    
    def part_1(self):
        file = open("./day_1/input.txt")
        zeros = 0
        
        next_word = file.readline()
        while next_word:
            direction, steps = next_word[0], int(next_word[1:])
            if direction == "R":
                self.current = self.current + steps
            if direction == "L":
                self.current = self.current - steps
            
            self.current %= 100

            if self.current == 0:
                zeros += 1
            next_word = file.readline()
        
        return zeros
    
    def part_2(self):
        file = open("./day_1/input.txt")
        zeros = 0
        
        next_word = file.readline()
        while next_word:
            direction, steps = next_word[0], int(next_word[1:])
            zeros += (steps // 100)
            left = steps % 100

            if direction == "R":
                self.current = self.current + left
                if (self.current) > 99:
                    self.current -= 100
                    zeros += 1
                
            if direction == "L":
                self.current = self.current - left
                if (self.current) < 0:
                    self.current += 100
                    zeros += 1

            next_word = file.readline()
        
        return zeros
        
        
        
        
print(Solution(50).part_2())