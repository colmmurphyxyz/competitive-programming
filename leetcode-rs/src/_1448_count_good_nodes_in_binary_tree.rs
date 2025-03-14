use std::{cell::RefCell, rc::Rc};

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None
        }
    }
}

enum Solution {}

impl Solution {
    pub fn count_good_nodes(root: Option<Rc<RefCell<TreeNode>>>, curr_max: i32) -> i32 {
        match root {
            None => 0,
            Some(node) => {
                let val = node.borrow().val;
                if val >= curr_max {
                    return 1 + Self::count_good_nodes(node.borrow().left.clone(), val)
                        + Self::count_good_nodes(node.borrow().right.clone(), val);
                }
                Self::count_good_nodes(node.borrow().left.clone(), curr_max)
                + Self::count_good_nodes(node.borrow().right.clone(), curr_max)
            }
        }
    }

    pub fn good_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Self::count_good_nodes(root, i32::MIN)
    }
}

fn main() {
    let mut root = TreeNode { val: 3, left: None, right: None};
    root.left = Some(Rc::new(RefCell::new(TreeNode { 
        val: 1,
        left: Some(Rc::new(RefCell::new(TreeNode {
            val: 3,
            left: None,
            right: None
        }))),
        right: None
    })));
    root.right = Some(Rc::new(RefCell::new(TreeNode {
        val: 4,
        left: Some(Rc::new(RefCell::new(TreeNode {
            val: 1,
            left: None,
            right: None
        }))),
        right: Some(Rc::new(RefCell::new(TreeNode {
            val: 5,
            left: None,
            right: None
        })))
    })));
    println!("{:?}", root);
    println!("{}", Solution::good_nodes(Some(Rc::new(RefCell::new(root)))));
}