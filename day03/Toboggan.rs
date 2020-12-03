fn main() {
    let contents = std::fs::read_to_string("input.txt").expect("should be there");
    let mut answer :i64 = 1;
    let slopes = [(1,1), (3,1), (5,1), (7,1),(1,2)];
    for slope in &slopes {
        let mut x = 0;
        let mut trees = 0;
        for line in contents.lines().step_by(slope.1) {
            if line.chars().nth(x).unwrap() == '#' {
                trees += 1;
            }
            x += slope.0;
            x %= line.chars().count()
        };

        println!("({}, {}): {}", slope.0, slope.1, trees);
        answer*=trees;
    }
    println!("{}", answer)
}