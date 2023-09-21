use std::collections::HashSet;

fn divisor_sum(n: i64) -> i64 {
    let mut divisors: HashSet<i64> = HashSet::new();

    for div in 2..((n as f64).sqrt().round() as i64 + 1) {
        if n % div == 0 {
            divisors.insert(div);
            divisors.insert(n / div);
        }
    }

    return divisors.iter().sum();
}

fn buddy(start: i64, limit: i64) -> Option<(i64, i64)> {
    for num in start..(limit + 1) {
        let m = divisor_sum(num);
        if m > num && divisor_sum(m) == num {
            return Some((num, m));
        }
    }
    return None;
}
