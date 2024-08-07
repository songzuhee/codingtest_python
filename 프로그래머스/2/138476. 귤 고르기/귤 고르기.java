import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int size : tangerine) {
            map.put(size, map.getOrDefault(size, 0) + 1);
        }

        ArrayList<Integer> counts = new ArrayList<>(map.values());
        Collections.sort(counts, Collections.reverseOrder());

        int totalCount = 0;
        for (int count : counts) {
            totalCount += count;
            answer++;
            if (totalCount >= k) {
                break;
            }
        }

        return answer;
    }
}