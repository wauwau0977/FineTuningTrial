For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/mutex/GlobalSynced.java' with name 'GlobalSynced.java'... 
Assume the `Hooks` interface is defined as follows:

```java
interface Hooks<T> {
    void before(T syncedObject);
    void after(T syncedObject);
}
```

Describe a scenario where defining `Hooks` as a generic interface (as it is now) is *beneficial*, and a scenario where it might be *unnecessary complexity*. Explain your reasoning.