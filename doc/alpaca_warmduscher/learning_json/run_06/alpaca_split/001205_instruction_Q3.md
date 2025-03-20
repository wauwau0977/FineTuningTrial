For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/Utils.java' with name 'Utils.java' where below a part of it is displayed... 
```java
public static <T> double getMedian(Collection<T> entries, ToDoubleFunction<T> valueSupplier, int limit) {
    assert entries != null : "Entries must not be null";
    assert valueSupplier != null : "Supplier must not be null";
    Median median = new Median();
    // ... rest of the code
}
```
What is the purpose of the assertions at the beginning of this method? Explain why these checks are important in terms of code robustness and preventing unexpected behavior.