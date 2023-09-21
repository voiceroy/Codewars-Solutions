fn sequence_sum(start: u32, end: u32, step: u32) -> u32 {
    let mut i = start;
    let mut total = 0;

    while i <= end {
        total += i;
        i += step;
    }

    return total;
}
