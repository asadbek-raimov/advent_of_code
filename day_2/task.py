class Solution:
    def find_invalid_ids(self):
        invalid_ids_sum = 0
        with open("./day_2/input.txt", "r") as file:
            ranges = file.readline().split(",")
            for elem in ranges:
                start = int(elem.split("-")[0])
                end = int(elem.split("-")[1])
                
                if len(str(end)) % 2 == 0:
                    end_s = str(end)
                    if end_s[:int(len(end_s)/2)] == end_s[int(len(end_s)/2):]:
                        invalid_ids_sum += end
                
                for i in range(end - start):
                    curr = str(start + i)
                    if len(curr) % 2 == 0:
                        if curr[:int(len(curr)/2)] == curr[int(len(curr)/2):]:
                            invalid_ids_sum += int(curr)

    def find_invalid_ids_2(self):
        invalid_ids_sum = 0
        with open("./day_2/input.txt", "r") as file:
            ranges = file.readline().split(",")
            for elem in ranges:
                start = int(elem.split("-")[0])
                end = int(elem.split("-")[1])
                
                curr = str(end)
                progress = str()
                for i in range(len(curr) // 2):
                    progress += curr[i]
                    if curr.replace(progress, str()) == str():
                        invalid_ids_sum += int(curr)
                        break
                
                for i in range(end - start):
                    curr = str(start + i)
                    progress = str()
                    for i in range(len(curr) // 2):
                        progress += curr[i]
                        if curr.replace(progress, str()) == str():
                            invalid_ids_sum += int(curr)
                            break
            
        print(invalid_ids_sum)
            
        
        
Solution().find_invalid_ids_2()