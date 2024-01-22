package jUnit;

import java.lang.StringBuilder;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;


class IOUnit{

  protected List<String> tokens = new ArrayList<String>();
  
  public void read(InputStream input) throws IOException {
	  
	  StringBuilder builder = new StringBuilder();
	  int data = input.read();
	  
	  while(data != -1){
		  if(((char)data) != ','){
			  builder.append((char) data);
		  } else {
			  
			  this.tokens.add(builder.toString().trim());
			  builder.delete(0, builder.length());
		  }//end else 
		  
		  data = input.read();
	    }//end while
	}//end read
	
	public void write(OutputStream output) throws IOException {
		
		for(int i=0; i<tokens.size(); i++){
			
			if(i>0){
				output.write(',');
			}
			output.write(tokens.get(i).getBytes());
		}//end for
	}//end write 

	
}//end IOUnit
