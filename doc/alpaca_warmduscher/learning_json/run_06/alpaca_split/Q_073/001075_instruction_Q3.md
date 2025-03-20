```java
protected double readInputRegister(ModbusMaster modbusMaster, int address, boolean signed, int scale) throws Exception {
    int vInt = modbusMaster.readInputRegisters(slaveId, address, 1)[0];
    double vDouble = vInt;
    if (signed) {
        vDouble = getSignedNumber(vInt);
    }
    return vDouble / scale;
}
```
The `readInputRegister` method is designed to read values from Modbus registers. What is the purpose of the `signed` boolean parameter, and how does the method handle negative numbers if `signed` is true?