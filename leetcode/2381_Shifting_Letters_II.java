import java.util.Arrays;

class Solution {
    public String shiftingLetters(String s, int[][] shifts) {
        int[] deltas = new int[s.length()];
        Arrays.fill(deltas, 0);
        for (int[] op : shifts) {
            int start = op[0];
            int end = op[1];
            int direction = op[2] == 1 ? 1 : -1;
            for (int i = start; i <= end; i++) {
                deltas[i] += direction;
            }
        }

        // char[] shifted = new char[s.length()];
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < s.length(); i++) {
            int codePoint = ((int) s.charAt(i)) - 97;
            int delta = deltas[i];
            int shifted = Math.floorMod(codePoint + delta, 26);
            sb.appendCodePoint(shifted + 97);
        }


        // return new String(shifted);
        return sb.toString();
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] shifts = new int[][] {
            new int[] {0, 1, 0},
            new int[] {1, 2, 1},
            new int[] {0, 2, 1}
        };
        System.out.println(s.shiftingLetters("abc", shifts));
        shifts = new int[][] {
            new int[] {0, 0, 0},
            new int[] {1, 1, 1}
        };
        System.out.println(s.shiftingLetters("dztz", shifts));
        shifts = new int[][] {
            new int[] {4,8,0},
            new int[] {4,4,0},
            new int[] {2,4,0},
            new int[] {2,4,0},
            new int[] {6,7,1},
            new int[] {2,2,1},
            new int[] {0,2,1},
            new int[] {8,8,0},
            new int[] {1,3,1}
        };
        System.out.println(s.shiftingLetters("xuwdbdqik", shifts));
    }
}
