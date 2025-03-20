For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/MySessionFilter.java' with name 'MySessionFilter.java' where below a part of it is displayed... 

```java
   @Override
   public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain) throws IOException, ServletException {
       HttpServletResponse response = (HttpServletResponse) res;
       HttpServletRequest request = (HttpServletRequest) req;
       Cookie cookie = WebUtils.getCookie(request, TH_SERVER_SESSON_ID);
       if (cookie == null) {
           cookie = new Cookie(TH_SERVER_SESSON_ID, UUIDUtils.generateShortTextUUID());
           cookie.setHttpOnly(false);
           cookie.setMaxAge(60 * 60 * 24 * 365); // 1Y
           cookie.setPath("/");
       }
       String sessionId = cookie.getValue();
```
What is the purpose of this code snippet within the `doFilter` method, and what steps are taken if a session cookie (`TH_SERVER_SESSON_ID`) is not found in the request? Explain the significance of the cookie settings applied.