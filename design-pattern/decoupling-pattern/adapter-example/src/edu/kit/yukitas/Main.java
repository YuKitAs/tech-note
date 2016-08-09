package edu.kit.yukitas;

/**
 * Client
 */
public class Main {
    public static void main(String[] args) {
        int[] numbers = {4, 2, 1, 3};
        Sorter s = new SorterAdapter();
        int[] sortedNumbers = s.sort(numbers);
        for (int i : sortedNumbers) {
            System.out.print(i + " ");
        }
    }
}
