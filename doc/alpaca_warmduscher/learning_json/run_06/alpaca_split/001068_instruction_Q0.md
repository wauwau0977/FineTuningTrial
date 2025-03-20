You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary
This class, `HeatingModbusReadService`, is responsible for reading data from a Modbus TCP device (heat pump) and converting it into a `HeatPumpEntity` object. It communicates with the heat pump using the jlibmodbus library, reads various input registers and discrete inputs, and maps these values to properties within the `HeatPumpEntity`. The service is designed to be initiated once during application startup and periodically read data from the heat pump. Includes a debugging/scanning mode to read all registers.

## 2. File Information
- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/device/service/impl/HeatingModbusReadService.java
- **Class Name(s):** `HeatingModbusReadService`

## 3. Functional Requirements
- **Primary Operations**: Reads data from a Modbus TCP heat pump and maps it to a `HeatPumpEntity`.  Provides a scan functionality to read all available registers for debugging.
- **User Inputs & Outputs**:
    - **Inputs**: Configuration parameters such as the heat pump IP address.  Internally, the service uses Modbus register addresses to read specific values.
    - **Outputs**: A `HeatPumpEntity` object containing the read data.  A list of strings containing register values during the scan operation.
- **Workflow/Logic**:
    1. **Initialization:** The service initializes a Modbus master connection using the configured IP address.
    2. **Data Reading:**  The `getData()` method reads a predefined set of input registers and discrete inputs.
    3. **Data Mapping:** Read values are mapped to properties of the `HeatPumpEntity`.
    4. **Data Return:** The populated `HeatPumpEntity` object is returned.
    5. **Scanning**: The `scanAllRegisters()` method reads all input registers, holding registers and discrete inputs and returns them as a list of strings.
- **External Interactions**:
    - **Modbus TCP:** Establishes a TCP connection with the heat pump at the configured IP address and port (502).
    - **jlibmodbus library**: Uses the jlibmodbus library to send Modbus requests (read input registers, read discrete inputs) and receive responses.
- **Edge Cases Handling**:
    - **Connection Errors:**  Handles potential connection errors when establishing the Modbus TCP connection (handled via GlobalSynced hook).
    - **Invalid Register Addresses:**  Assumes valid register addresses are used.  (No explicit error handling for this case currently).
    - **Communication Timeout**: Assumes the jlibmodbus library handles communication timeouts.
    - **Data Conversion**: The `getSignedNumber()` method handles conversion of int to signed numbers.

## 4. Non-Functional Requirements
- **Performance**: The data reading process should be relatively quick to allow for periodic updates of the `HeatPumpEntity`.  Scanning can take a significant amount of time due to reading all available registers.
- **Scalability**: The service is designed for a single heat pump. Scaling to multiple heat pumps would require modification to handle multiple connections.
- **Security**: The communication with the heat pump is not encrypted.  This could be a security concern if the network is not trusted.
- **Maintainability**: The code is reasonably well-structured, with clear separation of concerns.  Adding new registers and data mappings would require modifying the `getData()` method.
- **Reliability & Availability**: The service relies on the stability of the Modbus TCP connection and the jlibmodbus library.
- **Usability**: The service is designed to be used by other components within the `Warmduscher` application.
- **Compliance**:  No specific compliance requirements are mentioned.

## 5. Key Components
- **`HeatingModbusReadService` Class**: The main class that handles the communication with the heat pump and data mapping.
- **`getData()` Function**: Reads data from the heat pump and returns a `HeatPumpEntity`.
- **`scanAllRegisters()` Function**: Scans all registers and return register values as a list of strings.
- **`readInputRegister()` Function**: Reads a single input register and scales it according to the provided parameters.
- **`getSignedNumber()` Function**: Converts an integer to a signed integer using two's complement.
- **`modbusMasterSynced`**: An instance of `GlobalSynced<ModbusMaster>`, ensuring thread-safe access to the Modbus master connection.
- **`modBusMasterHooks`**:  Hooks for connecting and disconnecting the Modbus master.

## 6. Dependencies

### 6.1 Core Language Features
- Java 8 or later.
- Collections (Lists, Arrays)
- Logging (SLF4J)
- Atomic Integer
- InetAddress

### 6.2 External Frameworks & Libraries
- **jlibmodbus:** Used for Modbus TCP communication.
- **SLF4J:** Used for logging.
- **Apache Commons Lang3:** Used for string manipulation (StringUtils.equals).

### 6.3 Internal Project Dependencies
- `com.x8ing.thsensor.thserver.db.entity.HeatPumpEntity`: Represents the data structure for storing heat pump data.
- `com.x8ing.thsensor.thserver.utils.mutex.GlobalSynced`:  Provides thread-safe access to shared resources.
- `com.x8ing.thsensor.thserver.utils.mutex.Hooks`: Provides before/after hooks for resource operations.

## 7. Potential Improvements
- **Performance Enhancements:**
    - Optimize the data reading process by reading multiple registers in a single request.
    - Consider using a caching mechanism to reduce the number of Modbus requests.
- **Code Readability:**
    - Extract the register address constants into a separate configuration file or enum for better maintainability.
    - Add more comments to explain the purpose of each register and its corresponding data mapping.
- **Security Improvements:**
    - Consider implementing encryption or authentication to secure the Modbus TCP communication.
- **Scalability Considerations:**
    - Design the service to handle multiple heat pumps by creating a separate Modbus master connection for each device.
    - Consider using a message queue to decouple the data reading process from the application.
- **Error Handling**: Add explicit error handling for invalid register addresses or communication errors.
- **Configuration**: Make the IP address configurable via properties file or environment variables.
- **Unit Tests**: Add unit tests to verify the correctness of the data mapping and error handling logic.