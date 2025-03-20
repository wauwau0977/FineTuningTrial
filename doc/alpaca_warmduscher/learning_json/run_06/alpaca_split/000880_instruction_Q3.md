For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/HeatPumpEntity.java' with name 'HeatPumpEntity.java' where below a part of it is displayed...
```java
public Boolean isDi19HeatPumpOn() {
    return di19HeatPumpOn;
}
public void setDi19HeatPumpOn(Boolean di19HeatPumpOn) {
    this.di19HeatPumpOn = di19HeatPumpOn;
}
```
Explain the purpose of having both a getter (`isDi19HeatPumpOn`) and a setter (`setDi19HeatPumpOn`) method for the `di19HeatPumpOn` field.  Why is this pattern commonly used in Java, particularly in the context of JPA entities?