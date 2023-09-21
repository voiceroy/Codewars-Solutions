fn enough(cap: i32, on: i32, wait: i32) -> i32 {
    match (on + wait) <= cap {
        true => return 0,
        false => return on + wait - cap,
    }
}
