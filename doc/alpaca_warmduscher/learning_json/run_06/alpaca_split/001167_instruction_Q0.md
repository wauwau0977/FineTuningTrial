You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This code defines a utility interface named `Unsafe` providing static methods to execute functions, callables, and runnables within a try-catch block, re-throwing any caught exceptions as `RuntimeException`. It essentially provides a simplified way to handle exceptions when executing potentially unsafe operations, by wrapping the execution and forwarding exceptions. This simplifies error handling in scenarios where specific exception handling isn't required at the call site.

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/Unsafe.java
- **Class Name(s):** `Unsafe`

## 3. Functional Requirements

- **Primary Operations**:  Execute functions, callables, or runnables and propagate any exceptions thrown by them as `RuntimeException`.
- **User Inputs & Outputs**:
    - `execute(Function<P, R> f, P param)`: Takes a function and a parameter. Returns the result of the function, or null if the function is null.
    - `execute(Callable<R> c)`: Takes a callable. Returns the result of the callable, or null if the callable is null.
    - `execute(UnsafeRunnable c)`: Takes a runnable.  Does not return a value.
- **Workflow/Logic**: Each method checks if the input (function, callable, or runnable) is null. If not null, it attempts to execute the input within a try-catch block. If an exception is caught during execution, it's wrapped in a `RuntimeException` and thrown.  If the input is null, the method returns null (for `Function` and `Callable`) or returns immediately (for `Runnable`).
- **External Interactions**: None. The methods are self-contained and don't interact with external systems.
- **Edge Cases Handling**:
    - Null input: If the input function, callable, or runnable is null, the method handles this by returning null (for `Function` and `Callable`) or doing nothing (for `Runnable`).
    - Exceptions during execution:  Any exception thrown by the function, callable, or runnable is caught and re-thrown as a `RuntimeException`. This ensures that errors are propagated to the calling code.

## 4. Non-Functional Requirements

- **Performance**: The performance overhead is minimal, consisting of the exception handling overhead.  Shouldn't be a significant bottleneck.
- **Scalability**: The code is stateless and doesn't involve any shared resources, so it should scale well.
- **Security**: No specific security considerations. The code doesn't handle sensitive data or perform any security-critical operations.
- **Maintainability**: The code is simple and easy to understand. The use of static methods and clear logic contribute to maintainability.
- **Reliability & Availability**: The code relies on Java's exception handling mechanisms, which are generally reliable. The code itself doesn’t introduce any points of failure.
- **Usability**:  The methods provide a convenient way to handle exceptions in scenarios where detailed error handling is not required.
- **Compliance**: No specific compliance requirements.

## 5. Key Components

- **Functions**:
    - `execute(Function<P, R> f, P param)`: Executes a function with a parameter and returns the result.
    - `execute(Callable<R> c)`: Executes a callable and returns the result.
    - `execute(UnsafeRunnable c)`: Executes a runnable.
- **Important logic flows**: All methods follow a similar flow: null check, try-catch block for execution, re-throw of exceptions as `RuntimeException`.
- **Error handling**: All methods wrap potential exceptions in `RuntimeException` to propagate them.
- **Classes**: None. This is an interface with static methods.
- **Modules**: This is a utility class with static methods, and does not have modules.

## 6. Dependencies

### 6.1 Core Language Features
- Java 8 Functional Interfaces (Function, Callable)
- Exception handling (try-catch blocks)

### 6.2 External Frameworks & Libraries
- None. This class uses core Java features only.

### 6.3 Internal Project Dependencies
- `UnsafeRunnable` - Custom interface used to define the contract for a runnable that can throw exceptions. (This should be described elsewhere in the project documentation).

## 7. Potential Improvements

- **Performance Enhanecements**:  The code is simple, and performance is unlikely to be a bottleneck. No immediate improvements needed.
- **Code Readability**: The code is already reasonably readable.
- **Security Improvements**: No specific security risks identified.
- **Scalability Considerations**:  The code is already scalable, as it's stateless and doesn't rely on shared resources.
- **Logging**: Consider adding logging within the `catch` block to record the original exception before re-throwing it as a `RuntimeException`. This could aid in debugging.
- **Custom Exception**: Instead of always re-throwing a `RuntimeException`, consider creating a custom exception type specific to the `Unsafe` utility. This would allow calling code to handle exceptions thrown by this utility differently from other exceptions.