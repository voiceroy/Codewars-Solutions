fn basic_op(operator: char, value1: i32, value2: i32) -> i32 {
    match operator {
        '+' => return value1 + value2,
        '-' => return value1 - value2,
        '*' => return value1 * value2,
        '/' => return value1 / value2,
        _ => return 0,
    }
}
