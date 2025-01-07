import java.util.List;
import java.util.Arrays;

class Solution {
    private boolean isSubstring(String word, String[] text) {
        for (String t : text) {
            if (t.contains(word) && !t.equals(word)) {
                return true;
            }
        }
        return false;
    }

    public List<String> stringMatching(String[] words) {
        return Arrays.asList(words)
            .stream()
            .filter(word ->
                isSubstring(word, words)
            ).toList();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.stringMatching(new String[] {"mass", "as", "superhero", "hero"}));
        System.out.println(s.stringMatching(new String[] {"leetcode", "et", "code"}));
        System.out.println(s.stringMatching(new String[] {"blue", "green", "bu"}));
    }
}
