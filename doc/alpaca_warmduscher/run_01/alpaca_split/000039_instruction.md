You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This class, `HeatingDataReadServiceMock`, provides a mock implementation of the `HeatingDataReadService` interface. It's designed to simulate data retrieval for heating system parameters during development or testing, specifically when a real heating data source is unavailable or undesirable. The mock data is generated based on the elapsed time since a fixed timestamp (`t0`), providing time-varying values for various heating system metrics. This implementation is activated when the application runs with the `SENSOR_MOCK` profile.

## 2. File Information

- **File Location:** `Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/device/service/impl/HeatingDataReadServiceMock.java`
- **Class Name(s):** `HeatingDataReadServiceMock`

## 3. Functional Requirements

- **Primary Operations:** Simulate retrieval of heating data.
- **User Inputs & Outputs:**  No direct user input. The service outputs a `HeatPumpEntity` object containing simulated heating data.
- **Workflow/Logic:**
    1. Calculates the elapsed time (`dtS`) in seconds since a fixed timestamp (`t0`).
    2. Populates a `HeatPumpEntity` with simulated values for `heatingIn`, `heatingOut`, `soleIn`, `soleOut`, `boilerTemp`, `compressorHours`, and `ireg300TempOutdoor`, based on the calculated `dtS`.
    3. Logs the returned `HeatPumpEntity` object using SLF4J.
    4. Returns the populated `HeatPumpEntity`.
- **External Interactions:**
    - Logging via SLF4J.
- **Edge Cases Handling:**
    - The `init()` method is defined but does not contain any implementation. This is acceptable as the mock service does not require any initialization steps.
    - The `scanAllRegisters` method returns a list containing the string "Not implemented", indicating that this functionality is not supported in the mock implementation.

## 4. Non-Functional Requirements

- **Performance:** The mock service is expected to be very fast, as it only involves simple calculations and object creation. The execution time should be negligible.
- **Scalability:** Not a primary concern for a mock service. It's designed for testing, not high-volume production use.
- **Security:** Not applicable. The mock service does not handle sensitive data or external connections.
- **Maintainability:** The code is relatively simple and easy to understand.
- **Reliability & Availability:** High reliability is expected, as the service only generates data and does not depend on external systems.
- **Usability:** The mock service is easy to use and integrate, as it implements the same interface as the real data source.
- **Compliance:** Not applicable.

## 5. Key Components

- **Functions:**
    - `init()`:  Empty method, intended for potential initialization, but not currently used.
    - `getData()`: Generates a `HeatPumpEntity` with mock heating data based on elapsed time.
    - `scanAllRegisters(int maxRegister)`: Returns a list containing the string "Not implemented".
- **Important Logic Flows:**  The core logic resides within the `getData()` method, where the mock data is calculated and the `HeatPumpEntity` is populated.
- **Error Handling:**  No explicit error handling is present. Any exceptions would be thrown by the underlying Java code.
- **Classes:** No subclasses defined.
- **Modules:** Part of the `thserver` module.

## 6. Dependencies

### 6.1 Core Language Features

- Basic Java data types (double, int, long).
- Collections (List).
- System.currentTimeMillis() for timestamping.

### 6.2 External Frameworks & Libraries

- **SLF4J:** Logging framework.
- **Spring Framework:**  Used for component management (`@Component`) and profile activation (`@Profile`).

### 6.3 Internal Project Dependencies

- `com.x8ing.thsensor.thserver.Profiles`: Used to define the profile name (`SENSOR_MOCK`) that activates this mock implementation.
- `com.x8ing.thsensor.thserver.db.entity.HeatPumpEntity`: Represents the data structure for heating system parameters.

## 7. Potential Improvements

- **Performance Enhancements:** Not a priority, as the performance is already sufficient for a mock service.
- **Code Readability:** The code is already relatively readable.
- **Security Improvements:** Not applicable.
- **Scalability Considerations:** Not applicable.
- **Configurability:** Allow the initial timestamp (`t0`) and the scaling factors used in the data generation to be configurable through properties or environment variables. This would make the mock service more flexible and realistic.
- **More Realistic Data Generation:**  Improve the data generation logic to simulate more complex and realistic heating system behavior, potentially including random variations or correlations between different parameters.
- **Mock of `scanAllRegisters`:** Although not a requirement, a simple implementation of `scanAllRegisters` returning a list of mocked register values could be useful for more comprehensive testing.