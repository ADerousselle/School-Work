package jUnit;

class Calculator{
	
	public Calculator(){
		this.name = "Calculator";
	}
	
	public int multiply (int x, int y) {
		return x*y;
	}//end multiply
	
	public String concatenate(String one, String two){
		return one + two;
	}
	
	public boolean greater(int x, int y){
		return (x > y);
	}
	
	public void setName(String aName){
		this.name = aName; 
	}
	
	public String getName(){
		return this.name; 
	}
	
	private String name;  

}//end class