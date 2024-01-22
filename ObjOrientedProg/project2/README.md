# Project 2 JUnit5

Due date on Canvas

**Goal:** The goal of the project is to help students understand the use of JUnit to test Java code.  You will create a set of unit tests, to test the behavior of the code in 2022Fall/Projects -> project2

**Unit testing** is used to test the behavior of the code (or parts of the code) written, without having to run the whole program.

## Tasks:

Your task is to create 20 JUnit tests in total to test the methods of shoppingCart/*.java classes in src/main/java/project2

1.	Implement the JUnit tests to test  
    *  - ShoppingCart.java (JUnit tests)
	*  - ItemToPurchase.java (Hamcrest tests)

Try to be creative by coming up with test cases that can test as many different situations as possible.

Start with testing the behavior of the class/methods under normal operation scenarios.  
* Mock objects can be created either in the same test method or before any test methods are run, using the @BeforeAll or @BeforeEach annotation. 

## Code steps 

1. Copy project2 folder from 2022Fall/Projects, to **ID** folder 
  * ID stands for NetID
 
2. Open the folder with IDE of choice 
  * Maven-IDE integration [link](https://maven.apache.org/ide.html) 
  * Maven-VS Code integration [link](https://code.visualstudio.com/docs/java/java-build)
  * Build a project. Run tests. 
3. (Optional) install Java testing extension for specific IDE  
  * [Visual Studio Code JUnit integration](https://code.visualstudio.com/docs/java/java-testing)
  * Run tests
4. Add test methods to ShoppingCartTest.java and ItemToPurchaseHamcrestTest.java (under src/test/java/shoppingCart). Test changes and make sure the tests are passing. All tests need to pass and need to be non-trivial. You will get 0 credit for trivial or failed tests 

* Option 1. Run Maven project once (package) it should coimpile and run all tests and install all extensions. Run new tests in VS Code using Run Tests button in the code.

* Option 2: Compile and run JUnit5 testing, within your IDE or download junit-platform-console-standalone-1.9.1.jar from [here]( https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/1.9.1/) and place it in lib folder inside **ID/project2** 

```
cd project2
javac -d bin –cp ".;bin\;lib\*"  src\main\java\shoppingCart\*.java src\test\java\shoppingCart\*.java
java -cp ".;bin\;lib\*" org.junit.platform.console.ConsoleLauncher --exclude-engine=junit-vintage --include-engine=junit-jupiter --fail-if-no-tests --scan-classpath
```
**Your code will be tested against project2/src/main/java/shoppingCart code enforcing no source code modifications**

5. Commit and submit the work  


## How to use git repositories for project2 submission

0. NetID is **ID** in the text below 

1. 
```
cd 2022Fall/
git pull
```

2. Move to your working directory
```
cd ..
cd ID
git pull
cp ../Projects/project2
```

3. Make and save changes using IDE or text editor of choice 

* add test methods to ShoppingCartTest.java and ItemToPurchaseHamcrestTest.java (under src/test/java/shoppingCart)

Repeat once:
```

git add project2/src/main/java/shoppingCart/*.java
git add project2/src/test/java/shoppingCart/*.java
git commit -m "project2 baseline added"
git push origin:<ID>
```

4. Test all new test methods and make sure they compile and run, as listed above. 

5. Check in changes often to  **ID** repository 
-> make sure you are in **ID** folder for git commandline:

Repeat multiple times: 
```
git add project2/src/test/java/shoppingCart/*.java
git commit -m "project2 tests ABCD added"
gitk
```
gitk will show you the status, close it to continue
```
git push origin:<ID>
```

5. Repeat step 4 and 5 often to save your work until done. 

6. Done! 
