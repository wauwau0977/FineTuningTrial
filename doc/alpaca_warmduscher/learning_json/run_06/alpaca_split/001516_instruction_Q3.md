For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/test/java/com/x8ing/thsensor/thserver/utils/Base58BitcoinFlavorTest.java' with name 'Base58BitcoinFlavorTest.java' where below a part of it is displayed...
```java
   @Test
   public void checkPerformance() {
       final int loops = 1000;
       long t0 = System.currentTimeMillis();
       for (int i = 0; i < loops; i++) {
           byte[] randomBytes = new byte[64];
           new Random().nextBytes(randomBytes);
           String encode = Base58BitcoinFlavor.encode(randomBytes);
           byte[] decodedBytes = Base58BitcoinFlavor.decode(encode);
           assertEquals(Arrays.toString(randomBytes), Arrays.toString(decodedBytes));
       }
       long dt = System.currentTimeMillis() - t0;
       System.out.println("Test iteration for " + loops + " took " + dt + " ms. 1 encoding/decoding in " + (1.0 * dt / loops) + " ms.");
   }
```
What does the `checkPerformance` test method aim to evaluate, and what metric is used to quantify the performance?