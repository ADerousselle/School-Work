package jUnit;

import org.junit.jupiter.api.Test;
import static org.hamcrest.MatcherAssert.assertThat; 
import static org.hamcrest.Matchers.*;

public class BiscuitHamcrestTest {

  @Test 
  public void testEquals() { 
    Biscuit theBiscuit = new Biscuit("Ginger"); 
    Biscuit myBiscuit = new Biscuit("Ginger"); 
    assertThat(theBiscuit, equalTo(myBiscuit)); 

  } 

  @Test 
  public void testMethods() { 
    Biscuit theBiscuit = new Biscuit("Ginger"); 
    assertThat(theBiscuit.getChocolateChipCount(), equalTo(10)); 
    assertThat(theBiscuit.getHazelnutCount(), equalTo(3));
  } 
  
} 