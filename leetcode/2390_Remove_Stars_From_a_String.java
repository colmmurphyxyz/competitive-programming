import java.util.Stack;

class Solution {
    public String removeStars(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c != '*') {
                stack.push(c);
            } else {
                if (!stack.isEmpty()) stack.pop();
            }
        }
        char[] res = new char[stack.size()];
        for (int i = stack.size() - 1; i >= 0; i--) {
            res[i] = stack.pop();
        }
        return new String(res);
    }

    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.removeStars("leet**cod*e"));
        System.out.println(s.removeStars("erase*****"));
    }
}