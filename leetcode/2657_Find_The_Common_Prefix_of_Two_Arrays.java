import java.util.HashSet;
import java.util.Arrays;

class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        HashSet<Integer> seen = new HashSet<>();
        int count = 0;
        int n = A.length;
        int[] C = new int[n];
        for (int i = 0; i < A.length; i++) {
            int a = A[i];
            if (seen.contains(a)) {
                count++;
            } else {
                seen.add(a);
            }
            int b = B[i];
            if (seen.contains(b)) {
                count++;
            } else {
                seen.add(b);
            }
            C[i] = count;
        }

        return C;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(Arrays.toString(s.findThePrefixCommonArray(new int[] {1, 3, 2, 4}, new int[] {3, 1, 2, 4})));
        System.out.println(Arrays.toString(s.findThePrefixCommonArray(new int[] {2, 3, 1}, new int[] {3, 1, 2})));
    }
}