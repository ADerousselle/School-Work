package jUnit;

import java.io.*;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.*;


class IOUnitTest {
	
	@BeforeEach
	void createEnvironMent() {
	  
	  System.out.println("Set Up Environment");
	 
	}
	
	@AfterEach
	void clearEnvironMent() {
	  
	  System.out.println("Cleared Environment");
	} 
	
	@Test
	void testRead() throws IOException {
		
		//IOUnit class is tested       
	    IOUnit unit = new IOUnit();
	  
		byte[] data = "123,456,789,123,456,789".getBytes();
		InputStream input = new ByteArrayInputStream(data);
		unit.read(input);
		
		assertEquals("123", unit.tokens.get(0));
		assertEquals("456", unit.tokens.get(1));
		assertEquals("789", unit.tokens.get(2));
		assertEquals("123", unit.tokens.get(3));
		assertEquals("456", unit.tokens.get(4));
		//assertEquals("789", unit.tokens.get(5));
	}
	
	@Test
	void testWrite() throws IOException {
		
		//IOUnit class is tested       
	    IOUnit unit = new IOUnit();
		
		unit.tokens.add("one");
		unit.tokens.add("two");
		unit.tokens.add("three");
		
		ByteArrayOutputStream output = new ByteArrayOutputStream();
        unit.write(output);
		String string = new String(output.toByteArray());
		assertEquals("one,two,three", string);
		
	}//end testWrite

}
