package edu.kit.yukitas;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Adaptee
 */
public class NumberSorter {
    private List<Integer> numbers;

    public NumberSorter(int[] numbers) {
        this.numbers = Arrays.stream(numbers).boxed().collect(Collectors.toList());
    }

    public List<Integer> sort() {
        Collections.sort(numbers);
        return numbers;
    }
}
