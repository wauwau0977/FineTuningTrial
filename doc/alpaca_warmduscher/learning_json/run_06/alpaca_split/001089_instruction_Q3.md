For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/Base58BitcoinFlavor.java' with name 'Base58BitcoinFlavor.java' where below a part of it is displayed... 
```java
   private static byte divmod(byte[] number, int firstDigit, int base, int divisor) {
       // this is just long division which accounts for the base of the input digits
       int remainder = 0;
       for (int i = firstDigit; i < number.length; i++) {
           int digit = (int) number[i] & 0xFF;
           int temp = remainder * base + digit;
           number[i] = (byte) (temp / divisor);
           remainder = temp % divisor;
       }
       return (byte) remainder;
   }
```
What is the purpose of the `& 0xFF` operation performed on `number[i]` within the `divmod` method, and why is it necessary? Explain its role in the context of byte array manipulation.