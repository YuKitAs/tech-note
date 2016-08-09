package edu.kit.yukitas;

import java.util.List;

/**
 * Adapter
 */
public class SorterAdapter implements Sorter {
    @Override
    public int[] sort(int[] numbers) {
        List<Integer> sortedNumbers = new NumberSorter(numbers).sort();
        int size = sortedNumbers.size();
        int[] result = new int[size];
        for (int i = 0; i < size; i++) {
            result[i] = sortedNumbers.get(i).intValue();
        }

        return result;
    }
}
