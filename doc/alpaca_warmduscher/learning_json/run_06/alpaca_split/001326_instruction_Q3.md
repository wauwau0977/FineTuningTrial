For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/MvcConfig.java' with name 'MvcConfig.java' where below a part of it is displayed...
```java
@Override
public void addInterceptors(final InterceptorRegistry registry) {
    registry.addInterceptor(new MyRequestInterceptor(sessionRequestRepository));
}
```
What is the purpose of this method, and how does it integrate with the `sessionRequestRepository` dependency? Explain what an interceptor does in this context.