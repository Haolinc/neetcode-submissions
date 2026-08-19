// Definition for a pair
// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {
        List<List<Pair>> sortedList = new ArrayList<>();
        sortList(sortedList, pairs);
        return sortedList;
    }
    public void sortList(List<List<Pair>> sortedList, List<Pair> pairs){
        
        if (sortedList.size() == pairs.size())
            return;

        for (int i = 0; i < sortedList.size(); i++){
            if (pairs.get(sortedList.size()).key < pairs.get(i).key){
                Pair pair = pairs.get(sortedList.size());
                pairs.remove(sortedList.size());
                pairs.add(i, pair);
                break;
            }
        }
        sortedList.add(new ArrayList<>(pairs));
        
        sortList(sortedList, pairs);
    }
}
