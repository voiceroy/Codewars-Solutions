use std::cmp::Ordering;

fn solve(s: &str) -> String {
    let upper = s.chars().filter(|x| x.is_ascii_uppercase()).count();

    match upper.cmp(&(s.len() - upper)) {
        Ordering::Greater => return s.to_ascii_uppercase(),
        _ => return s.to_ascii_lowercase(),
    }
}
