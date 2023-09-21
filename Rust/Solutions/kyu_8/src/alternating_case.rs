fn to_alternating_case(s: &str) -> String {
    let mut string = String::new();

    for letter in s.chars() {
        if letter.is_lowercase() {
            string.push(letter.to_ascii_uppercase())
        } else if letter.is_uppercase() {
            string.push(letter.to_ascii_lowercase())
        } else {
            string.push(letter)
        }
    }

    return string;
}
