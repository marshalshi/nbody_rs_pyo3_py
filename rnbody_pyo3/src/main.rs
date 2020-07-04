mod bn;

fn main() {
    let n = std::env::args_os().nth(1)
        .and_then(|s| s.into_string().ok())
        .and_then(|n| n.parse().ok())
        .unwrap_or(1000);
    let mut bodies = bn::BODIES;

    bn::offset_momentum(&mut bodies);
    println!("{:.9}", bn::energy(&bodies));

    bn::advance(&mut bodies, 0.01, n);

    println!("{:.9}", bn::energy(&bodies));
}
