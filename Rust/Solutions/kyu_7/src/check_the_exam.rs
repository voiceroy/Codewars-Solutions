fn check_exam(arr_a: &[&str], arr_b: &[&str]) -> i64 {
    let mut score = 0;

    for (attempt, answer) in arr_a.iter().zip(arr_b) {
        if attempt.is_empty() || answer.is_empty() {
            score += 0
        } else if attempt == answer {
            score += 4
        } else {
            score -= 1
        }
    }

    return score.max(0);
}
