fn bin_to_decimal(inp: &str) -> i32 {
    return i32::from_str_radix(inp, 2).unwrap_or(0);
}
