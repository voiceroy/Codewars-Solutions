fn derive(coefficient: u32, exponent: u32) -> String {
    return format!("{}x^{}", coefficient * exponent, exponent - 1);
}
