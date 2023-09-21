fn remove_every_other(arr: &[u8]) -> Vec<u8> {
    return arr.iter().step_by(2).copied().collect();
}
