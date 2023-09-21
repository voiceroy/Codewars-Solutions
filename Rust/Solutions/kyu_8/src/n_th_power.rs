fn index(nums: &[u64], n: usize) -> Option<u64> {
    nums.get(n).map(|x| x.pow(n as u32))
}
