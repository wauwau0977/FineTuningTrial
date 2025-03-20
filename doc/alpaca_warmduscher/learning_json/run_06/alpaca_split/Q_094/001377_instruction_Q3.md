For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/dialogflow/JSONFactory.java' with name 'JSONFactory.java' where below a part of it is displayed... 

```java
@Component
public class JSONFactory {

   @Bean
   public JacksonFactory jacksonFactory() {
       return JacksonFactory.getDefaultInstance();
   }
}
```

What is the purpose of the `@Component` annotation in this code snippet, and how does it relate to Spring's dependency injection?