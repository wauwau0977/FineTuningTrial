```java
@Override
public List<String> scanAllRegisters(int maxRegister) {
    long t0 = System.currentTimeMillis();
    List<String> res = new ArrayList<>();
    final String SEP = "================================================================================";
    modbusMasterSynced.requestOperation(modbusMaster -> {
        res.add("Scan start time: " + new Date());
        res.add("maxRegister: " + maxRegister);
        // read input registers
        res.add(SEP);
        res.add("InputRegister");
        for (int inputRegister = 0; inputRegister <= maxRegister; inputRegister++) {
            int[] values = modbusMaster.readInputRegisters(slaveId, inputRegister, 1);
            String val = Arrays.toString(values);
            if (!StringUtils.equals("[0]", val)) {
                res.add(inputRegister + ": " + val);
            }
        }
        //
        res.add(SEP);
        res.add("Holding Register");
        for (int inputRegister = 0; inputRegister < maxRegister; inputRegister++) {
            int[] values = modbusMaster.readHoldingRegisters(slaveId, inputRegister, 1);
            String val = Arrays.toString(values);
            if (!StringUtils.equals("[0]", val)) {
                res.add(inputRegister + ": " + val);
            }
        }
        // ... (rest of the method)
```
The `scanAllRegisters` method iterates through a range of Modbus registers. What is the purpose of the `if (!StringUtils.equals("[0]", val))` condition within the loops, and why is it important?