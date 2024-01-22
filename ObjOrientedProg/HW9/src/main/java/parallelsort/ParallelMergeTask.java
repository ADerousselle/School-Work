package parallelsort;

import java.util.Arrays;
import java.util.concurrent.RecursiveAction;

/**
 * This class represents the work that is done to sort the array
 * @param <E> the type of the element that will be sorted
 */
class ParallelMergeTask<E extends Comparable<? super E>> extends RecursiveAction {
    /**
     * THRESHOLD is the max number of elements before using Arrays native sort.
     * In case anyone decides to through a massive array at this program by editing main
     */
    private static final int THRESHOLD = 500000;

    private final E[] a;
    private final int start;
    private final int end;

    /**
     * The constructor for ParallelMergeTask, assigns values to final variables
     * @param a the array that will be sorted
     * @param start beginning index of the portion to be sorted
     * @param end last index of portion to be sorted
     */
    ParallelMergeTask(E[] a, int start, int end) {
        this.a = a;
        this.start = start;
        this.end = end;
    }

    /**
     * Function does an initial check, if the length of the portion to be sorted is less than THRESHOLD then we use
     * arrays sorting method, else we fork the tasks and join them.
     *
     */
    @Override
    protected void compute() {
        if(a.length < 2)
            {return;}
        else
            int mid;
            mid = a.length / 2;
            E[] aLeft;
            aLeft = new E[mid];
            System.arrayCopy(a, 0, aLeft, 0, mid);

            E[] aRight;
            aRight = new E[a.length - mid];
            System.arrayCopy(a, mid, aRight, 0, (a.length - mid));

            invokeAll( new ParallelMergeTask(aLeft, 0, mid), new ParallelMergeTask(aRight, mid, (a.length - mid)));
            merge(0, mid, a.length);
        }

    /**
     *  Merges two adjacent subranges of an array
     *
     * @param lo beginning index of the portion to be sorted
     * @param middle middle index between the two portions to be sorted
     * @param hi last index of portion to be sorted
     */
    private void merge( int lo, int middle, int hi ) {
        Object[] newArray = new Object[hi - lo];

        int index = 0;
        int i1 = lo;
        int i2 = middle;

        while ( i1 < middle && i2 < hi ) {
            E left = a[i1];
            E right = a[i2];
            if ( left.compareTo(right) <= 0 ) {
                newArray[index] = a[i1];
                i1++;
            } else {
                newArray[index] = a[i2];
                i2++;
            }
            index++;
        }

        while( i1 < middle ){
            newArray[index] = a[i1];
            index++;
            i1++;
        }
        while( i2 < hi){
            newArray[index] = a[i2];
            index++;
            i2++;
        }
        System.arraycopy(newArray, 0, a, lo, newArray.length);
    }
}
