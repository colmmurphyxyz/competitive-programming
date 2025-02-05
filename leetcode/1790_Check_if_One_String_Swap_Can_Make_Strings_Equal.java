import java.util.ArrayList;

class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        ArrayList<Integer> mismatchedIndices = new ArrayList<>();
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                mismatchedIndices.add(i);
            }
        }
        if (mismatchedIndices.isEmpty()) return true;
        if (mismatchedIndices.size() != 2) return false;
        int j = mismatchedIndices.get(0);
        int k = mismatchedIndices.get(1);
        return s1.charAt(j) == s2.charAt(k) && s1.charAt(k) == s2.charAt(j);
    }

    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.areAlmostEqual("bank", "kanb"));
        System.out.println(s.areAlmostEqual("attack", "defend"));
        System.out.println(s.areAlmostEqual("kelb", "kelb"));
        System.out.println(s.areAlmostEqual("abcd", "dcba"));
        System.out.println(s.areAlmostEqual("fkhiweuvhwiwsulggpdkyyrbxsikcbnijmaxvdvcyldhagaligllfcfjrmwvvjrkchiqftmypywcgiyzvdgs", "ikihhzfmflcfrkbpvckcsjrwewhibdmyvsuciajlihrguytwnaxysgimwfpyiggvwyxayqgvjvvcglkllddd"));;
    }
}