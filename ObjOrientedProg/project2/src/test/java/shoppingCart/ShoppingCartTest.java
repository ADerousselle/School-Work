package shoppingCart;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.ByteArrayOutputStream;
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
public class ShoppingCartTest {

    private ShoppingCart cart1;
    private ShoppingCart cart2;
    private ItemToPurchase item1;
    private ItemToPurchase item2;
    private ItemToPurchase item3;
    ByteArrayOutputStream baos;
    PrintStream ps;
    PrintStream old;
    String separator;
    
    @BeforeAll
    public void initializer()
    {
        cart1 = new ShoppingCart();
        cart2 = new ShoppingCart("Abby", "November 27, 2022");
        item1 = new ItemToPurchase("Water", "12oz", 1, 1);
        item2 = new ItemToPurchase("Cookies", "12 pack", 5, 4);
        item3 = new ItemToPurchase("Juice", "1 gallon", 3, 3);
        cart2.addItem(item2);
        baos = new ByteArrayOutputStream();
        ps = new PrintStream(baos);
        old = System.out;
        System.setOut(new PrintStream(baos));
        separator = System.getProperty("line.separator");
    }

    //Makes sure null ShoppingCart object can be created.
    @Test
    @Order(1)
    public void testNullShoppingCartConstructor()
    {
        String result = cart1.getCustomerName() + ", " + cart1.getDate();

        assertEquals("none, January 1, 2016", result, "Test - Create null ShoppingCart.");

    }

    //Makes sure custom ShoppingCart object can be created.
    @Test
    @Order(2)
    public void testCustomShoppingCartConstructor()
    {
        String result = cart2.getCustomerName() + ", " + cart2.getDate();

        assertEquals("Abby, November 27, 2022", result, "Test - Create custom ShoppingCart.");

    }

    //Makes sure ShoppingCart object can add and remove items.
    @Test
    @Order(6)
    public void testCanAddItems()
    {
        cart2.addItem(item1);
        cart2.addItem(item3);
        cart2.removeItem("Cookies");
        int result = cart2.getNumItemsInCart();
        
        assertEquals(4, result, "Test - adding and removing items.");
    }

    //Makes sure ShoppingCart object cannot remove items not in the cart.
    @Test
    @Order(3)
    public void testCannotRemoveNonexistantObject()
    {
        cart1.removeItem("Juice");
        String result = baos.toString();
        String expected = "Item not found in cart. Nothing removed.";
        result = result.trim();
        baos.reset();

        assertEquals(expected, result, "Test - Cannot remove an item not in the cart.");
    }

    //Makes sure ShoppingCart object can modify the description, price and quantity of an item.
    @Test
    @Order(5)
    public void testCanModifyExistantItems()
    {
        item2.setQuantity(6);
        cart2.modifyItem(item2);
        int result = cart2.getNumItemsInCart();
        
        assertEquals(6, result, "Test - Can modify items in the cart.");
    }

    //Makes sure ShoppingCart object cannot modify object not in cart.
    @Test
    @Order(7)  
    public void testCannotModifyNonexistantItem()
    {
        cart1.modifyItem(item2);
        String result = baos.toString();
        result = result.trim();
        String expected = "Item not found in cart. Nothing modified.";
        baos.reset();

        assertEquals(expected, result, "Test - Cannot modify items not in the cart.");
    }

    //Makes sure ShoppingCart object gets the correct quantity.
    @Test
    @Order(4)
    public void testCorrectTotalCartQuantity()
    {
        int result = cart2.getNumItemsInCart();

        assertEquals(4, result, "Test - Produce correct total quantity of items in the cart.");
    }

    //Makes sure ShoppingCart object gets correct cart cost.
    @Test
    @Order(8)
    public void testCorrectTotalCartCost()
    {
        int expCost = (item1.getPrice() * item1.getQuantity()) + (item3.getPrice() * item3.getQuantity());
        int result = cart2.getCostOfCart();

        assertEquals(expCost, result, "Test - Can calculate correct total cost of all items in the cart.");

    }

    //Makes sure ShoppingCart object can print the correct total output.
    @Test
    @Order(9)
    public void testPrintsCorrectTotalFullCartCost()
    {
        String expOut = "Abby's Shopping Cart - November 27, 2022" + separator + "Number of Items: 4" + separator + separator 
                        + "Water 1 @ $1 = $1" + separator + "Juice 3 @ $3 = $9" + separator + separator + "Total: $10";
        cart2.printTotal();
        String result = baos.toString();
        result = result.trim();
        
        baos.reset();

        assertEquals(expOut, result, "Test - Correctly print total full-cart cost ouput.");
    }
 
    //Makes sure empty ShoppingCart object prints correct total output.
    @Test
    @Order(10)
    public void testPrintsCorrectTotalEmptyCartCost()
    {
        String expOut = "none's Shopping Cart - January 1, 2016" + separator + "Number of Items: 0" + separator + separator 
                        + "SHOPPING CART IS EMPTY" + separator + separator + "Total: $0";
        cart1.printTotal();
        String result = baos.toString();
        result = result.trim();
        baos.reset();

        assertEquals(expOut, result, "Test - Correctly print total empty-cart cost output.");
    }

    //Makes sure ShoppingCart object can print all descriptions output.
    @Test
    @Order(11)
    public void testPrintsCorrectFullCartItemsDescriptions()
    {
        String expOut = "Abby's Shopping Cart - November 27, 2022" + separator + separator + "Item Descriptions" + separator 
                        + "Water: 12oz" + separator + "Juice: 1 gallon" + separator;
        cart2.printDescriptions();
        String result = baos.toString();
        result = result.toString();
        baos.reset();

        assertEquals(expOut, result, "Test - Correctly print full-cart item descriptions.");
    }

    //Makes sure empty ShoppingCart object prints correct description output.
    @Test
    @Order(12)
    public void testPrintsCorrectEmptyCartItemsDescriptions()
    {
        System.setOut(ps);
        String expOut = "none's Shopping Cart - January 1, 2016" + separator + separator + "Item Descriptions" + separator 
                        + "SHOPPING CART IS EMPTY";
        cart1.printDescriptions();
        String result = baos.toString();
        result = result.trim();

        assertEquals(expOut, result, "Test - Correctly print empty-cart item descriptions.");
    }    

    @AfterAll
    public void resetSystemOut()
    {System.setOut(old);}
}
