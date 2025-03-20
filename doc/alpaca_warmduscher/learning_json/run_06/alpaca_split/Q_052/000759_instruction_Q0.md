You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below```
# IT Specification

## 1. Summary

This interface, `HeatPumpRepository`, provides data access operations for `HeatPumpEntity` objects, which represent heat pump measurements. It offers methods for retrieving the latest and historical data, as well as aggregated statistics calculated over different time intervals and groupings. The repository leverages Spring Data JPA for database interaction, utilizing native SQL queries for complex calculations and aggregations.

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/dao/HeatPumpRepository.java
- **Class Name(s):** `HeatPumpRepository`

## 3. Functional Requirements

- **Primary Operations:**
    - Retrieve the latest heat pump entry.
    - Retrieve historical heat pump entries (limited by a specified number of rows).
    - Calculate and retrieve aggregated heat pump statistics over a defined date range and with row limitation.
    - Calculate and retrieve heat pump statistics grouped by fixed time intervals.
    - Calculate and retrieve daily/hourly heat pump statistics with boiler temperature deltas.

- **User Inputs & Outputs:**
    - **Inputs:** Date ranges (start and end dates), maximum number of rows to retrieve, grouping intervals (in seconds), and potentially a maximum row limit for the stats queries.
    - **Outputs:**  `HeatPumpEntity` objects, lists of `HeatPumpEntity` objects, and lists of `HeatPumpStatisticsEntity` objects containing aggregated statistical data.

- **Workflow/Logic:**
    - The repository utilizes Spring Data JPA's `CrudRepository` interface for basic CRUD operations.
    -  Complex queries are implemented using native SQL queries for performance and flexibility.
    - Aggregation queries involve complex calculations such as averages, minimums, maximums, sums, and differences over time windows.
    - Date and time calculations are used for grouping data into time intervals and calculating deltas.

- **External Interactions:**
    - **Database:** Interacts with the database to retrieve and store `HeatPumpEntity` data.  Uses native SQL queries.

- **Edge Cases Handling:**
    - **Empty Date Range:** Queries should handle empty date ranges gracefully, returning empty lists or appropriate default values.
    - **Invalid Date Format:** The application should handle invalid date formats and provide meaningful error messages.
    - **No Data Found:**  Queries should handle cases where no data is found within the specified date range or criteria, returning empty lists.
    - **Large Date Ranges:**  Queries with very large date ranges should be optimized for performance or consider pagination.
    - **Database Connection Errors:** Should handle database connection errors with appropriate logging and error handling mechanisms.

## 4. Non-Functional Requirements

- **Performance:**
    - Queries should be optimized for performance to ensure fast response times, especially for aggregation queries.
    - The use of native SQL allows for tuning and optimization specific to the database system.
- **Scalability:**
    - The repository should be designed to handle increasing data volumes and user load.  Consider database indexing and query optimization.
- **Security:**
    -  Data access should be secured through appropriate authentication and authorization mechanisms.
- **Maintainability:**
    - The code should be well-documented and follow coding best practices to ensure easy maintenance and modification.
- **Reliability & Availability:**
    -  The repository should be reliable and available, with appropriate error handling and logging mechanisms.
- **Usability:**
    - The interface should be easy to use and integrate into other parts of the application.
- **Compliance:**
    - The application should comply with relevant data privacy regulations and security standards.

## 5. Key Components

- **Functions:**
    - `getLastEntry()`: Retrieves the most recent heat pump entry.
    - `getLastEntries(int maxRows)`: Retrieves the last `maxRows` heat pump entries.
    - `findBetweenDatesLimitByRowsStats(Date measurement_date_start, Date measurement_date_end, int maxRows)`: Retrieves aggregated heat pump statistics within a date range, limited by the number of rows.
    - `findBetweenDatesLimitByFixedIntervalStats(Date measurement_date_start, Date measurement_date_end, int groupEveryNthSecon)`: Retrieves aggregated statistics grouped by fixed time intervals.
    -  Numerous other methods involving various SQL queries that calculate stats over various time ranges.

- **Important logic flows:**
    - All queries perform database reads using Spring Data JPA.
    - Aggregation queries involve calculating various statistical measures (average, min, max, sum) using SQL functions.
    - Date and time calculations are used to group data into time intervals and calculate deltas.

- **Error handling:**
    - Database connection errors are handled by Spring Data JPA's exception handling mechanisms.
    - Invalid input parameters or data inconsistencies should be handled with appropriate error messages and logging.

- **Classes:**
    - No subclasses are defined. `HeatPumpRepository` implements the `CrudRepository` interface.

- **Modules:**
    - Spring Data JPA
    - Native SQL query definitions

## 6. Dependencies

### 6.1 Core Language Features
- Data structures (Lists, Dates)
- Standard Java libraries for date and time manipulation.

### 6.2 External Frameworks & Libraries
- **Spring Data JPA:** Used for database interaction and repository management.
- **Native SQL:** Used extensively for complex data aggregation and calculations.

### 6.3 Internal Project Dependencies
- `com.x8ing.thsensor.thserver.db.entity.HeatPumpEntity`: The entity class representing heat pump data.
- `com.x8ing.thsensor.thserver.db.entity.HeatPumpStatisticsEntity`:  The entity class representing aggregated heat pump statistics.

## 7. Potential Improvements

- **Performance Enhancements:**
    - Analyze query execution plans to identify bottlenecks and optimize SQL queries.
    - Implement caching mechanisms to reduce database load.
    - Consider using database indexes to speed up data retrieval.

- **Code Readability:**
    - Break down complex SQL queries into smaller, more manageable subqueries.
    - Add comments to explain the purpose and logic of complex SQL statements.

- **Security Improvements:**
    - Implement input validation to prevent SQL injection attacks.

- **Scalability Considerations:**
    - Partition the database table to improve scalability and performance.
    - Consider using a distributed caching system to handle large data volumes.
```