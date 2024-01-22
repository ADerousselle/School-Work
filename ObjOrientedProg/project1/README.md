# Programming project 1 (Sentiment Analysis)

## Objective
The educational objective of this assignment is to help students familiarize themselves with the following Java programming concepts:
1.	Input/Output to and from the terminal. 
2.	Storing data in a file and reading data from a file.
3.	Creating object-oriented classes and methods to handle data.
4.	Using data structures to store data in main memory (e.g., HashSet, ArrayList).
5.	Working with character strings.
6.	Using Javadoc comments and generating HTML documentation of the program.
7.	Using Java Exceptions to improve the error-handling capabilities of a program.

## Description
For this assignment, you will create a program to classify a set of movie reviews as positive or negative based on their sentiment. This process is known as [Sentiment Analysis](https://en.wikipedia.org/wiki/Sentiment_analysis). 

In this assignment, you are to write a Java package _project1_ that will classify a provided movie review as positive or negative by counting the number of positive and negative words in that review. Your class containing the _main()_ method should be named _SentimentAnalysisApp.java_. Design your main method to have multiple inputs as command line arguments: 
* Paths to two text files:  list of positive words (positive-words.txt) and list of negative words (negative-words.txt). 
* Paths to two folders:  the folder ‘pos’ contains the positive reviews and the folder ‘neg’ contains the negative reviews, both manually assigned by humans.  The reviews within each folder are given in separate .txt files, one review per file.  

_SentimentAnalysisApp_ should accept the following command line arguments. 
```java SentimentAnalysisApp <path_to_pos_words> <path_to_neg_words> <path_to pos_reviews_folder> <path_to_neg_reviews_folder>```

_SentimentAnalysisApp_ run example that assumes you have copied projecet1 directory as is, and made changes: 
```java SentimentAnalysisApp ./Data/positive-words.txt ./Data/negative-words.txt ./Data/Movie-reviews/pos ./Data/Movie-reviews/neg```

_SentimentAnalysisApp_ and the Java classes in the package _project1_ should automatically classify the .txt files in the folders and output the total count of how many were correctly classified, compared to the human ground truth. 

Steps needed: 
* The program loads the positive words and negative words and stores them in two separate lookup tables. The HashSet data structure can be used as a lookup table in Java as it provides a fast way to look if a word exists in it or not.
* The program iterates over the .txt files, and in each file, it counts the number of positive and negative words the review contains. If the review contains more positive than negative words, it is classified as positive and vice versa. If the same number of positive and negative words were found on the review, it counts as negative. 
* After each review has been classified, the program prints out in the command line the file name of the review, its real class, and its predicted class.
* The program should also print how many reviews were correctly classified and how many were misclassified – both total numbers or broken down per positive or negative review are accepted. 
* At the end, the program should print the accuracy per positive (i.e. Number of correctly classified positive reviews / Number of positive reviews ) and negative (i.e. Number of correctly classified negative reviews / Number of negative reviews ) classification and overall accuracy (Number of correctly classified reviews / Total number of reviews).

## Hints

1. Java provides the method [split()](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html), which allows us to split a String into multiple tokens by specifying a separator character. E.g.
```
String animals = "dog cat bear elephant giraffe";
String[] animalsArray = animals.split("\\s+");
```

2. Utilize Java [stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/package-summary.html) package to efficiently process the movie reviews. 

3. Utilize Java [regex](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/package-summary.html) package to remove special characters e.g. 
  1. Open .txt file, and read it into a String    
  2. Remove punctuation marks using regex \p{Punct} [https://docs.oracle.com/javase/17/docs/api/java/util/regex/Pattern.html](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html)  e.g. ```review = review.replaceAll(“\\p{Punct}”, “”);```  
  3. Convert everything to lowercase  
  4. Tokenize (split) review using white space as a separating character.  
  5. Count the number of positive and negative words.  
  6. Close .txt file.  


## Guidelines

* This assignment should be done individually.
* You may use any IDE (e.g., VSCode, BlueJ, Netbeans, Eclipse) or just an editor (e.g., Notepad+, Atom) and command line operations (javac, java) in Unix or Windows/DOS to develop your program.
* You don't need to create any GUI for this assignment. Command line operations are enough.
* Use a standard Java coding style to improve your program’s visual appearance and make it more readable, e.g. Google Java style guide: [https://google.github.io/styleguide/javaguide.html](https://google.github.io/styleguide/javaguide.html) 

## Submit

* A Git repository will be used to submit this assignment at [https://git.txstate.edu/CS3354](https://git.txstate.edu/CS3354). Add your files to the repository named after your netID.  

* Do NOT include executable .class or .jar files in your submission. Only .java files.
