package jUnit;

import org.hamcrest.Description; 
import org.hamcrest.Matcher; 
import org.hamcrest.TypeSafeMatcher;

public class IsNotANumber extends TypeSafeMatcher{

  @Override 
  protected boolean matchesSafely(Object obj) { 
    Double d = null;
    if (obj instanceof Double) {
        d = (Double) obj;
    }
    return d.isNaN(); 
  }

  public void describeTo(Description description) { 
    description.appendText("not a number"); 
  }

  public static Matcher notANumber() { 
    return new IsNotANumber(); 
  }

} 

