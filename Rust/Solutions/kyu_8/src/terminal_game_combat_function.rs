fn combat(health: f32, damage: f32) -> f32 {
    return (health - damage).max(0.0);
}
