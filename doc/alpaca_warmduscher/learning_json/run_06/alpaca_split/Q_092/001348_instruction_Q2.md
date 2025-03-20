For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/MySessionFilter.java' with name 'MySessionFilter.java'... 
Consider the following code snippet from the `doFilter` method:

```java
cookie.setHttpOnly(false);
cookie.setMaxAge(60 * 60 * 24 * 365); // 1Y
cookie.setPath("/");
```

What are the security implications of setting `HttpOnly` to `false`? Explain the risks and suggest a better approach if security is a primary concern.