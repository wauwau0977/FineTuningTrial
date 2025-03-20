You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary
This code defines a custom exception class `ThException` extending `RuntimeException`. It provides a mechanism for handling and propagating application-specific exceptions within the 'Warmduscher' project, specifically within the `thserver` component. It allows for creating exceptions with either a message or a message and a root cause, facilitating better error handling and debugging.

## 2. File Information
- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/ThException.java
- **Class Name(s):** `ThException`

## 3. Functional Requirements
- **Primary Operations**: To define a custom exception class for the Warmduscher project.
- **User Inputs & Outputs**:  The class accepts a string message and/or a `Throwable` cause as input during instantiation. It outputs a `ThException` object, representing the application-specific exception.
- **Workflow/Logic**: The class provides two constructors:
    1.  Takes a string message as input and passes it to the `RuntimeException` superclass constructor.
    2.  Takes a string message and a `Throwable` cause as input and passes both to the `RuntimeException` superclass constructor.
- **External Interactions**: None. The class is self-contained and does not interact with external systems or components.
- **Edge Cases Handling**:  The class handles cases where an exception needs to be thrown with just a message, or with a message and the original cause of the exception. This provides flexibility in reporting errors.

## 4. Non-Functional Requirements
- **Performance**: Negligible impact on performance. The class is lightweight and primarily involves constructor calls.
- **Scalability**:  Scalable as exception handling is generally lightweight.
- **Security**: No direct security implications. Proper use of exception handling throughout the application enhances overall system robustness.
- **Maintainability**: The class is simple and well-defined, making it easy to understand and maintain.
- **Reliability & Availability**: Improves reliability by allowing for specific error handling within the application.
- **Usability**: Improves code readability and maintainability by providing a consistent way to handle application-specific exceptions.
- **Compliance**: N/A

## 5. Key Components
- **Functions**:
    - `ThException(String message)`: Constructor to create an exception with a message.
    - `ThException(String message, Throwable cause)`: Constructor to create an exception with a message and the root cause.
- **Important logic flows**: The class simply defines constructors to initialize the `RuntimeException` superclass with the provided message and cause.
- **Error handling**: The class serves *as* a mechanism for error handling, allowing the calling code to catch and handle specific application errors using `ThException`.
- **Classes**:  No subclasses are defined.
- **Modules**: Belongs to the `utils` package, suggesting it provides utility functionality.

## 6. Dependencies

### 6.1 Core Language Features
- Basic Java syntax and object-oriented principles.
- `RuntimeException` class (built-in Java class)
- String manipulation

### 6.2 External Frameworks & Libraries
- None

### 6.3 Internal Project Dependencies
- None

## 7. Potential Improvements
- **Custom Exception Codes:** Consider adding an integer or enum code to identify specific error types, enabling more granular error handling and reporting.
- **Logging Integration:**  Integrate exception logging within the constructors to automatically log exception details when an instance is created.
- **Documentation:** Add Javadoc comments to clearly explain the purpose and usage of the class and its constructors.