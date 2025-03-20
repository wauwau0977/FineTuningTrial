For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/Physics.java' with name 'Physics.java' where below a part of it is displayed... 
```java
public static final double calculateAbsoluteHumidityApproximation(double temperature, double relativeHumidity) {
    return (6.112 * Math.exp((17.67 * temperature) / (temperature + 243.5)) * relativeHumidity * 2.1674) / ((273.15 + temperature));
}
```
What is the significance of the `relativeHumidity` parameter in this function, and how does it affect the final calculated absolute humidity?