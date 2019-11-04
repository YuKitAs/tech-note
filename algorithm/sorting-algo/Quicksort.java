public class Quicksort {
    public void sort(int[] arr, int l, int r) {
        if (l < r) {
            int par = partition(arr, l, r);
            sort(arr, l, par - 1);
            sort(arr, par + 1, r);
        }
    }

    private int partition(int[] arr, int l, int r) {
        int p = arr[r]; // select the last element as pivot
        int i = l; // left pointer
        int j = r - 1; // right pointer
        while (true) {
            while (i < r && arr[i] < p) {
                i++;
            }

            while (j > 0 && arr[j] > p) {
                j--;
            }

            if (i < j && arr[i] > p && arr[j] < p) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }

            if (i >= j) {
                // swap pivot to i
                int temp = arr[i];
                arr[i] = p;
                arr[r] = temp;
                return i;
            }
        }
    }
}
