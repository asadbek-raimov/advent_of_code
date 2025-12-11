from functools import lru_cache


def solution(path: str)-> None:
    with open(path) as file:
        lines = file.read().splitlines()
        table: dict[str, tuple[str, ...]] = {}
        
        for line in lines:
            key, value = line.split(":")
            connections = value.strip().split(" ")
            table[key] = tuple(connections)
        
        starting = table["you"]
        
        def recur(startList: tuple, table: dict, passed: set = set())-> int :
            outs = 0
            for elem in startList:
                if table[elem][0] == "out":
                    outs += 1
                    passed.clear()
                else:
                    if elem in passed:
                        continue
                    else:
                        passed.add(elem)
                        outs += recur(table[elem], table, passed)
            return outs
        
        print(recur(starting, table))
        

def part2(path: str) -> None:
    with open(path) as file:
        lines = file.read().splitlines()
        table: dict[str, tuple[str, ...]] = {}

        for line in lines:
            key, value = line.split(":")
            connections = value.strip().split()
            table[key] = tuple(connections)

        if "out" not in table:
            table["out"] = tuple()

        SPECIAL = {"dac": 0, "fft": 1}

        @lru_cache(maxsize=None)
        def dfs(node: str, mask: int) -> int:
            if node in SPECIAL:
                mask |= 1 << SPECIAL[node]

            if node == "out":
                return 1 if mask == 0b11 else 0

            total = 0
            for nxt in table[node]:
                total += dfs(nxt, mask)
            return total

        count = dfs("svr", 0)
        print(count)


if __name__ == "__main__":
    part2("./day_11/input.txt")
        