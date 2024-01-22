package jUnit;

import org.junit.jupiter.api.Test;
import static org.hamcrest.MatcherAssert.assertThat; 
import static org.hamcrest.Matchers.*;
import static jUnit.IsNotANumber.notANumber;


class MyHamcrestTest {
    
    @Test
    void testSquareRootOfMinusOneIsNotANumber() { 
        double result = My.sqrt(-1.0);
        assertThat(result, is(notANumber())); 
    }
}
