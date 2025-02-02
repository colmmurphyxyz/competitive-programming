import java.util.regex.MatchResult;
import java.util.regex.Pattern;

class Solution {
    private boolean isSorted(Integer[] nums) {
        if (nums.length == 1) return true;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] <= nums[i - 1]) return false;
        }

        return true;
    }
    public boolean areNumbersAscending(String s) {
        Integer[] matches = Pattern.compile("\\d+")
            .matcher(s)
            .results()
            .map(MatchResult::group)
            .map(Integer::parseInt)
            .toArray(Integer[]::new);

        return isSorted(matches);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"));
        System.out.println(s.areNumbersAscending("hello world 5 x 5"));
        System.out.println(s.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"));
    }
}