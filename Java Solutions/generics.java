public class generics {

    public static <Type> void printArray(Type[] receivedArray){
        for (Type elem : receivedArray)
            System.out.println(elem);
    }
    public static void main( String args[] ) {
        Integer[] intArray = { 1, 2, 3 };
        String[] stringArray = {"Hello", "World"};        
        printArray(intArray);
        printArray(stringArray);
    }
}