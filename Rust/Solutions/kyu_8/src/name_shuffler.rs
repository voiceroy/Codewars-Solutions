fn name_shuffler(s: &str) -> String {
    return s.split(' ').rev().collect::<Vec<&str>>().join(" ");
}
