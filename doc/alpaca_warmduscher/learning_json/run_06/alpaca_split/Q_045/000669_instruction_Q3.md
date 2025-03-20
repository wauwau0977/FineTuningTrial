For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/Profiles.java' with name 'Profiles.java' where below a part of it is displayed... 
```java
public class Profiles {
   public static final String DEFAULT = "default";
   /**
    * use a mock implementation instead of the real modbus or the real service.
    */
   public static final String SENSOR_MOCK = "sensormock";
}
```
What is the benefit of using named constants (like `DEFAULT` and `SENSOR_MOCK`) instead of hardcoding the string literals directly within the application's logic?