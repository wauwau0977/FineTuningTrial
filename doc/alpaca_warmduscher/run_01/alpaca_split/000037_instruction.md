You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This class, `HeatingDataPoller`, is a scheduled service responsible for periodically reading heating data from an external source (either a ModBus device or a mock service) using `HeatingDataReadService`, and persisting this data to a database using `HeatPumpRepository`. It logs the execution time and any errors encountered during the process.

## 2. File Information

- **File Location:** `Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/device/service/HeatingDataPoller.java`
- **Class Name(s):** `HeatingDataPoller`

## 3. Functional Requirements

- **Primary Operations**:  Periodically poll heating data and persist it.
- **User Inputs & Outputs**: This service doesn't have direct user inputs or outputs. It interacts with other services and the database.
- **Workflow/Logic**:
    1. The `@Scheduled` annotation triggers the `pollData()` method at a defined interval.
    2. `pollData()` calls `heatingDataReadService.getData()` to retrieve heating data.
    3. If `heatingDataReadService.getData()` succeeds, it returns a `HeatPumpEntity`.
    4. The `HeatPumpEntity` is then saved to the database via `heatPumpRepository.save()`.
    5.  Execution time is logged.
    6.  If any exception occurs during data retrieval, it's logged as an error and re-thrown as a `RuntimeException`.
- **External Interactions**:
    - Interacts with `HeatingDataReadService` to read data.
    - Interacts with `HeatPumpRepository` (a database repository) to persist data.
- **Edge Cases Handling**:
    - If `heatingDataReadService.getData()` throws an exception (e.g., network error, invalid data), the exception is caught, logged with an error message, and re-thrown as a `RuntimeException`. This ensures that the error is propagated and handled at a higher level.

## 4. Non-Functional Requirements

- **Performance**:  The polling interval is configurable (defaulting to 60 seconds). Execution time is logged for monitoring.  The execution should be fast enough to not significantly impact other services, ideally completing within a few seconds.
- **Scalability**: The polling interval can be adjusted to accommodate increased load.  If the database becomes a bottleneck, consider optimizing database queries or using a caching mechanism.
- **Security**:  Data security depends on the implementation of `HeatingDataReadService` and the database configuration. Sensitive data should be encrypted in transit and at rest.
- **Maintainability**: The class is relatively simple and well-structured.  Dependencies are injected via the constructor, making it easier to test and modify.
- **Reliability & Availability**: The service relies on the availability of `HeatingDataReadService` and the database. Proper error handling and monitoring are crucial.
- **Usability**: The service is designed for internal use and doesn't have a direct user interface.  Configuration is done via application properties.

## 5. Key Components

- **`pollData()` Function**: The main function that orchestrates the data polling and persistence process.
- **`HeatingDataReadService`**: An interface/class responsible for retrieving heating data from an external source.
- **`HeatPumpRepository`**: A Spring Data repository interface for interacting with the database.
- **Error Handling**:  Exception handling within `pollData()` ensures that errors are logged and propagated.
- **Scheduled Task**:  The `@Scheduled` annotation triggers the task at a configurable interval.
- **Classes:** No subclasses are defined.
- **Modules:** Part of the `thserver` module responsible for device service functionalities.

## 6. Dependencies

### 6.1 Core Language Features

- Data structures (Objects)
- Logging using `java.util.logging` or similar.

### 6.2 External Frameworks & Libraries

- **Spring Framework**: Dependency Injection (DI), Scheduled Tasks (`@Scheduled`).
- **SLF4J**: Logging facade.

### 6.3 Internal Project Dependencies

- **`com.x8ing.thsensor.thserver.db.dao.HeatPumpRepository`**:  Interface for database interactions.
- **`com.x8ing.thsensor.thserver.device.service.HeatingDataReadService`**: Interface for reading heating data.

## 7. Potential Improvements

- **Performance Enhancements**:  If `heatingDataReadService.getData()` is slow, consider caching the data or implementing asynchronous data retrieval.
- **Code Readability**: The code is already fairly readable.
- **Security Improvements**:  Ensure that any sensitive data transmitted between services is encrypted. Implement appropriate authentication and authorization mechanisms.
- **Scalability Considerations**:  Consider using a message queue to decouple the data polling process from the database persistence process. This would allow the system to handle a larger volume of data. Implement a retry mechanism in case of database connection failures.
- **Monitoring**: Add more detailed monitoring metrics, such as the number of successful polls, the number of errors, and the average execution time.  Consider using a dedicated monitoring system.