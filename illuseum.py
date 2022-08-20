# Solving the puzzle from Illuseum, Berlin

board = ''.join([
    ' ', '4', '*', ' ',
    '2', '*', '*', '2',
    '|', '3', '-', '|',
    '2', '1', '1', '2',
    '|', '1', '1', '|'
])

directions = {
    -1: "left",
    -4: "up",
    +1: "right",
    +2: "right",
    +4: "down",
    +8: "down",
}


class Node:
    def __init__(self, depth, board, predecessor, move):
        self.depth = depth
        self.board = board
        self.predecessor = predecessor
        self.move = move


def print_board(board):
    for i in range(0, 20):
        print(board[i], end=" ")
        if i % 4 == 3:
            print()
    print()


def is_solution(board):
    return board[13] == '4'


def check_board(b):
    if 2 != b.count(' ') or 4 != b.count('1') or 4 != b.count('2') or 1 != b.count('3') or 1 != b.count('4'):
        print("*** Incorrect board: ")
        print_board(b)
        exit()


def exists_and_is_empty(board, index, offset):
    # check that destination is within the board
    if index + offset < 0 or index + offset >= 20:
        return False

    # check that we are not wrapping horizontally
    if offset == 1 and index % 4 == 3:
        return False
    if offset == -1 and index % 4 == 0:
        return False
    if offset == 2 and index % 4 >= 2:
        return False
    if offset == -2 and index % 4 <= 1:
        return False

    # is the destination field empty?
    return board[index+offset] == ' '


def print_solution(node):
    nodes = []
    while node.predecessor:
        nodes.append(node)
        node = node.predecessor
    nodes.reverse()
    for i in range(0, len(nodes)):
        node = nodes[i]
        print(f"Step {i}:")
        print(f"Move: {node.move}")
        print_board(node.board)


def get_next_boards_and_moves(board):
    boards = []
    moves = []

    for index in range(0, 20):
        b = board[index]

        if b == '1':
            for offset in [-1, +4, +1, -4]:
                if exists_and_is_empty(board, index, offset):
                    # swap single with empty
                    board_new = list(board)
                    board_new[index+offset] = '1'
                    board_new[index] = ' '
                    boards.append(''.join(board_new))
                    moves.append(f"{b} {directions[offset]}")

        elif b == '2':
            for offset in [-1, +1]:
                if exists_and_is_empty(board, index, offset) and exists_and_is_empty(board, index, offset+4):
                    board_new = list(board)
                    board_new[index+offset] = '2'
                    board_new[index] = ' '
                    board_new[index+offset+4] = '|'
                    board_new[index+4] = ' '
                    boards.append(''.join(board_new))
                    moves.append(f"{b} {directions[offset]}")
            if exists_and_is_empty(board, index, -4):
                board_new = list(board)
                board_new[index-4] = '2'
                board_new[index] = '|'
                board_new[index+4] = ' '
                boards.append(''.join(board_new))
                moves.append(f"{b} {directions[-4]}")
            if exists_and_is_empty(board, index, +8):
                board_new = list(board)
                board_new[index] = ' '
                board_new[index+4] = '2'
                board_new[index+8] = '|'
                boards.append(''.join(board_new))
                moves.append(f"{b} {directions[+8]}")

        elif b == '3':
            for offset in [-4, +4]:
                if exists_and_is_empty(board, index, offset) and exists_and_is_empty(board, index, offset+1):
                    board_new = list(board)
                    board_new[index+offset] = '3'
                    board_new[index] = ' '
                    board_new[index+offset+1] = '-'
                    board_new[index+1] = ' '
                    boards.append(''.join(board_new))
                    moves.append(f"{b} {directions[offset]}")
            if exists_and_is_empty(board, index, -1):
                board_new = list(board)
                board_new[index-1] = '3'
                board_new[index] = '-'
                board_new[index+1] = ' '
                boards.append(''.join(board_new))
                moves.append(f"{b} {directions[-1]}")
            if exists_and_is_empty(board, index, +2):
                board_new = list(board)
                board_new[index] = ' '
                board_new[index+1] = '3'
                board_new[index+2] = '-'
                boards.append(''.join(board_new))
                moves.append(f"{b} {directions[+2]}")

        elif b == '4':
            if exists_and_is_empty(board, index, -1) and exists_and_is_empty(board, index, +3):
                board_new = list(board)
                board_new[index-1] = '4'
                board_new[index] = '*'
                board_new[index+1] = ' '
                board_new[index+3] = '*'
                board_new[index+4] = '*'
                board_new[index+5] = ' '
                boards.append(''.join(board_new))
                moves.append(f"{b} {directions[+4]}")
            if exists_and_is_empty(board, index, +2) and exists_and_is_empty(board, index, +6):
                board_new = list(board)
                board_new[index] = ' '
                board_new[index+1] = '4'
                board_new[index+2] = '*'
                board_new[index+4] = ' '
                board_new[index+5] = '*'
                board_new[index+6] = '*'
                boards.append(''.join(board_new))
                moves.append(f"{b} {directions[+2]}")
            if exists_and_is_empty(board, index, -4) and exists_and_is_empty(board, index, -3):
                board_new = list(board)
                board_new[index-4] = '4'
                board_new[index-3] = '*'
                board_new[index] = '*'
                board_new[index+1] = '*'
                board_new[index+4] = ' '
                board_new[index+5] = ' '
                boards.append(''.join(board_new))
                moves.append(f"{b} {directions[-4]}")
            if exists_and_is_empty(board, index, +8) and exists_and_is_empty(board, index, +9):
                board_new = list(board)
                board_new[index] = ' '
                board_new[index+1] = ' '
                board_new[index+4] = '4'
                board_new[index+5] = '*'
                board_new[index+8] = '*'
                board_new[index+9] = '*'
                boards.append(''.join(board_new))
                moves.append(f"{b} {directions[+8]}")

    return boards, moves


def bfs(visited, board):
    global board_no
    check_board(board)
    visited.append(board)
    queue.append(Node(0, board, None, None))

    while queue:
        node = queue.pop(0)
        board_no = board_no + 1

        if is_solution(node.board):
            print(f"+++ Heureka! Found the solution! Depth = {node.depth}")
            print_solution(node)
            return

        boards, moves = get_next_boards_and_moves(node.board)

        for i in range(0, len(boards)):
            if boards[i] not in visited:
                check_board(boards[i])
                visited.append(boards[i])
                queue.append(Node(node.depth+1, boards[i], node, moves[i]))


visited = []
queue = []
board_no = 0
bfs(visited, board)
print(f"=== checked {board_no} boards to find solution ===")
