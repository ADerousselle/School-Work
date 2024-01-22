package parallelsort;

import java.util.*;
import java.util.concurrent.ForkJoinPool;

/**
 * Class that will invoke the ParallelMergeTask
 */
public class ParallelMergeSort{

    /**
     *  Original sort call that calls the overloaded sort.
     * @param a the array that will be sorted
     * @param comp Comparator to compare type E
     * @param <E> the type of the element that will be sorted
     */
    public static <E extends Comparable<? super E>> void sort(E[] a, Comparator<? super E> comp) {
        sort(a, 0, a.length);
    }

    /**
     * Sort call that will create the threadpool and invoke the ParallelMergeTask
     * @param a the array that will be sorted
     * @param start beginning index of the portion to be sorted
     * @param end last index of portion to be sorted
     * @param <E> the type of the element that will be sorted
     */
    public static <E extends Comparable<? super E>> void sort(E[] a, int start, int end) {
      
        // add code here 
    }

}