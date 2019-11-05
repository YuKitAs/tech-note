import java.util.Arrays;

public class Mergesort {
    public void sort(int[] arr, int l, int r) {
        if (l < r) {
            int m = (l + r) / 2;
            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
    }

    public void merge(int[] arr, int l, int m, int r) {
        int[] arrLeft = Arrays.copyOfRange(arr, l, m + 1); // range l..m
        int[] arrRight = Arrays.copyOfRange(arr, m + 1, r + 1); // range (m + 1)..r

        int nLeft = arrLeft.length;
        int nRight = arrRight.length;
        int i = 0, j = 0, k = l;
        while (i < nLeft && j < nRight) {
            if (arrLeft[i] <= arrRight[j]) {
                arr[k] = arrLeft[i++];
            } else {
                arr[k] = arrRight[j++];
            }
            k++;
        }

        // copy the remaining elements either from left or right array
        while (i < nLeft) {
            arr[k++] = arrLeft[i++];
        }

        while (j < nRight) {
            arr[k++] = arrRight[j++];
        }
    }
}
