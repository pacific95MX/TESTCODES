import java.util.Scanner;
class Calculator
{
  public static void main(String args[])
  {
    String yn;
    do
   {
      Scanner s =new Scanner(System.in);
    System.out.println("Enter first number");
    double a = s.nextDouble();
    System.out.println("Enter second number");
    double b = s.nextDouble();
    System.out.println("Select type of Operation (+, -, *, /)");
    String str = s.next();
    
    double result;
    
    switch(str)
    {
      case "+": result=a+b;
         System.out.println("Addition is : "+result);
         break;
      case "-": result=a-b;
         System.out.println("Substraction is : "+result);
        break;
      case "*": result=a*b;
        System.out.println("Multiplication is : "+result);
        break;
      case "/": result=a/b;
        System.out.println("Division is : "+result);
        break;
      default : System.out.println("INVALID SYMBOL");
        break;
    }
     System.out.println("Do u want to continue(Press y or Y for yes and n or N for no)");
      yn= s.next();
   }while(yn.equals("y") || yn.equals("Y"));
  }
}
        
        
    
  
