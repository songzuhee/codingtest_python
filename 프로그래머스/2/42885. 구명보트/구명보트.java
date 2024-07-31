import java.util.Arrays;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        Arrays.sort(people);
        int i = 0;
        int j = people.length - 1;
        
        while (i <= j) {
            answer += 1;
            if (people[i] + people[j] <= limit){
                // limit보다 작으면 무거운사람만
                i +=1;
            } 
            // 크면 둘다 태움
            j -= 1; 
        }
        return answer;
    }
}