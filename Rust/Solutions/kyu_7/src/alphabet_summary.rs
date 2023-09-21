fn solve(strings: &[String]) -> Vec<usize> {
    strings
        .iter()
        .map(|word| {
            word.to_ascii_lowercase()
                .chars()
                .zip('a'..='z')
                .filter(|(c1, c2)| c1 == c2)
                .count()
        })
        .collect()
}
