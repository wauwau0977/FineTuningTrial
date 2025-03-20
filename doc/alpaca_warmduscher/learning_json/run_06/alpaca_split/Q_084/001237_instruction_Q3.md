For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/mutex/Hooks.java' with name 'Hooks.java' where below a part of it is displayed... 
```java
public interface Hooks<T> {
   void before(T t) throws Throwable;
   void after(T t) throws Throwable;
}
```
What is the role of the generic type parameter `T` in this interface? Give a specific example of how this interface could be used with a concrete type for `T`.