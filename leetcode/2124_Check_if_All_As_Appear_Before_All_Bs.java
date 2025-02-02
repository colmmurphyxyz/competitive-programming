class Solution {
    public boolean checkString(String s) {
        boolean seenB = false;
        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            if (current == 'a') {
                if (seenB) return false;
            } else {
                seenB = true;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.checkString("aaabbb"));
        System.out.println(s.checkString("abab"));
        System.out.println(s.checkString("bbb"));
    }
}