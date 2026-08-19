class DynamicArray {
    int [] array;
    int endPointer;
    public DynamicArray(int capacity) {
        array = new int [capacity];
        endPointer = 0;
    }

    public int get(int i) {
        return array[i];
    }

    public void set(int i, int n) {
        array[i] = n;
        if (i > endPointer)
            endPointer = i;
    }

    public void pushback(int n) {
        if (getCapacity() <= endPointer)
            resize();
        array[endPointer] = n;
        endPointer++;
    }

    public int popback() {
        int endValue = array[endPointer-1];
        array[--endPointer] = 0;
        return endValue;
    }

    private void resize() {
        int [] copyArray = new int [array.length * 2];
        for (int i = 0; i < array.length; i++){
            copyArray[i] = array[i];
        }
        array = copyArray;
    }

    public int getSize() {
        return endPointer;
    }

    public int getCapacity() {
        return array.length;
    }
}
