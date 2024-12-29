import java.util.ArrayDeque;
import java.util.Deque;
import java.lang.Math;

class Solution {
    private boolean isVowel(char c) {
        switch (c) {
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u': return true;
            default: return false;
        }
    }

    public int maxVowels(String s, int k) {
        Deque<Character> d = new ArrayDeque<>(k);
        int currentVowels = 0;
        for (int i = 0; i < k; i++) {
            char c = s.charAt(i);
            d.addLast(c);
            if (isVowel(c)) currentVowels++;
        }
        int maxVowels = currentVowels;

        for (int i = 1; i <= s.length() - k; i++) {
            char old = d.removeFirst();
            if (isVowel(old)) currentVowels--;
            char next = s.charAt(i + k - 1);
            d.addLast(next);
            if (isVowel(next)) currentVowels++;

            maxVowels = Math.max(maxVowels, currentVowels);
        }

        return maxVowels;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.maxVowels("abciiidef", 3));
        System.out.println(s.maxVowels("aeiou", 2));
        System.out.println(s.maxVowels("leetcode", 3));
    }
}