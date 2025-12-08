class Solution:
    def solve(self):
        counter = 0
        with open("./day_4/input.txt") as file:
            grid = list()
            next_line = file.readline().strip()
            while next_line:
                row = list(next_line)
                grid.append(row)
                
                next_line = file.readline().strip()
            
            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    roll_neighbors = 0
                     # check for first row and first and last column of it
                    # check for last row and first and last column of it
                    # just check for first and last column
                    if grid[r][c] != "@":
                        continue

                    # check top
                    if r != 0:
                        if self.check_if_roll(grid[r-1][c]):
                            roll_neighbors += 1
                    # bottom
                    if r != len(grid) - 1:
                         if self.check_if_roll(grid[r+1][c]):
                            roll_neighbors += 1

                    # check right
                    if c != len(grid[r]) - 1:
                        if self.check_if_roll(grid[r][c+1]):
                            roll_neighbors += 1
                     # check left
                    if c != 0:
                        if self.check_if_roll(grid[r][c-1]):
                            roll_neighbors += 1
                   
                    # left up corner
                    if c != 0 and r != 0:
                        if self.check_if_roll(grid[r-1][c-1]):
                            roll_neighbors += 1
                    # right up corner
                    if c != len(grid[r]) - 1 and r != 0:
                        if self.check_if_roll(grid[r-1][c+1]):
                            roll_neighbors += 1

                    # right bottom corner
                    if c != len(grid[r]) - 1 and r != len(grid) - 1:
                        if self.check_if_roll(grid[r+1][c+1]):
                            roll_neighbors += 1
        
                    # left bottom corner
                    if c != 0 and r != len(grid) - 1:
                        if self.check_if_roll(grid[r+1][c-1]):
                            roll_neighbors += 1
                            
                    if roll_neighbors < 4:
                        counter += 1
                        grid[r][c] = "x"
        return counter        
  
    def solve2(self):
        totalCount = 0
        with open("./day_4/input.txt") as file:
            grid = list()
            next_line = file.readline().strip()
            while next_line:
                row = list(next_line)
                grid.append(row)
                
                next_line = file.readline().strip()
            counter = 0
            while True:
                for r in range(len(grid)):
                    for c in range(len(grid[r])):
                        if grid[r][c] == "x":
                           grid[r][c] = "." 

                for r in range(len(grid)):
                    for c in range(len(grid[r])):
                        roll_neighbors = 0
                         # check for first row and first and last column of it
                        # check for last row and first and last column of it
                        # just check for first and last column
                        if grid[r][c] != "@":
                            continue

                        # check top
                        if r != 0:
                            if self.check_if_roll(grid[r-1][c]):
                                roll_neighbors += 1
                        # bottom
                        if r != len(grid) - 1:
                             if self.check_if_roll(grid[r+1][c]):
                                roll_neighbors += 1

                        # check right
                        if c != len(grid[r]) - 1:
                            if self.check_if_roll(grid[r][c+1]):
                                roll_neighbors += 1
                         # check left
                        if c != 0:
                            if self.check_if_roll(grid[r][c-1]):
                                roll_neighbors += 1

                        # left up corner
                        if c != 0 and r != 0:
                            if self.check_if_roll(grid[r-1][c-1]):
                                roll_neighbors += 1
                        # right up corner
                        if c != len(grid[r]) - 1 and r != 0:
                            if self.check_if_roll(grid[r-1][c+1]):
                                roll_neighbors += 1

                        # right bottom corner
                        if c != len(grid[r]) - 1 and r != len(grid) - 1:
                            if self.check_if_roll(grid[r+1][c+1]):
                                roll_neighbors += 1

                        # left bottom corner
                        if c != 0 and r != len(grid) - 1:
                            if self.check_if_roll(grid[r+1][c-1]):
                                roll_neighbors += 1

                        if roll_neighbors < 4:
                            counter += 1
                            grid[r][c] = "x"
                
                if counter == 0:
                    break
                totalCount += counter
                counter = 0
                
            
            return totalCount        
                        
    def check_if_roll(self, elem: str)-> bool :
        return elem == "@" or elem == "x"
                    
                        
                        


print(Solution().solve2())