You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary
This code defines a class `Profiles` containing static string constants representing application profiles. These profiles are used to select different configurations or implementations within the `Warmduscher` application, particularly for sensor data acquisition. Currently, it supports a "default" profile and a "sensormock" profile, enabling the use of a mock sensor implementation for testing or demonstration purposes.

## 2. File Information
- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/Profiles.java
- **Class Name(s):** `Profiles`

## 3. Functional Requirements
- **Primary Operations**: Defines application profiles as string constants. These profiles act as configuration identifiers.
- **User Inputs & Outputs**: No direct user inputs or outputs. The profiles are used internally by other components.
- **Workflow/Logic**: The code simply defines static final strings. There's no procedural logic.
- **External Interactions**: No direct external interactions. The profiles are intended to be used by other components to determine runtime behavior.
- **Edge Cases Handling**: There are no edge cases to handle as the code only defines static constants.

## 4. Non-Functional Requirements
- **Performance**: Negligible performance impact as it only defines static constants.
- **Scalability**: Not applicable as the code doesn't involve any processing or data handling.
- **Security**: Not applicable.
- **Maintainability**:  Highly maintainable due to its simplicity and use of static constants. Adding new profiles is straightforward.
- **Reliability & Availability**: The code itself is entirely reliable as it is a static definition.
- **Usability**:  Usable as configuration keys within the application.
- **Compliance**: Not applicable.

## 5. Key Components
- **`DEFAULT`**:  A string constant representing the default application profile.
- **`SENSOR_MOCK`**: A string constant representing a profile using a mock sensor implementation.
- **Error handling**: None.
- **Classes**: No subclasses are defined.
- **Modules**: This class represents a small module for defining application profiles.

## 6. Dependencies

### 6.1 Core Language Features
- Basic Java data types (String)
- Static variables and constants

### 6.2 External Frameworks & Libraries
- None

### 6.3 Internal Project Dependencies
- None. This class is self-contained.

## 7. Potential Improvements
- **Configuration Management**:  Consider using a more robust configuration management system (e.g., Spring profiles, environment variables, configuration files) to manage application profiles instead of hardcoding them. This would allow for easier switching between profiles without code changes.
- **Enum**: Consider using an enum instead of string constants for better type safety and readability.
- **Documentation**: Add more detailed Javadoc comments explaining the purpose of each profile and when to use it.