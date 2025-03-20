For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/MvcConfig.java' with name 'MvcConfig.java'... 
Consider the following code snippet:
```java
   @Override
   public void addInterceptors(final InterceptorRegistry registry) {
       registry.addInterceptor(new MyRequestInterceptor(sessionRequestRepository));
   }
```
What is the purpose of the `final` keyword in the method parameter `final InterceptorRegistry registry`? How does it contribute to the overall robustness and maintainability of the code?