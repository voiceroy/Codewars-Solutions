fn string_to_array(s: &str) -> Vec<String> {
    return s
        .split(" ")
        .map(|word| String::from(word))
        .collect::<Vec<String>>();
}
