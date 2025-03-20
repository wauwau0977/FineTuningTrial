For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/Utils.java' with name 'Utils.java' where below a part of it is displayed... 
```java
public static String getRequestIP(HttpServletRequest request) {
    for (String header : IP_HEADERS) {
        String value = request.getHeader(header);
        if (value == null || value.isEmpty()) {
            continue;
        }
        return Arrays.toString(value.split("\\s*,\\s*"));
    }
    return Arrays.toString(new String[]{request.getRemoteAddr()});
}
```
What is the purpose of this method, and how does it attempt to determine the client's IP address? Explain the logic behind iterating through the `IP_HEADERS` array.