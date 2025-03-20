You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This code defines a REST controller (`HeatPumpDataService`) that provides access to heat pump data stored in a database. The service offers endpoints to retrieve current data, historical data, and aggregated statistics (hourly, daily, delta stats). It also includes functionality to scan heating registers via an external service. The primary goal is to provide data for monitoring and analysis of heat pump performance.

## 2. File Information

- **File Location:** `Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/heating/HeatPumpDataService.java`
- **Class Name(s):** `HeatPumpDataService`

## 3. Functional Requirements

- **Primary Operations:**
    - Retrieve current heat pump data.
    - Retrieve historical heat pump data within a specified range.
    - Retrieve heat pump statistics aggregated by hour.
    - Retrieve heat pump statistics aggregated by day of the week.
    - Retrieve sole in/out delta stats.
    - Scan heating registers.

- **User Inputs & Outputs:**
    - `/current`: No input, output: `HeatPumpEntity` (or null if no data found).
    - `/lastValues`: Input: `maxRows` (int, optional, default 1500), output: `List<HeatPumpEntity>`.
    - `/getBetweenDates`: Input: `start` (Date), `end` (Date), `maxRows` (int, optional, default -1), `groupEveryNthSecond` (int, optional, default -1), output: `List<HeatPumpStatisticsEntity>`.
    - `/getBoilerStatsByHour`: Input: `start` (Date), `end` (Date), output: `List<BoilerStatsByHour>`.
    - `/getBoilerStatsByDayOfWeek`: Input: `start` (Date), `end` (Date), output: `List<BoilerStatsByDayOfWeek>`.
    - `/getSoleDeltaInOperationStats`: Input: `start` (Date), `end` (Date), `maxRows` (int, optional, default -1), `groupEveryNthSecond` (int, optional, default -1), output: `List<SoleInOutDeltaInOperationStats>`.
    - `/scanRegisters`: Input: `maxRegister` (int, optional, default 510), output: `List<String>`.

- **Workflow/Logic:**
    - Each endpoint translates the request parameters into a database query through the `HeatPumpRepository`.
    - The `HeatPumpRepository` handles the data retrieval process.
    -  For `/getBetweenDates`, validation logic prevents passing both `maxRows` and `groupEveryNthSecond` or neither.
    -  `/scanRegisters` calls the external `HeatingDataReadService` to scan registers.

- **External Interactions:**
    - Interacts with a database via `HeatPumpRepository`.
    - Calls `HeatingDataReadService` for register scanning.

- **Edge Cases Handling:**
    - `/current`: Returns null if no data is found.
    - `/getBetweenDates`:  Throws `ThException` if invalid parameter combinations are provided (both or neither of `maxRows` and `groupEveryNthSecond`).
    - Database errors should be handled gracefully, potentially returning appropriate error responses or logging errors.
    - `HeatingDataReadService` errors need proper handling, perhaps by catching exceptions and returning an empty list or an error message.

## 4. Non-Functional Requirements

- **Performance:**
    - Response times for all endpoints should be acceptable (e.g., under 2 seconds for typical data volumes). Database query performance is critical.
- **Scalability:** The system should be able to handle an increasing number of requests and data volume without significant performance degradation.
- **Security:** Authentication and authorization mechanisms are assumed to be handled elsewhere (e.g., by a security filter).  Data access should be restricted to authorized users.
- **Maintainability:** The code is relatively well-structured with clear separation of concerns. Further modularization could improve maintainability.
- **Reliability & Availability:** Database connectivity and external service calls need to be robust. Implement retry mechanisms and error handling to improve reliability.
- **Usability:** The API is straightforward and easy to understand.  Documentation is crucial for usability.

## 5. Key Components

- **Functions:**
    - `getCurrent()`: Retrieves the latest heat pump data.
    - `lastValues()`: Retrieves a specified number of historical data points.
    - `getBetweenDates()`: Retrieves data within a date range, with options for limiting by row count or time interval.
    - `getBoilerStatsByHour()`: Retrieves hourly statistics.
    - `getBoilerStatsByDayOfWeek()`: Retrieves daily statistics.
    - `getSoleDeltaInOperationStats()`: Retrieves sole in/out delta stats.
    - `scanRegisters()`: Scans heating registers via an external service.

- **Important Logic Flows:**
    - Each endpoint follows a similar flow: receive request, validate parameters, query the database (or call external service), return results.
    - `/getBetweenDates` has validation logic to ensure valid parameter combinations.

- **Error Handling:**
    - `ThException` is used for custom error handling within `/getBetweenDates`.
    - General database and external service errors need to be handled appropriately.

- **Classes:**
    - No subclasses defined.

- **Modules:**
    -  The code is organized into a single controller class.

## 6. Dependencies

### 6.1 Core Language Features

- Data structures: Lists, Dates
- File handling: Not used directly in this class
- Concurrency/threading: Not used directly in this class

### 6.2 External Frameworks & Libraries

- **Spring Framework:** Used for dependency injection, request mapping, and REST controller functionality.
- **Spring Data JPA:** Used for database interaction via `HeatPumpRepository`.

### 6.3 Internal Project Dependencies

- `com.x8ing.thsensor.thserver.db.dao.HeatPumpRepository`: Interface for accessing heat pump data in the database.
- `com.x8ing.thsensor.thserver.db.entity.*`: Data entities representing heat pump data.
- `com.x8ing.thsensor.thserver.device.service.HeatingDataReadService`: Service for scanning heating registers.
- `com.x8ing.thsensor.thserver.utils.ThException`: Custom exception class.

## 7. Potential Improvements

- **Performance Enhancements:**
    - Optimize database queries (e.g., using indexes, appropriate data types).
    - Consider caching frequently accessed data.
- **Code Readability:**
    - Extract complex logic into separate helper functions or classes.
- **Security Improvements:**
    - Implement proper input validation to prevent injection attacks.
    - Ensure secure database connection configuration.
- **Scalability Considerations:**
    - Consider using a distributed caching system for improved performance and scalability.
    - Explore asynchronous processing for long-running operations.
- **Error Handling:**
    - Implement more robust error handling and logging throughout the code.  Return meaningful error responses to the client.
- **Testing:** Implement unit and integration tests to ensure code correctness and reliability.