use std::rc::Rc;
use std::cell::RefCell;

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
    pub fn is_leaf(root: &Rc<RefCell<TreeNode>>) -> bool {
        let node = root.borrow();
        node.left.is_none() && node.right.is_none()
    }

    pub fn get_leaf_sequence(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut stack: Vec<Rc<RefCell<TreeNode>>> = vec![root.unwrap()];
        let mut leaf_sequence: Vec<i32> = vec![];
        while !stack.is_empty() {
            let top = stack.pop().unwrap();
            if Self::is_leaf(&top) {
                leaf_sequence.push(top.borrow().val);
            } else {
                if let Some(right) = &top.borrow().right {
                    stack.push(Rc::clone(right));
                }
                if let Some(left) = &top.borrow().left {
                    stack.push(Rc::clone(left));
                }
            }
        }

        leaf_sequence
    }
    pub fn leaf_similar(root1: Option<Rc<RefCell<TreeNode>>>, root2: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let seq1 = Self::get_leaf_sequence(root1);
        let seq2 = Self::get_leaf_sequence(root2);
        println!("{:?}", seq1);
        println!("{:?}", seq2);
        seq1 == seq2
    }
}