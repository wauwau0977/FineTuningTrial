For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/MySessionFilter.java' with name 'MySessionFilter.java' where below a part of it is displayed... 

```java
   public static boolean isSessionRelevantRequest(HttpServletRequest request) {
       String path = request.getRequestURI();
       return path != null
               && Stream.of("html", "htm", "css", "png", "svg", "woff", "woff2", "json", "js").noneMatch(s -> StringUtils.endsWithIgnoreCase(path, s))
               && !StringUtils.equals("/", path)
               && !StringUtils.equals("/pi11", path)
               && !StringUtils.equals("/pi11/", path)
               && !StringUtils.equalsIgnoreCase(request.getMethod(), HttpMethod.OPTIONS.name()) // ignore preflight requests
               ;
   }
```
What is the purpose of the `isSessionRelevantRequest` method, and explain how it determines whether a request should be considered relevant for session tracking?