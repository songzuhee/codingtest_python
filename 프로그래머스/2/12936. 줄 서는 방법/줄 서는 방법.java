import java.util.ArrayList;

class Solution {
    public int[] solution(int n, long k) {
        ArrayList<Integer> al = new ArrayList<>();
        int[] result = new int[n];
        long fn = 1;
        for(int i = 1; i <= n; i++) {
            fn *= i;
            al.add(i);
        }
        k--;
        
        int idx = 0;
        while(n > 0) {
            fn /= n;
            int index = (int)(k / fn);
            result[idx++] = al.get(index);
            al.remove(index);
            k %= fn;
            n--;
        }
        return result;
    }
}