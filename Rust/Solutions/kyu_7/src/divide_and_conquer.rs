use either::Either;

fn div_con(arr: &[Either<i32, String>]) -> i32 {
    arr.iter().cloned().fold(0, |a, x| {
        a + x.either(|x| x, |x| -x.parse::<i32>().unwrap())
    })
}
