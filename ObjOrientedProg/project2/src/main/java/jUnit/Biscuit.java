package jUnit;

public class Biscuit {

   /**
     Constructs a Student object that saves the name of a person.
     @param aName the name of the person.
   */
   public Biscuit(String aName){
    name = aName;
   } 

   public int getChocolateChipCount(){
       return 10;
   }

   public int getHazelnutCount(){
    return 3;
   }

   public String getName(){
    return this.name;
   }

   @Override
   public boolean equals(Object obj){
       if (obj instanceof Biscuit) {
        Biscuit freshB = (Biscuit) obj;
        return this.getName().equals(freshB.getName());
       }
       return false;
   }
    
    private String name;
}
