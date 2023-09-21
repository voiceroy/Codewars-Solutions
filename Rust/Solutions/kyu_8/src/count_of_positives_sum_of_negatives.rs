use std::cmp::Ordering;

fn count_positives_sum_negatives(input: Vec<i32>) -> Vec<i32> {
    if !input.is_empty() {
        let mut count_positives = 0;
        let mut sum_negatives = 0;

        for number in &input {
            match number.cmp(&0) {
                Ordering::Less => {
                    sum_negatives += number;
                }
                Ordering::Greater => count_positives += 1,
                Ordering::Equal => (), // Do nothing
            }
        }

        [count_positives, sum_negatives].to_vec()
    } else {
        [].to_vec()
    }
}
