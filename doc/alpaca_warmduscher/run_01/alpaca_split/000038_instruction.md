You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This code implements a service to read heating data from a Modbus TCP device, specifically a heat pump. It reads various registers and discrete inputs to gather information such as temperatures, compressor hours, and the status of different components. This data is then encapsulated into a `HeatPumpEntity` object, providing a structured representation of the heat pump's operational state. The service utilizes a synchronized Modbus master connection to ensure thread safety.

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/device/service/impl/HeatingModbusReadService.java
- **Class Name(s):** `HeatingModbusReadService`

## 3. Functional Requirements

- **Primary Operations:**
    - Read data from a Modbus TCP heat pump.
    - Retrieve specific register and discrete input values.
    - Encapsulate the data into a `HeatPumpEntity` object.
    - Provide a scan function to read all registers for debugging purposes.
- **Data Read:** The service reads various registers and discrete inputs, including:
    - Temperatures (heating out, compressor, etc.)
    - Compressor hours
    - Status of compressors, pumps, and valves.
    - Error flags
- **Synchronization:** The service utilizes a synchronized Modbus master connection to handle concurrent requests.
- **Error Handling:** While not explicitly detailed, exception handling is present in `readInputRegister` and can be extended for more robust error handling.
- **Scanning:** A `scanAllRegisters` function provides the ability to read all available registers and discrete inputs for troubleshooting.

## 4. Non-Functional Requirements

- **Thread Safety:** The service must be thread-safe due to the use of a synchronized Modbus master connection.
- **Performance:** The data retrieval process should be efficient to minimize latency.
- **Maintainability:** The code should be well-structured and documented to facilitate future maintenance and enhancements.

## 5. Data Model

- **HeatPumpEntity:** This class (not defined in the provided code, but used as a return type) is expected to contain the following data:
    - Temperatures (various)
    - Compressor hours
    - Status of compressors, pumps, and valves (boolean values)
    - Error flags (boolean values)

## 6. API/Interface

- **`HeatingModbusReadService`**:
    - `HeatPumpEntity getData()`: Retrieves the current heat pump data.
    - `List<String> scanAllRegisters(int maxRegister)`: Scans and returns a list of strings representing all registers up to `maxRegister`.
    - `readInputRegister(ModbusMaster modbusMaster, int address, boolean signed, int scale)`: Protected method for reading input registers.

## 7. Dependencies

- **j2mod:**  (Implicitly, from ModbusMaster usage) A Java Modbus library.
- **ModbusMaster:**  An interface or class from the j2mod library used to interact with the Modbus TCP device.
- **StringUtils:** From Apache Commons Lang for string manipulation.

## 8. Design Considerations

- **Modbus Addressing:** The code relies on specific Modbus register and discrete input addresses. These addresses are hardcoded and may need to be configurable for different heat pump models.
- **Data Scaling:** The `readInputRegister` method includes scaling to convert raw register values to meaningful units.
- **Error Handling:** The code includes basic exception handling in `readInputRegister`. More robust error handling could be implemented to handle network errors, invalid register addresses, and other potential issues.
- **Configuration:** The Modbus IP address, port, and register addresses could be externalized to a configuration file.

## 9. Future Enhancements

- **Configuration:** Allow Modbus IP address, port, and register addresses to be configured externally.
- **Error Handling:** Implement more robust error handling with logging and retries.
- **Data Validation:** Validate the retrieved data to ensure its integrity and accuracy.
- **Caching:** Implement caching to reduce the frequency of Modbus requests.
- **Unit Tests:** Add unit tests to verify the functionality of the service.
- **Logging:** Add comprehensive logging to track the data retrieval process and identify potential issues.