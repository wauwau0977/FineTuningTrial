You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This code defines a REST controller (`HeatPumpDataService`) responsible for providing historical and current data related to a heat pump system. It fetches data from a database through a `HeatPumpRepository` and, in one case, through a `HeatingDataReadService`. The controller offers endpoints to retrieve current readings, historical data within specified date ranges, aggregated statistics (hourly, daily, delta), and allows scanning of device registers. 

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/heating/HeatPumpDataService.java
- **Class Name(s):** `HeatPumpDataService`

## 3. Functional Requirements

- **Primary Operations**:
    - Retrieve the last heat pump entry.
    - Retrieve historical heat pump data up to a specified number of rows.
    - Retrieve heat pump statistics between specified start and end dates, limited by either a fixed time interval or a maximum number of rows.
    - Retrieve hourly boiler statistics within a specified date range.
    - Retrieve daily boiler statistics within a specified date range.
    - Retrieve sole delta in operation statistics within a specified date range.
    - Scan device registers to retrieve their current values.
- **User Inputs & Outputs**:
    - **`/current`**: No inputs. Output: Last `HeatPumpEntity`.
    - **`/lastValues`**: Input: `maxRows` (integer, optional, default=1500). Output: List of `HeatPumpEntity` up to `maxRows`.
    - **`/getBetweenDates`**: Inputs: `start` (Date), `end` (Date), `maxRows` (integer, optional, default=-1), `groupEveryNthSecond` (integer, optional, default=-1). Output: List of `HeatPumpStatisticsEntity`.
    - **`/getBoilerStatsByHour`**: Inputs: `start` (Date), `end` (Date). Output: List of `BoilerStatsByHour`.
    - **`/getBoilerStatsByDayOfWeek`**: Inputs: `start` (Date), `end` (Date). Output: List of `BoilerStatsByDayOfWeek`.
    - **`/getSoleDeltaInOperationStats`**: Inputs: `start` (Date), `end` (Date), `maxRows` (integer, optional, default=-1), `groupEveryNthSecond` (integer, optional, default=-1). Output: List of `SoleInOutDeltaInOperationStats`.
    - **`/scanRegisters`**: Input: `maxRegister` (integer, optional, default=510). Output: List of Strings representing register values.
- **Workflow/Logic**:
    - Each endpoint primarily delegates data retrieval to the appropriate method in `HeatPumpRepository` or `HeatingDataReadService`.
    - `/getBetweenDates` enforces a mutual exclusion rule - either `maxRows` or `groupEveryNthSecond` can be specified, but not both. At least one must be specified.
- **External Interactions**:
    - Database interaction through `HeatPumpRepository` (fetching `HeatPumpEntity`, `HeatPumpStatisticsEntity`, `BoilerStatsByHour`, `BoilerStatsByDayOfWeek`, `SoleInOutDeltaInOperationStats`).
    - Interaction with `HeatingDataReadService` to scan device registers.
- **Edge Cases Handling**:
    - `/getBetweenDates`: Throws a `ThException` if both `maxRows` and `groupEveryNthSecond` are provided, or if neither is provided.
    - Database queries will handle empty result sets gracefully (returning empty lists).
    - Date format is assumed to be handled by the framework (Spring) and defined in the application.yml configuration file.
    - Invalid input dates might cause database errors depending on the database configuration.

## 4. Non-Functional Requirements

- **Performance**: Response times should be acceptable for a web application (under 2 seconds for most queries).  Performance of database queries needs to be monitored and optimized as data volume grows.
- **Scalability**: The system should be able to handle a growing number of heat pump devices and a larger volume of historical data. Database indexing and caching are important considerations.
- **Security**: Access to the endpoints should be secured with appropriate authentication and authorization mechanisms. Data transmitted over the network should be encrypted (HTTPS).
- **Maintainability**: Code should be well-documented, modular, and follow coding best practices.
- **Reliability & Availability**: The system should be designed to minimize downtime and ensure data integrity.
- **Usability**: The API should be well-defined and easy to understand for consumers.
- **Compliance**: Data handling should comply with relevant privacy regulations.

## 5. Key Components

- **`HeatPumpDataService` Class**:  The main controller class handling incoming requests and delegating to data access layers.
- **`HeatPumpRepository`**:  Interface or implementation providing access to heat pump data in the database.
- **`HeatingDataReadService`**: Interface/Implementation responsible for reading raw data from heat pump registers.
- **Functions:**
    - `getCurrent()`: Retrieves the last heat pump entry.
    - `lastValues()`: Retrieves the last n heat pump entries.
    - `getBetweenDates()`: Retrieves heat pump statistics within a date range, limited by rows or time interval.
    - `getBoilerStatsByHour()`: Retrieves hourly boiler statistics.
    - `getBoilerStatsByDayOfWeek()`: Retrieves daily boiler statistics.
    - `getSoleDeltaInOperationStats()`: Retrieves sole delta in operation statistics.
    - `scanRegisters()`: Scans and retrieves values from device registers.
- **Error Handling**:  `ThException` is used for specific business logic errors.  Database errors and other exceptions should be handled appropriately with logging.
- **Classes**: No subclasses are defined.
- **Modules**: The code appears to be part of a larger module responsible for handling heating data.

## 6. Dependencies

### 6.1 Core Language Features

- Java 8+
- Data structures (Lists, Dates)
- Standard exception handling

### 6.2 External Frameworks & Libraries

- **Spring Framework**: Used for dependency injection, REST controller handling, and request mapping.
- **Spring Data JPA**: Facilitates database interaction.

### 6.3 Internal Project Dependencies

- `com.x8ing.thsensor.thserver.db.dao.HeatPumpRepository`: Interface or implementation for accessing heat pump data.
- `com.x8ing.thsensor.thserver.db.entity.*`: Data entities representing heat pump data (e.g., `HeatPumpEntity`, `HeatPumpStatisticsEntity`).
- `com.x8ing.thsensor.thserver.device.service.HeatingDataReadService`: Service for reading raw data from the heat pump device.
- `com.x8ing.thsensor.thserver.utils.ThException`: Custom exception class.

## 7. Potential Improvements

- **Performance Enhancements**:
    - Database query optimization: Review and optimize database queries, especially for `/getBetweenDates`, with appropriate indexing.
    - Caching: Implement caching mechanisms to reduce database load for frequently accessed data.
- **Code Readability**:
    - Extract complex logic into separate helper functions or classes.
    - Add more comprehensive Javadoc comments.
- **Security Improvements**:
    - Implement input validation to prevent injection attacks.
    - Secure access to the endpoints with authentication and authorization.
- **Scalability Considerations**:
    - Consider using a database sharding strategy to distribute the load across multiple database servers.
    - Explore using a message queue to offload long-running tasks.
    - Monitor database performance and scale resources as needed.