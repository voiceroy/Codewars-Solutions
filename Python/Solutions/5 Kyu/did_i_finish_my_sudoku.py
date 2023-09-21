def done_or_not(board: list) -> str:

    # Check the rows
    for row in board:
        if len(row) != len(set(row)):
            return "Try again!"

    # Check the columns
    for column_no in range(9):
        column = [board[y][column_no] for y in range(9)]
        if len(column) != len(set(column)):
            return "Try again!"

    # Check the blocks
    for block_y in range(0, 9, 3):
        for block_x in range(0, 9, 3):
            block = [
                x
                for row in [
                    board[block_y + i][block_x : block_x + 3] for i in range(3)
                ]  # Get 3x3 block
                for x in row  # Flatten list
            ]
            if len(block) != len(set(block)):
                return "Try again!"

    return "Finished!"
