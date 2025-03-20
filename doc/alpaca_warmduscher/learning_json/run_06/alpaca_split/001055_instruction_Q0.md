You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This class, `HeatingDataReadServiceMock`, is a mock implementation of the `HeatingDataReadService` interface within the 'Warmduscher' project. It simulates reading heating data from a heat pump. This mock is activated only when the application is running with the `SENSOR_MOCK` profile. It generates synthetic data based on the elapsed time since the service initialization, providing values for various heating-related parameters.

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/device/service/impl/HeatingDataReadServiceMock.java
- **Class Name(s):** `HeatingDataReadServiceMock`

## 3. Functional Requirements

- **Primary Operations**: This class provides mock heating data for testing and development purposes.
- **User Inputs & Outputs**:
    - **Input**: None directly. The data generation depends on system time.
    - **Output**: A `HeatPumpEntity` object containing simulated heating data.
- **Workflow/Logic**:
    1. The `getData()` method calculates the elapsed time (in seconds) since service initialization (`t0`).
    2. Based on the elapsed time, it generates values for:
        - `heatingIn`
        - `heatingOut`
        - `soleIn`
        - `soleOut`
        - `boilerTemp`
        - `compressorHours`
        - `ireg300TempOutdoor`
    3. These generated values are set in a new `HeatPumpEntity` object.
    4. The populated `HeatPumpEntity` is returned.
- **External Interactions**:
    - Logging using SLF4J.
- **Edge Cases Handling**: 
    - The `scanAllRegisters` method always returns a list containing the string "Not implemented". This indicates that this functionality is not available in the mock implementation.

## 4. Non-Functional Requirements

- **Performance**: The data generation is simple and should execute very quickly. No significant performance concerns are anticipated.
- **Scalability**: As a mock, scalability is not a primary concern.
- **Security**: No security considerations are relevant as this is a mock implementation.
- **Maintainability**: The code is relatively simple and easy to understand.
- **Reliability & Availability**: High reliability and availability are not critical for a mock.
- **Usability**:  The mock is intended for development and testing and is easy to integrate into a testing environment.
- **Compliance**: No specific compliance requirements.

## 5. Key Components

- **Functions:**
    - `init()`:  An empty method, does nothing.  Left over from the Interface.
    - `getData()`:  Generates and returns a `HeatPumpEntity` with mock heating data.
    - `scanAllRegisters(int maxRegister)`: Returns a list containing "Not implemented".
- **Important logic flows**: The `getData()` method calculates values based on a time delta.
- **Error handling**: No explicit error handling is present.
- **Classes**: No subclasses defined.
- **Modules**: This class is a self-contained module providing mock data.

## 6. Dependencies

### 6.1 Core Language Features

- Data structures: Lists
- Time: System.currentTimeMillis()

### 6.2 External Frameworks & Libraries

- **SLF4J**: Used for logging.
- **Spring Framework**: Used for `@Component` and `@Profile` annotations.

### 6.3 Internal Project Dependencies

- **`com.x8ing.thsensor.thserver.db.entity.HeatPumpEntity`**: Represents the structure of the heating data being mocked.
- **`com.x8ing.thsensor.thserver.Profiles`**: Defines the application profiles including `SENSOR_MOCK`.
- **`com.x8ing.thsensor.thserver.device.service.HeatingDataReadService`**: The interface implemented by this class.

## 7. Potential Improvements

- **Performance Enhancements:** No significant performance improvements are needed given the simple calculations.
- **Code Readability:** The code is reasonably readable. Adding more comments could improve clarity.
- **Security Improvements:** Not applicable to a mock implementation.
- **Scalability Considerations:** Not applicable.
- **Data Customization**: Allow the data generation parameters (e.g. factors in the calculation) to be configurable via properties, allowing for more realistic and varied mock data.
- **More Realistic Mock**:  Explore generating data that more closely resembles real-world heating system behavior.