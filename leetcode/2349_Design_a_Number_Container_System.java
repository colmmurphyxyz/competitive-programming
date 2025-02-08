import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;

class NumberContainers {

    private Map<Integer, Integer> numberContainer;
    private Map<Integer, TreeSet<Integer>> indices;

    public NumberContainers() {
        this.numberContainer = new HashMap<>();
        this.indices = new HashMap<>();
    }
    
    public void change(int index, int number) {
        // System.out.printf("change(%d, %d)\n", index, number);
        Integer currentValue = numberContainer.get(index);
        if (currentValue != null) {
            indices.get(currentValue).remove(index);
        }
        numberContainer.put(index, number);

        TreeSet<Integer> indicesSet = indices.getOrDefault(number, new TreeSet<>());
        indicesSet.add(index);
        indices.put(number, indicesSet);
    }

    public int find(int number) {
        // System.out.printf("find(%d)\n", number);
        TreeSet<Integer> indicesSet = indices.get(number);
        if (indicesSet == null || indicesSet.isEmpty()) {
            return -1;
        }
        return indicesSet.first();
    }
    
    // public int find(int number) {
    //     Set<Integer> keys = numberContainer.keySet();
    //     for (int key : keys) {
    //         if (number == numberContainer.get(key)) {
    //             return key;
    //         }
    //     }
    //     return -1;
    // }

    public static void main(String[] args) {
        var nc = new NumberContainers();
        System.out.println(nc.find(10));
        nc.change(2, 10);
        nc.change(1, 10);
        nc.change(3, 10);
        nc.change(5, 10);
        System.out.println(nc.find(10));
        nc.change(1, 20);
        System.out.println(nc.find(10));
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.change(index,number);
 * int param_2 = obj.find(number);
 */