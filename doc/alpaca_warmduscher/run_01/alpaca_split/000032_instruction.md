You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary
This code defines a `SpringApplicationRunListener` that intercepts the Spring Boot application startup process. It captures the time taken during startup and stores it in a bean named `StartupData` within the application context. This allows other parts of the application to access and use this startup time information, potentially for logging, monitoring, or performance analysis.

## 2. File Information
- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/spring/MyStartUpListener.java
- **Class Name(s):** `MyStartUpListener`

## 3. Functional Requirements
- **Primary Operations:** Capture the startup time of a Spring Boot application.
- **User Inputs & Outputs:**
    - **Input:** Spring Boot `SpringApplication` instance, command-line arguments (though not directly used), and a `ConfigurableApplicationContext` after the application is ready.
    - **Output:** Sets the `startupTimeTakenInMillis` property of a `StartupData` bean within the application context.
- **Workflow/Logic:**
    1. The `MyStartUpListener` is registered as a `SpringApplicationRunListener` via the `spring.factories` file.
    2. When the Spring Boot application starts, the `ready()` method of this listener is called *after* the application context has been initialized.
    3. Inside the `ready()` method, it retrieves a bean named `StartupData` from the application context.
    4. It then extracts the startup time (as a `Duration`) from the `ConfigurableApplicationContext` and converts it to milliseconds.
    5. Finally, it sets the `startupTimeTakenInMillis` property of the `StartupData` bean with the calculated startup time.
- **External Interactions:** 
    - Interacts with the Spring Boot application context to retrieve and set beans.
- **Edge Cases Handling:**
    - If the `StartupData` bean is not found in the application context, a `NullPointerException` will occur. (This is not explicitly handled in the provided code).

## 4. Non-Functional Requirements
- **Performance:** The listener should have minimal impact on the overall application startup time.  The operations performed are simple and should execute quickly.
- **Maintainability:** The code is relatively simple and easy to understand, promoting maintainability.
- **Reliability & Availability:** The listener's failure shouldn't prevent the application from starting. The absence of the `StartupData` bean is a potential point of failure.
- **Usability:** Integration is straightforward by simply registering the listener in `spring.factories`.

## 5. Key Components
- **`MyStartUpListener` class:** Implements the `SpringApplicationRunListener` interface and captures the startup time.
- **`ready()` method:** The core method that's called after the application context is initialized.
- **`StartupData` Bean:**  An external bean responsible for storing the captured startup time.  (Its definition isn't included in the provided code).
- **Error handling:** No explicit error handling is present; a missing `StartupData` bean would lead to a `NullPointerException`.

## 6. Dependencies

### 6.1 Core Language Features
- Java 8+ features such as `Duration`
- Basic object creation and method calls

### 6.2 External Frameworks & Libraries
- **Spring Boot:** Used for dependency injection, application context management, and the `SpringApplicationRunListener` interface.
- **Spring Framework:** Provides the underlying framework for dependency injection and application context management.

### 6.3 Internal Project Dependencies
- **`StartupData` class:**  An internal project class used to store the startup time. The code relies on the existence of this bean within the Spring context.

## 7. Potential Improvements
- **Error Handling:** Add error handling to gracefully handle the case where the `StartupData` bean is not found in the application context.  A `try-catch` block could log an error message and prevent a crash.
- **Logging:** Add logging to record when the startup time is captured and any errors that occur.
- **Configuration:** Consider making the name of the `StartupData` bean configurable to allow for greater flexibility.
- **Testing:** Add unit tests to verify that the startup time is captured correctly and stored in the `StartupData` bean.
- **Performance Enhancements:** While the code is already relatively efficient, consider using a more optimized method for measuring the startup time if performance is critical. (However, this is unlikely to be a significant factor.)