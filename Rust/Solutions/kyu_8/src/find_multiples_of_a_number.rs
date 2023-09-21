fn find_multiples(n: u32, limit: u32) -> Vec<u32> {
    return (n..=limit).filter(|x| x % n == 0).collect();
}
