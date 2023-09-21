fn find_average(slice: &[f64]) -> f64 {
    if slice.is_empty() {
        return 0.0;
    } else {
        return slice.iter().sum::<f64>() / slice.len() as f64;
    }
}
