fn divisors(n: u32) -> u32 {
    // 1 is already a divisor of any positive real number
    let mut count = 1;

    for i in 2..(n + 1) {
        if n % i == 0 {
            count += 1;
        }
    }
    return count;
}
