class Solution {
    private int numSetBits(int x) {
        int n = 0;
        for (int i = 0; i < 32; i++) {
            if ((1 << i & x) > 0) {
                n++;
            }
        }
        return n;
    }

    private boolean isBitSet(int x, int idx) {
        return (1 << idx & x) > 0;
    }

    public int minimizeXor(int num1, int num2) {
        int n = numSetBits(num2);
        int ans = 0;
        for (int i = 31; i >= 0; i--) {
            if (n <= 0) break;
            if (isBitSet(num1, i)) {
                n--;
                ans |= 1 << i;
            }
        }
        // distribute remaining bits
        int i = 0;
        while (n > 0) {
            if (isBitSet(ans, i)) {
                i++;
                continue;
            };
            ans |= 1 << i;
            n--;
            i++;
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.minimizeXor(3, 5));
        System.out.println(s.minimizeXor(1, 12));
    }
}