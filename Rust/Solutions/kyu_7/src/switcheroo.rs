fn switcheroo(s: &str) -> String {
    return s
        .chars()
        .map(|chr| match chr {
            'a' => 'b',
            'b' => 'a',
            _ => chr,
        })
        .collect();
}
