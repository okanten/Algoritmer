
public static void selectionSort(int a[]) {
    int n = a.length, tmp = 0;

    for (int i = 0; i < n - 1; i++) {
        int min = i;

        for (int j = i + 1; j < n; j++) {
            if a([j] < a[min])
                min = j

        }
        tmp = a[min];
        a[min] = a[i];
        a[i] = tmp;
    }


}
