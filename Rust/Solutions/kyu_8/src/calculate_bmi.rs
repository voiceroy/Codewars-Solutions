fn bmi(weight: u32, height: f32) -> &'static str {
    let bmi: f32 = (weight as f32) / height.powf(2.);

    match bmi {
        bmi if bmi <= 18.5 => "Underweight",
        bmi if bmi <= 25.0 => "Normal",
        bmi if bmi <= 30.0 => "Overweight",
        _ => "Obese",
    }
}
