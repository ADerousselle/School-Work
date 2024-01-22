# [HW9](https://canvas.txstate.edu/courses/1993332/assignments/27480114)

* This assignment will help students familiarize with parallel impelmentation and java logging. 
* Refer to [zyBook](https://learn.zybooks.com/zybook/TXSTATECS3354TesicFall2022) Sections 18 and 19 for more details. 
  * [sort](sort) package starting point for logging and design pattern submission
  * [parallelsort](parallelsort) package starting point for parallelization submission 
  * [forkjoin](https://git.txstate.edu/CS3354/2022Fall/tree/main/Examples/moreJava/src/main/java/forkjoin) package as an example of forkjoin implementation

# HW 9 Problem Description

MergeSort is a sorting algorithm that can be easily parallelized due its divide-and-conquer nature. On CPUs with multiple cores, multiple threads can speed up the sorting time, by splitting the work. Provided source code in extracredit/sortanimation sorts a set of numbers using the top-down MergeSort  algorithm. In the given implementation, the program uses a single thread to sort the whole input.  MergeSort is a divide-and-conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

##  parallelsort 3 pt 

Parallelize MergeSort using ForkJoin paradigm in **parallelSort** package.  
* Use provided code in parallelSort as a starting point for this task.  
  * add code to  public static <E extends Comparable<? super E>> void sort(E[] a, int start, int end) method in ParalleMergeSort.java
  * add code to compute() method in ParalleMergeTask.java
* ParallelMergeSort class makes use of multiple threads to perform the sorting task - use forkjoin.part4 in concurrency folder as a guiding example. 
  * it  should implements recursive method to sort, and fit ForkJoin paradigm. 
* To make sure that your parallelized MergeSort works correctly, use the method isSorted, of the given class SortTester which takes an array as an input argument and returns true or false, depending on if the input array is sorted or not.
* You will get full grade if you implement console or animation interface, it is your choice 
  * You can use the existing **sort** package for the interface to integrate. 
  
### The following is a pseudocode of the mergeSort method in MergeSorter class: 

```
mergeSort(arr[], l,  r)
if r > l
    Find the middle point to divide the array into two halves:  
        middle m = (l+r)/2
    Call mergeSort for first half:   
        Call mergeSort(arr, l, m)
    Call mergeSort for second half:
        Call mergeSort(arr, m+1, r)
    Merge the two halves sorted in step 2 and 3:
        Call merge(arr, l, m, r)	
```

 
The pseudocode above can be modified to allow mergeSort(arr, l, m) and mergeSort(arr, m+1, r) to run in parallel -> create new parallelMergeSort method in the new ParallelMergeSort class, e.g. 

```
parallelMergeSort(arr[], 1, r):
   if r>1
         middle m = (l+r)/2
         fork subtask to parallelMergeSort(arr, l, m)
         fork subtask to parallelMergeSort(arr, l, m)
        join all subtasks spawned 
        return combined results
   else: 
        merge(arr, l, m, r)
```

## logging 2 pt  

Add logging capability to **sort** and **parallelsort** packages using native java logging framework.  
(https://docs.oracle.com/en/java/javase/11/docs/api/java.logging/java/util/logging/package-summary.html).
Write the output to the file using XML formatter with Level.INFO set, and to the console using simple formatter with Level: WARNING set 
Add logging to all *.java files in the package 

## Submission 
* Use Javadoc is for every public class, and every public or protected member of such a class. Other classes and members may still have Javadoc as needed. Whenever an implementation comment would be used to define the overall purpose or behavior of a class, method or field, that comment is written as Javadoc instead. (It's more uniform, and more tool-friendly.)  
**There is no single correct solution.** 
* All solutions that are reasonable, well documented and follow the standards that we saw in class, will be accepted. 
* If you are unsure about certain decisions and need to make assumptions, please state your assumptions clearly in your solution document.

1. copy ```HW9``` folder from [2022Fall.git](https://git.txstate.edu/CS3354/2022Fall/tree/main/Projects/HW9) to git.xtstate.edu/CS3354/**NetID**.git repo
	```
	>>cd 2020Fall
	>>git pull
	>>cd ..
	>>cd NetID
	git pull
	```
* copy HW9 folder from  Projects/ to **NetID**/

2. navigate into HW9, right-click and select open with VSCode or your editor of choice
3. edit files in [sort](sort) folder for logging (Task 1) 
   * add logger and logging messages as described below to existing .java files 
   * check in changes often to  **NetID** repository 
   ``` 
	>> git add *
	>> git commit -m "update comment "
	>> gitk
	```
   * compile and run 
4. edit files in [parallelsort](parallelsort) folder for parallel processing (Task 2)
   * add methods to parallelsort package to make it work 
   * Compile and run 
	```
	>>javac -d bin –cp ".;target\;lib\*"  src\main\java\parallelsort\*.java
	>>java -cp ".;target\;lib\*" parallelsort.SortMain
	```
	* check-in changes often 
	``` 
	>> git add *
	>> git commit -m "update comment "
	>> gitk
	```
gitk will show you the status, close it to continue
```
git push origin:<NetID>
```

5. Repeat step 2, 3 and 4 often to save your work until done. 
  * it allows you to re-trace your steps
  * do not forget to list **ALL** team members under @author javadoc tag






