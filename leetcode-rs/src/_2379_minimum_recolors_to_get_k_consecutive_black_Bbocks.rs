use std::cmp::min;

pub fn count_white(s: String) -> i32 {
    s.chars().filter(|&c| c == 'W').count() as i32
}
pub fn minimum_recolors(blocks: String, k: i32) -> i32 {
    let n = blocks.len();
    let substrings: Vec<String> = blocks.chars()
        .collect::<Vec<_>>()
        .windows(k as usize)
        .map(|w| w.iter().collect())
        .collect();
    let mut minimum_ops = k;
    for x in substrings {
        let num_white = count_white(x);
        minimum_ops = min(minimum_ops, num_white);
        if minimum_ops == 0 {
            return 0;
        }
    }
    minimum_ops
}

fn main() {
    println!("{}", minimum_recolors(String::from("WBBWWBBWBW"), 7));
    println!("{}", minimum_recolors(String::from("WBWBBBW"), 2));
}