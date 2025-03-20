For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/MyRequestInterceptor.java' with name 'MyRequestInterceptor.java' where below a part of it is displayed...
```java
@Override
   public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
       long startTime = System.currentTimeMillis();
       request.setAttribute(START_TIME_ATTR_NAME, startTime);
       return true;
   }
```
What is the purpose of the `preHandle` method, and what information is being stored and how?