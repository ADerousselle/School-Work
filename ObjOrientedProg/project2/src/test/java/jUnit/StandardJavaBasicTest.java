package jUnit;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Disabled;
import static org.junit.jupiter.api.Assertions.*;
import static java.util.Arrays.*;
import static java.time.Duration.*;
import java.util.ArrayList;
import java.util.LinkedList;

class StandardJavaBasicTest {
  
  @Test
  void testArraysEquals() {
	  
	  char[] expected = { 'J', 'u', 'p', 'i', 't', 'e', 'r' };
	  char[] actual = "Jupiter".toCharArray();
	  
	  assertArrayEquals(expected, actual, "Arrays should be equal");
  }//end test ArraysEqual
  
  @Disabled("Test disabled annotation")
  void testFail() {
	  // Test not completed
	  fail("FAIL - test not completed");
  }//end testFail
  
  @Test
  void testMultipleAssertion() {  
  
	  assertAll("heading",
      () -> assertEquals(4, 2*2, "4 is 2 times 2"),
      () -> assertEquals("java", "JAVA".toLowerCase())
	  );
  }//end 
  
  @Test
  void testEqualIterator() {
	  
	  Iterable<String> al = new ArrayList<>(asList("Java", "Junit", "Test"));
	  Iterable<String> ll = new LinkedList<>(asList("Java", "Junit", "Test"));
	  
	  assertIterableEquals(al, ll);
  }
  
  @Test
  void testNotEqual() {
	  
	  Integer value = 5; // result of an algorithm
	  
	  assertNotEquals(0, value, "The result cannot be 0");
  }
  
  @Test
  void testExpectedException() {
	  
	  assertThrows(NumberFormatException.class, () -> {
		  Integer.parseInt("One");});
  }
  
  @Test
  void testTimeout() {
	  
	// code that requires less then 2 seconds to execute, sleep is in miliSeconds 
    assertTimeout(ofSeconds(2),() -> {  Thread.sleep(1000);});

  }

}
