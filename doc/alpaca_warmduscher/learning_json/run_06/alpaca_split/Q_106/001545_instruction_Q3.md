For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/test/java/com/x8ing/thsensor/thserver/utils/UUIDUtilsTest.java' with name 'UUIDUtilsTest.java' where below a part of it is displayed...
```java
@Test
public void testPerformance() {
    // warm-up
    for (int i = 0; i < 10000; i++) {
        UUIDUtils.generateShortTextUUID();
    }
    long t0 = System.currentTimeMillis();
    final int LOOP = 100000;
    for (int i = 0; i < LOOP; i++) {
        String uuid = UUIDUtils.generateShortTextUUID();
        if ("trick_out_optimizer".equals(uuid)) {
            System.out.println("won't happen but the JIT will not know");
        }
    }
    long dt = System.currentTimeMillis() - t0;
    System.out.println("time for " + LOOP + " loops was " + dt + " ms. " + (1.0 * dt / LOOP) + " ms per one UUID");
    assertTrue( dt < 500,"Generating the UUID took too long. dt=" + dt);
}
```
What is the purpose of the "warm-up" loop at the beginning of the `testPerformance` method, and why is the `if` statement inside the main loop included?