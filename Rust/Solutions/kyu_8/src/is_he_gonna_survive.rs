fn hero(bullets: u16, dragons: u16) -> bool {
    return match dragons {
        0 => false,
        _ => bullets / dragons >= 2,
    };
}
