pub fn get_age(age: &str) -> u32 {
    return age.chars().nth(0).unwrap().to_digit(10).unwrap();
}
