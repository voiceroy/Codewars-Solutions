fn evaporator(content: f64, evap_per_day: i32, threshold: i32) -> i32 {
    let mut current = content;
    let evap_per_day = (evap_per_day as f64) / 100.0;
    let threshold = (threshold as f64) / 100.0;

    if (current / content) < (threshold) {
        return 0;
    }

    let mut days: i32 = 0;

    while (current / content) >= (threshold) {
        current -= current * evap_per_day;
        days += 1;
    }

    return days;
}
