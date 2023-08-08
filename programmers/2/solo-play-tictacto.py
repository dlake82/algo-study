def solution(board):
    def isEqualO(x):
        return all(i == "O" for i in x)

    def isEqualX(x):
        return all(i == "X" for i in x)

    answer = 0

    board = [list(b) for b in board]
    board2 = list(map(list, zip(*board)))

    o_cnt, x_cnt, o, x, cross1, cross2 = 0, 0, 0, 0, [], []

    for i in range(3):
        cross1.append(board[i][i])
        cross2.append(board[i][2 - i])

    o_cnt += 1 if isEqualO(cross1) else 0
    o_cnt += 1 if isEqualO(cross2) else 0
    x_cnt += 1 if isEqualX(cross2) else 0
    x_cnt += 1 if isEqualX(cross2) else 0

    for b in board:
        if isEqualO(b):
            o_cnt += 1
        if isEqualX(b):
            x_cnt += 1

    for b in board2:
        if isEqualO(b):
            o_cnt += 1
        if isEqualX(b):
            x_cnt += 1

    for r in board:
        for c in r:
            if c == "O":
                o += 1
            if c == "X":
                x += 1

    print(o_cnt, x_cnt, o, x, cross1, cross2)

    a = o_cnt == 0 and x_cnt == 0
    b = o_cnt == 1 and x_cnt == 0
    c = o_cnt == 0 and x_cnt == 1
    d = o_cnt == 2 and x_cnt == 0

    if a and o in (x, x + 1):
        return 1

    if b and o == x - 1:
        return 1

    if c and o == x:
        return 1

    if d and o == x - 1:
        return 1

    return 0


print(solution(["XO.", "OX.", "..X"]))
