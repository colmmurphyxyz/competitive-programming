import java.util.HashSet;
import java.util.Arrays;

class Solution {
    private HashSet<Integer> isTravelNeeded;

    private int solve(int[] dp, int[] days, int[] costs, int currDay) {
        if (currDay > days[days.length - 1]) {
            return 0;
        }

        // if we do not need to travel on this day, move to the next
        if (!isTravelNeeded.contains(currDay)) {
            return solve(dp, days, costs, currDay + 1);
        }

        // if this day has already been calculated, return the stored answer
        if (dp[currDay] != -1) {
            return dp[currDay];
        }

        int oneDay = costs[0] + solve(dp, days, costs, currDay + 1);
        int sevenDay = costs[1] + solve(dp, days, costs, currDay + 7);
        int thirtyDay = costs[2] + solve(dp, days, costs, currDay + 30);

        dp[currDay] = Math.min(oneDay, Math.min(sevenDay, thirtyDay));
        return dp[currDay];
    }

    public int mincostTickets(int[] days, int[] costs) {
        isTravelNeeded = new HashSet<>();
        int lastDay = days[days.length - 1];
        int dp[] = new int[lastDay + 1];
        Arrays.fill(dp, -1);

        for (int day : days) {
            isTravelNeeded.add(day);
        }

        return solve(dp, days, costs, 1);
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.mincostTickets(
            new int[] {1, 4, 6, 7, 8, 20},
            new int[] {2, 7, 15})
        );
        System.out.println(s.mincostTickets(
            new int[] {1,2,3,4,5,6,7,8,9,10,30,31},
            new int[] {2, 7, 15})
        );
    }
}