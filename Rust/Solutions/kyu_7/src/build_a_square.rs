fn generate_shape(n: i32) -> String {
    return (0..n)
        .map(|_| "+".repeat(n as usize))
        .collect::<Vec<String>>()
        .join("\n");
}
