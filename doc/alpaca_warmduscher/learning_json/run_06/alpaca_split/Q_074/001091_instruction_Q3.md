For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/Base58BitcoinFlavor.java' with name 'Base58BitcoinFlavor.java' where below a part of it is displayed... 
```java
 public static String encode(byte[] input) {
       if (input.length == 0) {
           return "";
       }
       // Count leading zeros.
       int zeros = 0;
       while (zeros < input.length && input[zeros] == 0) {
           ++zeros;
       }
       // Convert base-256 digits to base-58 digits (plus conversion to ASCII characters)
       input = Arrays.copyOf(input, input.length); // since we modify it in-place
       char[] encoded = new char[input.length * 2]; // upper bound
       int outputStart = encoded.length;
```
Explain the purpose of the `Arrays.copyOf(input, input.length)` line in the `encode` method. Why is it necessary to create a copy of the input array before modifying it in-place?