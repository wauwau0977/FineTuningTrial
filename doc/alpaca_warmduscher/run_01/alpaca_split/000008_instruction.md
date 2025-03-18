You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This code defines a class `Profiles` containing static string constants representing application profiles. These profiles likely control which implementation of a service or component (e.g., a temperature sensor) is used. The defined profiles are "default" and "sensormock", which suggests a capability for testing with mock data instead of real hardware.

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/Profiles.java
- **Class Name(s):** `com.x8ing.thsensor.thserver.Profiles`

## 3. Functional Requirements

- **Primary Operations**: Defines application profiles (constants).
- **User Inputs & Outputs**: No direct user input or output. The profiles are used internally within the application.
- **Workflow/Logic**:  The class provides a simple lookup mechanism for profile names.  The application logic can switch behavior based on the currently active profile.
- **External Interactions**: No external interactions.
- **Edge Cases Handling**: No specific edge cases to handle within this class. The application logic using these profiles should handle invalid profile names gracefully.

## 4. Non-Functional Requirements

- **Performance**: Negligible. The class only defines constants; performance is not a concern.
- **Scalability**: Not applicable.
- **Security**: Not applicable.
- **Maintainability**: Highly maintainable. Simple and straightforward class definition.
- **Reliability & Availability**:  High.  Constant values are inherently reliable.
- **Usability**: Easy to use within the application.
- **Compliance**: Not applicable.

## 5. Key Components

- **Functions**: No functions. The class contains only static final string constants.
- **Important logic flows**:  No specific logic flows.
- **Error handling**: No error handling.
- **Classes**: No subclasses defined.
- **Modules**: N/A

## 6. Dependencies

### 6.1 Core Language Features
- Strings
- Static variables

### 6.2 External Frameworks & Libraries
- None.

### 6.3 Internal Project Dependencies
- None.

## 7. Potential Improvements

- **Enum instead of Strings**:  Consider using an `enum` instead of static string constants. This would provide type safety and prevent accidental typos in profile names.  It would also enhance code readability.
- **Configuration Management**:  Instead of hardcoding the profiles, consider loading them from a configuration file or environment variables.  This would allow for easier profile switching without code changes.
- **Documentation**: Add Javadoc comments to the class and constants to explain their purpose and usage.