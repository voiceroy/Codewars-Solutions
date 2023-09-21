def seats_in_theater(tot_cols: int, tot_rows: int, col: int, row: int) -> int:
    return (tot_cols - (col - 1)) * (tot_rows - row)
