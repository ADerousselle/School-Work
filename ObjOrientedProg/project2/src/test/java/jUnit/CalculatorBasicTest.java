package jUnit;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorBasicTest {

  @BeforeEach
  public void setUp() {
    this.testCalc = new Calculator();
    System.out.println("Setup method test environment.");
  }

  @AfterEach
  public void tearDown() {
    this.testCalc = null;
    System.out.println("Cleared method test environment");
  }

  @Test
  public void testMultiply() {

    // Tests
    assertEquals(0, testCalc.multiply(10, 0), "10 x 0 must be 0");
    assertEquals(0, testCalc.multiply(0, 10), "0 x 10 must be 0");

    Integer x = 5;
    Integer y = 4;
    assertEquals(20, testCalc.multiply(x, y), x + " x " + y + " must be 20");

  }// end testMultiply

  @Test
  public void testConcatenate() {

    String result = testCalc.concatenate("one", "two");
    assertEquals("onetwo", result);

  }// end testConcatenate

  @Test
  public void testAssertingConditions() {

    assertTrue(testCalc.greater(5, 4), "5 is greater the 4");

  }

  @Test
  public void testGetTheSameObject() {

    assertSame(testCalc, testCalc);
    assertNotSame(testCalc, "Calculator");

  }

  @Test
  public void testAssertingNotNull() {

    assertNotNull(testCalc, "The dog should not be null");

  }

  @Test
  public void whenAssertingNull_thenTrue() {

    this.testCalc = null;
    assertNull(testCalc, "The testCalc should be null");

  }

  public Calculator testCalc;

}
