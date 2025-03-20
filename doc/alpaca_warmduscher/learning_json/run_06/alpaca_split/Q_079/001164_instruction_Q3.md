For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/UUIDUtils.java' with name 'UUIDUtils.java' where below a part of it is displayed...
```java
public static UUID fromShortText(String shortTextUUID) {
    if (StringUtils.isEmpty(shortTextUUID)) {
        return null;
    }
    byte[] bytes = Base58BitcoinFlavor.decode(shortTextUUID);
    ByteBuffer bb = ByteBuffer.wrap(bytes);
    return new UUID(bb.getLong(), bb.getLong());
}
```
What does this method do and how does it reverse the conversion performed by `toShortText`? Explain the process step-by-step.