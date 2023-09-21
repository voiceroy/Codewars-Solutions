fn bool_to_word(value: bool) -> &'static str {
    if value {
        return "Yes";
    } else {
        return "No";
    }
}
