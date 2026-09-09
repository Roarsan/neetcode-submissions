class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> map = new HashMap<>();
        List<Integer>[] list = new ArrayList[nums.length + 1];

        //initialise empty list
        for(int i = 0;i<nums.length;i++){
            list[i] = new ArrayList<>();
        }
        //mapping nums and it frequencies
        for(int n : nums){
            map.put(n,map.getOrDefault(n,0)+1);
        }

        // Step 2: loop through keyset and get the value associated which
        for (int n : map.keySet()) {
            int freq = map.get(n);
            //add number in list according to their freq
            if (list[freq] == null) {
                list[freq] = new ArrayList<>();
            }
            list[freq].add(n);
        }

        // Step 3: loop through list from the back and allAll to a result list
        List<Integer> result = new ArrayList<>();
        for (int i = list.length - 1; i >= 0 && result.size() < k; i--) {
            if (list[i] != null) {
                result.addAll(list[i]);
            }
        }

         // Step 4: create an array with size of k and loop in k to add the value into the new array
        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = result.get(i);
        }

        return res;

    }
}