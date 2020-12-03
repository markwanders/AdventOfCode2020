fn main() {
    let contents = std::fs::read_to_string("input.txt").expect("should be there");
    let mut x = 0;
    let mut trees = 0;
    for line in contents.lines() {
       if line.chars().nth(x).unwrap() == '#' {
           trees+=1;
       }
        x+=3;
        x%=line.chars().count()
    };

    println!("{}", trees)
}