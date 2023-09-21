fn fake_bin(s: &str) -> String {
    let mut result = String::new();

    for num in s.chars() {
        if num.to_digit(10) <= Some(4) {
            result.push('0');
        } else {
            result.push('1');
        }
    }

    result
}
