You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary
This class, `MemoryInfo`, is a simple data transfer object (DTO) designed to encapsulate and provide information about the system's memory usage and processor count. It allows retrieval of current memory statistics (total, max, free) in kilobytes and the number of available processors. It primarily serves as a bean for web service responses, providing system health information.

## 2. File Information
- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/info/bean/MemoryInfo.java
- **Class Name(s):** `com.x8ing.thsensor.thserver.web.services.info.bean.MemoryInfo`

## 3. Functional Requirements
- **Primary Operations**:  Provides current system memory and processor information.
- **User Inputs & Outputs**: This class doesn’t directly receive user inputs. Outputs are the values of the encapsulated data: totalMemoryKb, maxMemoryKb, freeMemoryKb and availableProcessors.
- **Workflow/Logic**: 
    1. The `getCurrent()` method retrieves runtime information.
    2. It obtains the total, max, and free memory from `Runtime.getRuntime()`.
    3. It obtains the number of available processors from `Runtime.getRuntime()`.
    4. It creates a `MemoryInfo` object and populates it with the retrieved values.
    5. The populated `MemoryInfo` object is returned.
- **External Interactions**: Interacts with the Java Runtime Environment (JRE) to retrieve system information.
- **Edge Cases Handling**: No explicit error handling is present. `Runtime.getRuntime()` may throw exceptions if the system is critically low on resources, but this is not handled within the class.

## 4. Non-Functional Requirements
- **Performance**: The `getCurrent()` method should execute quickly as it only involves calls to `Runtime.getRuntime()` and basic calculations. Expected execution time is well under 1ms.
- **Scalability**: Not directly related to scalability concerns as it's a simple data object. However, excessive calls to `getCurrent()` under heavy load could impact performance.
- **Security**:  No security considerations are applicable, as the class doesn't handle sensitive data or user authentication.
- **Maintainability**: The class is relatively simple and easy to understand, promoting maintainability.
- **Reliability & Availability**: The class relies on the JRE, which is generally highly reliable. The class itself doesn't introduce any significant points of failure.
- **Usability**: Easy to integrate into web service responses as a simple data bean.
- **Compliance**: No specific compliance requirements.

## 5. Key Components
- **Functions:**
    - `MemoryInfo()`: Constructor with no arguments
    - `MemoryInfo(long totalMemoryKb, long maxMemoryKb, long freeMemoryKb)`: Constructor with parameters.
    - `getCurrent()`: Static method to retrieve the current system memory and processor information.
    - `getTotalMemoryKb()`: Getter for totalMemoryKb.
    - `setTotalMemoryKb(long totalMemoryKb)`: Setter for totalMemoryKb.
    - `getMaxMemoryKb()`: Getter for maxMemoryKb.
    - `setMaxMemoryKb(long maxMemoryKb)`: Setter for maxMemoryKb.
    - `getFreeMemoryKb()`: Getter for freeMemoryKb.
    - `setFreeMemoryKb(long freeMemoryKb)`: Setter for freeMemoryKb.
    - `getAvailableProcessor()`: Getter for availableProcessors.
    - `setAvailableProcessor(long availableProcessor)`: Setter for availableProcessors.
- **Important logic flows**: The `getCurrent()` function is the central logic. It retrieves system information and populates a new `MemoryInfo` object.
- **Error handling**: None.
- **Classes**: No subclasses are defined.
- **Modules**: The class functions as a standalone bean within the `web.services.info.bean` package.

## 6. Dependencies

### 6.1 Core Language Features
- Data structures: Primitive long type.
- Runtime API: `Runtime.getRuntime()`, `Runtime.availableProcessors()`, `Runtime.totalMemory()`, `Runtime.freeMemory()`.

### 6.2 External Frameworks & Libraries
- None.

### 6.3 Internal Project Dependencies
- None.

## 7. Potential Improvements
- **Performance Enhanecements**:  Caching the values returned by `getCurrent()` for a short period could reduce the load on the runtime, but this may introduce stale information.
- **Code Readability**: The code is already quite readable due to its simplicity.
- **Security Improvements**: Not applicable.
- **Scalability Considerations**: Consider a background task or scheduled job to periodically update the `MemoryInfo` and store it in a shared cache if frequent access is required. This can reduce the load on the runtime during peak request times.
- **Error Handling**: Implement basic error handling in `getCurrent()` to prevent potential crashes if the runtime throws an exception. This could involve logging the error and returning default values.
- **Unit Tests**:  Add unit tests to verify the accuracy of the data returned by `getCurrent()`. This should include testing with different system configurations and resource levels.