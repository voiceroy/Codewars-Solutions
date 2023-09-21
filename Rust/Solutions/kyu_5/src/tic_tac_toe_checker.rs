fn is_solved(board: &[&[u8; 3]; 3]) -> i8 {
    // Check rows
    for row in board {
        let row_string = row.iter().map(|x| x.to_string()).collect::<String>();

        if row_string.matches('1').count() == 3 {
            return 1;
        } else if row_string.matches('2').count() == 3 {
            return 2;
        }
    }

    // Check columns
    for column in 0..3 {
        let column_string = board
            .iter()
            .map(|row| row[column].to_string())
            .collect::<String>();

        if column_string.matches('1').count() == 3 {
            return 1;
        } else if column_string.matches('2').count() == 3 {
            return 2;
        }
    }

    // Check diagonals
    let diag_1 = [board[0][0], board[1][1], board[2][2]]
        .iter()
        .map(|x| x.to_string())
        .collect::<String>();

    let diag_2 = [board[0][2], board[1][1], board[2][0]]
        .iter()
        .map(|x| x.to_string())
        .collect::<String>();

    for i in "12".chars() {
        if diag_1.matches(i).count() == 3 || diag_2.matches(i).count() == 3 {
            return i.to_digit(10).unwrap() as i8;
        }
    }

    // Check if the board is not yet finished
    if board.iter().any(|row| row.contains(&0)) {
        return -1;
    } else {
        return 0; // Draw
    }
}
