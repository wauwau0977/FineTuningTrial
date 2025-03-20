For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/UUIDUtils.java' with name 'UUIDUtils.java' where below a part of it is displayed...
```java
public static String generateShortTextUUID() {
    String uuid = toShortText(UUID.randomUUID());
    int lengthOrig = StringUtils.length(uuid);
    if (lengthOrig < EXPECTED_FIXED_SIZE) {
        // length is not fixed. Add some more random characters.
        // Still we ONLY want the allowed characters and no special or similar looking one.
        // Hence take it of another UUID we generate
        String uuid2 = toShortText(UUID.randomUUID());
        uuid = uuid + StringUtils.substring(uuid2, 0, EXPECTED_FIXED_SIZE - lengthOrig);
    }
    return uuid;
}
```
What is the purpose of this `generateShortTextUUID` method, and why does it include a conditional block to potentially append characters from another UUID? Explain the logic.