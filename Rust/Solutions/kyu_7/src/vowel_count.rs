fn get_count(string: &str) -> usize {
    let mut vowels_count: usize = 0;

    for chr in "aeiou".chars() {
        vowels_count += string.matches(chr).count()
    }

    return vowels_count;
}
