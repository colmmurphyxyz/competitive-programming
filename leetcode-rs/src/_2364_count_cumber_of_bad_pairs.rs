use std::collections::HashMap;
use std::collections::HashSet;

pub fn count_bad_pairs(nums: Vec<i32>) -> i64 {
    let mut map: HashMap<i32, HashSet<usize>> = HashMap::new();
    let mut good_pairs = 0i64;
    for i in (0 .. nums.len()).rev() {
        let k = nums[i];
        let diff = k - i as i32;
        if map.contains_key(&diff) {
            good_pairs += map.get_mut(&diff).unwrap().len() as i64;
            map.get_mut(&diff).unwrap().insert(i);
        } else {
            map.insert(diff, HashSet::from([i]));
        }
    }
    // println!("{:?}", map);

    let n = nums.len() as i64;
    ((n * (n - 1)) / 2) - good_pairs
}

fn main() {
    println!("{}", count_bad_pairs(vec![4, 1, 3, 3]));
    println!("{}", count_bad_pairs(vec![1, 2, 3, 4, 5]));
    println!("{}", count_bad_pairs(vec![1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]));
}
