You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

The `MeteoDataPoller` class is a Spring-managed component responsible for periodically polling weather data from an external `MeteoDataService`, persisting it into the database using `MeteoSwissRepository`, and logging the process. It uses a scheduled task to retrieve and save weather data at a configurable interval.

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/data/meteoswiss/MeteoDataPoller.java
- **Class Name(s):** `MeteoDataPoller`

## 3. Functional Requirements

- **Primary Operations:** Poll weather data from MeteoSwiss, save to database.
- **User Inputs & Outputs:**  This class operates autonomously and doesn’t have direct user inputs.  Output is primarily logging information and the persistent storage of `MeteoSwissEntity` objects in the database.
- **Workflow/Logic:**
    1.  The `MeteoDataPoller` is initialized, which in turn calls the `init()` method of the `MeteoDataService`.
    2.  A scheduled task is triggered at a defined interval (configurable via `thserver.meteoSwiss.pollingInterval`).
    3.  The `pollData()` method is executed:
        a.  Starts a timer to measure execution time.
        b.  Calls the `getData()` method of `MeteoDataService` to retrieve a list of `MeteoSwissEntity` objects.
        c.  Saves the retrieved entities to the database using `MeteoSwissRepository.saveAll()`.
        d. Logs the execution time.
        e. If any exception occurs, logs the error and re-throws it as a `RuntimeException`.
- **External Interactions:**
    - **`MeteoDataService`**: Calls the `getData()` method to retrieve weather data.
    - **`MeteoSwissRepository`**:  Uses `saveAll()` to persist data into the database.
- **Edge Cases Handling:**
    - If `MeteoDataService.getData()` or `MeteoSwissRepository.saveAll()` throws an exception, the error is logged, and a `RuntimeException` is thrown.  This ensures that failures are visible and potentially handled by a higher-level error handling mechanism.

## 4. Non-Functional Requirements

- **Performance:**  The polling interval is configurable.  The execution time is logged, which can be used for performance monitoring. The goal is to complete data fetching and saving within the polling interval.
- **Scalability:**  The system's scalability depends on the `MeteoDataService` and `MeteoSwissRepository` implementations.  If the `MeteoDataService` can efficiently handle increased load and the database can handle increased writes, the system can scale.
- **Security:** Security considerations depend on how `MeteoDataService` retrieves data and how the database is secured. No specific security measures are implemented within this class.
- **Maintainability:** The class is relatively simple and well-structured. Dependency injection makes it easier to test and modify.
- **Reliability & Availability:** The error handling (logging and re-throwing exceptions) contributes to reliability.  Availability depends on the underlying `MeteoDataService` and database.
- **Usability:**  The class is designed for automated background operation and doesn’t have a direct user interface. Configuration is handled via Spring properties.
- **Compliance:** No specific compliance requirements are outlined.

## 5. Key Components

- **`MeteoDataPoller` Class:** The main class responsible for polling and persisting data.
- **`pollData()` Function:**  Performs the core logic of fetching data, saving it to the database, and logging execution time.
- **Error Handling:**  `try-catch` block around data fetching and saving, logging errors and re-throwing exceptions.
- **`init()` method in MeteoDataService**: Initialises the MeteoDataService.

## 6. Dependencies

### 6.1 Core Language Features

- **Data structures:** Lists (used for storing `MeteoSwissEntity` objects).
- **Logging:** Using `org.slf4j.Logger` and `org.slf4j.LoggerFactory` for logging.
- **Exception Handling:** `try-catch` blocks for error handling.

### 6.2 External Frameworks & Libraries

- **Spring Framework**: `@Component` and `@Scheduled` annotations, dependency injection.
- **SLF4J**: Logging framework.

### 6.3 Internal Project Dependencies

- **`com.x8ing.thsensor.thserver.db.dao.meteoswiss.MeteoSwissRepository`**:  Repository interface for database access.
- **`com.x8ing.thsensor.thserver.db.entity.meteoswiss.MeteoSwissEntity`**: Data entity representing weather data.
- **`com.x8ing.thsensor.thserver.data.meteoswiss.MeteoDataService`**: Service interface for retrieving weather data.

## 7. Potential Improvements

- **Performance Enhancements:** Monitor the execution time of `pollData()` and optimize the `MeteoDataService` and `MeteoSwissRepository` if necessary.  Consider asynchronous data saving to improve responsiveness.
- **Code Readability:** The code is already fairly readable.
- **Security Improvements:** Review the security of the `MeteoDataService` and database connection.
- **Scalability Considerations:**  If the amount of data increases significantly, consider using a message queue (e.g., Kafka, RabbitMQ) to handle data ingestion and processing asynchronously.  Implement pagination if `MeteoDataService` returns a very large dataset.
- **Error Handling:** Consider adding a retry mechanism for transient errors in `MeteoDataService`.  Implement more specific exception handling instead of catching `Throwable` for better error management.