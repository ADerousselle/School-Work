package shoppingCart;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.MethodOrderer;
import org.junit.jupiter.api.Order;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.api.TestMethodOrder;
import org.junit.jupiter.api.TestInstance.Lifecycle;

@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
@TestInstance(Lifecycle.PER_CLASS)
public class ItemToPurchaseHamcrestTest {

    private static ItemToPurchase item1;
    private static ItemToPurchase item2;
    static ByteArrayOutputStream  baos;
    PrintStream ps;
    PrintStream old;
    
    @BeforeAll
    public void initializer()
    {
        item1 = new ItemToPurchase();
        item2 = new ItemToPurchase("Water", "12oz", 1, 2);
        baos = new ByteArrayOutputStream();
        ps = new PrintStream(baos);
        old = System.out;
        System.setOut(new PrintStream(baos));
    }

    //Makes sure null ItemToPurchase object can be created.
    @Test
    @Order(1)
    public void testNullItemToPurchaseConstructor()
    {
        String result = item1.getName() + ", " + item1.getDescription() + ", " + item1.getPrice() + ", " + item1.getQuantity();

        assertEquals("none, none, 0, 0", result, "Test - Create null ItemToPurchase.");
    }

    //Makes sure customer ItemToPurchase object can be created.
    @Test
    @Order(2)
    public void testCustomItemToPurchaseConstructor()
    {
        String result = item2.getName() + ", " + item2.getDescription() + ", " + item2.getPrice() + ", " + item2.getQuantity();

        assertEquals("Water, 12oz, 1, 2", result, "Test - Create custom ItemToPurchase.");
    } 

    //Makes sure ItemToPurchase object name can be changed and retrieved correctly.
    @Test
    @Order(3)
    public void testSetandGetItemName()
    {
        item1.setName("Cookies");
        item2.setName("Juice");
        String result = (item1.getName() + ", " + item2.getName());

        assertEquals("Cookies, Juice", result, "Test - Can set and get ItemToPurchase name.");
    }
    
    //Makes sure ItemToPurchase object price can be changed and retrieved correctly.
    @Test
    @Order(4)
    public void testSetandGetItemPrice()
    {
        item1.setPrice(5);
        item2.setPrice(3);
        String result = (item1.getPrice() + ", " + item2.getPrice());
    
        assertEquals("5, 3", result, "Test - Can set and get ItemToPurchase price.");
    }

    //Makes sure ItemToPurchase object quantity can be changed and retrieved correctly.
    @Test
    @Order(5)
    public void testSetandGetItemQuantity()
    {
        item1.setQuantity(4);
        item2.setQuantity(3);
        String result = (item1.getQuantity() + ", " + item2.getQuantity());
    
        assertEquals("4, 3", result, "Test - Can set and get ItemToPurchase quantity.");
    }

    //Makes sure ItemToPurchase object description can be changed and retrieved correctly.
    @Test
    @Order(6)
    public void testSetandGetItemDescription()
    {
        item1.setDescription("12 pack");
        item2.setDescription("1 gallon");
        String result = (item1.getDescription() + ", " + item2.getDescription());
        
        assertEquals("12 pack, 1 gallon", result, "Test - Can set and get ItemToPurchase description.");
    }

    //Makes sure ItemToPurchase object cost can be printed correctly.
    @Test
    @Order(7)
    public void testCorrectItemCostOutput() throws IOException
    {
        String expected1 = "Cookies 4 @ $5 = $20";
        item1.printItemCost();
        String result1 = baos.toString();
        result1 = result1.trim();
        baos.reset();
        
       
        String expected2 = "Juice 3 @ $3 = $9";
        item2.printItemCost();
        String result2 = baos.toString();
        result2 = result2.trim();
        baos.reset();

        boolean result3 = expected1.equals(result1);
        boolean result4 = expected2.equals(result2);

       assertTrue(result3 && result4, "Test - Can calculate the correct ItemToPurchase total cost.");
    }

    //Makes sure ItemToPurchase object description can be printed correctly.
    @Test
    @Order(8)
    public void testCorrectItemDescriptionOutput()
    {
        
        String expDesc1 = "Cookies: 12 pack";
        item1.printItemDescription();
        String result1 = baos.toString();
        result1 = result1.trim();
        
        baos.reset();

        String expDesc2 = "Juice: 1 gallon";
        item2.printItemDescription();
        String result2 = baos.toString();
        result2 = result2.trim();

        boolean result3 = result1.equals(expDesc1);
        boolean result4 = result2.equals(expDesc2);
        
       assertTrue((result3 && result4), "Test - Can print the correct ItemToPurchase description.");
    }

    @AfterAll
    public void resetSystemOut()
    {System.setOut(old);}
}
