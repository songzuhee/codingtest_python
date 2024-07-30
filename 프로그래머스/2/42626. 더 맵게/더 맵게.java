import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> priorityQueueLowest = new PriorityQueue<>();
        
        for(int s : scoville) {
            priorityQueueLowest.add(s);
        }
        
        while(priorityQueueLowest.size() > 1 && priorityQueueLowest.peek() < K) {
            int a = priorityQueueLowest.poll(); // 가장 작은 값
            int b = priorityQueueLowest.poll(); // 두번째로 작은 값
            int result = a + (b*2);
            priorityQueueLowest.add(result);
            answer++;
        }
        if(priorityQueueLowest.peek() < K){
            return -1;
        }
        return answer;
    }
}