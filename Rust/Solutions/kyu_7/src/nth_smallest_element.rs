fn nth_smallest(nums: &[i32], pos: usize) -> i32 {
    let mut sorted = nums.to_vec();
    sorted.sort();
    return sorted[pos - 1];
}
