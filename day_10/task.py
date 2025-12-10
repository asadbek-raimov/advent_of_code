import re
import pulp


def parse_machine_part2(line: str):
    """
    Parse one line into:
      - target: list of ints (joltage requirements)
      - A: matrix (list of rows) with entries 0/1 of shape [counters][buttons]
    """
    line = line.strip()
    if not line:
        return None

    # Joltage target in { ... }
    m_target = re.search(r"\{([^}]*)\}", line)
    if not m_target:
        raise ValueError("No target joltage in line: " + line)
    target = [int(x) for x in m_target.group(1).split(",")]
    K = len(target)

    # Button index lists from ( ... )
    button_index_lists = []
    for button_str in re.findall(r"\(([^)]*)\)", line):
        button_str = button_str.strip()
        if not button_str:
            continue
        indices = [int(x) for x in button_str.split(",")]
        button_index_lists.append(indices)

    B = len(button_index_lists)

    # Build A: shape (K x B), A[i][j] = 1 if button j affects counter i
    A = [[0] * B for _ in range(K)]
    for j, indices in enumerate(button_index_lists):
        for idx in indices:
            if idx < 0 or idx >= K:
                raise ValueError(f"Button index {idx} out of range for {K} counters")
            A[idx][j] = 1

    return target, A


def min_presses_joltage_lp(target, A):
    """
    Solve:
        A x = target,  x >= 0 integer, minimize sum(x)
    using pulp (MILP).
    """
    K = len(target)
    if K == 0:
        return 0
    B = len(A[0])

    # Define problem
    prob = pulp.LpProblem("AOC_Day10_Part2", pulp.LpMinimize)

    # Variables: non-negative integers x_j
    x_vars = [pulp.LpVariable(f"x{j}", lowBound=0, cat="Integer") for j in range(B)]

    # Objective: minimize total presses
    prob += pulp.lpSum(x_vars)

    # Constraints: for each counter i, sum_j A[i][j] * x_j = target[i]
    for i in range(K):
        prob += pulp.lpSum(A[i][j] * x_vars[j] for j in range(B)) == target[i]

    # Solve (CBC solver is bundled with pulp)
    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[prob.status] != "Optimal":
        raise RuntimeError("No optimal solution found for machine")

    # Sum the presses
    presses = sum(int(v.value()) for v in x_vars)
    return presses


def solve_part2(filename="./day_10/input.txt"):
    total = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            target, A = parse_machine_part2(line)
            presses = min_presses_joltage_lp(target, A)
            total += presses
    print("Part 2: total minimal button presses:", total)
    return total


if __name__ == "__main__":
    solve_part2("./day_10/input.txt")