fn ordered_count(sip: &str) -> Vec<(char, usize)> {
    let mut already_seen: Vec<char> = Vec::new();
    let mut counts: Vec<(char, usize)> = Vec::new();

    for char in sip.chars() {
        if !already_seen.contains(&char) {
            counts.push((char, sip.matches(char).count()));
            already_seen.push(char);
        }
    }

    return counts;
}
