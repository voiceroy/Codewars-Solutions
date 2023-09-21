fn nearest_sq(n: u32) -> u32 {
    return ((n as f32).sqrt().round() as u32).pow(2);
}
