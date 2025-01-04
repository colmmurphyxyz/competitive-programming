import java.util.Set;
import java.util.HashSet;

class Solution {
    private int[] appearences(String s, char x) {
        int i = 0;
        for (; i < s.length(); i++) {
            if (s.charAt(i) == x) {
                break;
            }
        }

        if (i == s.length() - 1) return null;

        int j = s.length() - 1;
        for (; j > i; j--) {
            if (s.charAt(j) == x) {
                return new int[] {i, j};
            }
        }
        return null;
    }

    public int countPalindromicSubsequence(String s) {
        int numPalindromes = 0;
        for (char x = 'a'; x <= 'z'; x++) {
            int[] idxs = appearences(s, x);
            if (idxs == null) {
                continue;
            }
            Set<Character> mids = new HashSet<Character>();
            for (int i = idxs[0] + 1; i < idxs[1]; i++) {
                mids.add(s.charAt(i));
            }
            numPalindromes += mids.size();
        }
        return numPalindromes;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.countPalindromicSubsequence("aabca"));
        System.out.println(s.countPalindromicSubsequence("bbcbaba"));
        System.out.println(s.countPalindromicSubsequence("adc"));
    }
}