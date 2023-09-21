fn find_difference(a: &[i32; 3], b: &[i32; 3]) -> i32 {
    return (a.iter().product::<i32>() - b.iter().product::<i32>()).abs();
}
