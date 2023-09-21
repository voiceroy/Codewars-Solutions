use std::collections::BTreeSet;

fn men_from_boys(xs: &[i16]) -> Vec<i16> {
    let evens: BTreeSet<i16> = xs.iter().copied().filter(|x| x % 2 == 0).collect();
    let odds: BTreeSet<i16> = xs.iter().copied().filter(|x| x % 2 != 0).collect();

    let mut evens: Vec<i16> = evens.iter().copied().collect();
    evens.extend(odds.iter().rev());

    return evens;
}
