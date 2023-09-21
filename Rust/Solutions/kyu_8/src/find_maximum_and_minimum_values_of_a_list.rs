fn maximum(arr: &[i32]) -> i32 {
    return *arr.iter().max().unwrap();
}

fn minimum(arr: &[i32]) -> i32 {
    return *arr.iter().min().unwrap();
}
