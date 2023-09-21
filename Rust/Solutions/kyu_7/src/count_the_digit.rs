fn nb_dig(n: i32, d: i32) -> i32 {
    let mut temp_string = String::new();

    for i in 0..=n {
        temp_string.push_str(&i.pow(2).to_string())
    }

    return temp_string.matches(&d.to_string()).count() as i32;
}
