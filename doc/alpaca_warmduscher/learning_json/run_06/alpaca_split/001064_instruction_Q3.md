For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/device/service/impl/HeatingDataReadServiceMock.java' with name 'HeatingDataReadServiceMock.java' where below a part of it is displayed...

```java
   @Override
   public HeatPumpEntity getData() throws Exception {
       @SuppressWarnings("IntegerDivisionInFloatingPointContext")
       double dtS = (System.currentTimeMillis() - t0) / 1000;
       HeatPumpEntity ret = new HeatPumpEntity();
       ret.setHeatingIn(dtS / 30 + 20);
       ret.setHeatingOut(dtS / 30 + 30);
       ret.setSoleIn(dtS / 30 + 10);
       ret.setSoleOut(dtS / 30 + 5);
       ret.setBoilerTemp(dtS / 30 + 30);
       ret.setCompressorHours((int) (dtS + 100));
       ret.setIreg300TempOutdoor(dtS / 10 - 12);
       log.info("Return " + ret);
       return ret;
   }
```

What is the purpose of the `dtS` variable and how is it used to calculate the values for different attributes of the `HeatPumpEntity`? Explain the calculation.