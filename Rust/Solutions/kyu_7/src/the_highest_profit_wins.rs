fn min_max(lst: &[i32]) -> (i32, i32) {
    return (*lst.iter().min().unwrap(), *lst.iter().max().unwrap());
}
