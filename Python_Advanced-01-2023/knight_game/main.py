n = int(input())
board = [list(input()[0:n]) for _ in range(n)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2)
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks = []

    for row in range(n):
        for col in range(n):
            if board[row][col] == 'K':
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < n and 0 <= pos_col < n and board[pos_row][pos_col] == 'K':
                        attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_most_attacks = [row, col]

    if max_attacks > 0:
        board[knight_with_most_attacks[0]][knight_with_most_attacks[1]] = '0'
        removed_knights += 1
    else:
        print(removed_knights)
        break
