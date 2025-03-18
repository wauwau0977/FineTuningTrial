You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This interface, `MeteoSwissStatsRepository`, provides database access for retrieving and aggregating historical weather data from the `meteo_swiss` table. It utilizes Spring Data JPA to define queries for calculating various statistics (average, min, max) for temperature and wind gust speed within specified date ranges and grouping intervals. The primary purpose is to generate summarized weather data for analysis and reporting.

## 2. File Information

- **File Location:** `Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/dao/meteoswiss/MeteoSwissStatsRepository.java`
- **Class Name(s):** `MeteoSwissStatsRepository`

## 3. Functional Requirements

- **Primary Operations:**
    - Retrieve aggregated weather statistics (temperature, wind gust) within a specified date range.
    - Retrieve aggregated weather statistics grouped by fixed time intervals.
    - Retrieve aggregated weather statistics with a limit on the number of rows.
- **User Inputs & Outputs:**
    - **Inputs:**
        - `measurement_date_start`: Starting date for the data retrieval.
        - `measurement_date_end`: Ending date for the data retrieval.
        - `maxRows`: Maximum number of rows to return.
        - `groupEveryNthSecond`: Group data into intervals of specified seconds.
    - **Outputs:** A `List` of `MeteoSwissStatisticsEntity` objects, each containing the calculated statistics for a specific station and time interval.
- **Workflow/Logic:**
    1. The repository interface defines two main query methods:
        - `findBetweenDatesLimitByRowsStats`:  Retrieves statistics within a date range and limits the results by the specified number of rows. Uses `ntile` to group the results.
        - `findBetweenDatesLimitByFixedIntervalStats`: Retrieves statistics within a date range, grouping the data into fixed time intervals defined by `groupEveryNthSecond`.
    2. The queries perform aggregation (avg, min, max) on temperature and wind gust speed.
    3. The queries also retrieve the minimum and maximum dates for measurements.
    4. The results are mapped to `MeteoSwissStatisticsEntity` objects.
- **External Interactions:**
    - Database interaction: Executes SQL queries against the `meteo_swiss` table.
- **Edge Cases Handling:**
    - **Invalid Date Range:** The database queries should handle cases where `measurement_date_start` is after `measurement_date_end`. (Likely handled by the database itself.)
    - **Empty Date Range:** If the date range returns no data, the query should return an empty list.
    - **Database Connection Failure:** Spring Data JPA handles connection failures and throws appropriate exceptions.
    - **`maxRows` is 0 or negative:** The behavior is not explicitly defined, but a reasonable approach would be to return an empty list or throw an exception.

## 4. Non-Functional Requirements

- **Performance:** Queries should execute efficiently, especially considering potentially large datasets.  Indexing the `temperature_measure_date` column in the `meteo_swiss` table is critical.
- **Scalability:** The repository should be able to handle increasing data volumes and query load. Consider database partitioning or caching mechanisms for improved scalability.
- **Security:**  The database connection should be secured with appropriate authentication and authorization mechanisms.
- **Maintainability:** The code is relatively straightforward, leveraging Spring Data JPA for database interactions. Consistent coding style and comments improve maintainability.
- **Reliability & Availability:** The application relies on the reliability and availability of the database server. 
- **Usability:**  The interface provides a clear and concise API for accessing weather statistics.
- **Compliance:**  The code should comply with any relevant data privacy regulations.

## 5. Key Components

- **`MeteoSwissStatsRepository` Interface:** Defines the methods for retrieving and aggregating weather data.
- **`findBetweenDatesLimitByRowsStats`:** Query method that retrieves statistics within a date range and limits the results by the specified number of rows.
- **`findBetweenDatesLimitByFixedIntervalStats`:** Query method that retrieves statistics within a date range, grouping the data into fixed time intervals.
- **`MeteoSwissStatisticsEntity`:** Data transfer object representing the aggregated weather statistics.
- **SQL Queries:** The native SQL queries defined within the methods are the core logic for data retrieval and aggregation.

## 6. Dependencies

### 6.1 Core Language Features

- Java 8 or higher
- Standard Java Collections Framework (Lists, Dates)

### 6.2 External Frameworks & Libraries

- **Spring Data JPA:** Used for database interaction and query definition.
- **Spring Framework:** Provides dependency injection and other core functionalities.

### 6.3 Internal Project Dependencies

- `com.x8ing.thsensor.thserver.db.entity.meteoswiss.MeteoSwissStatisticsEntity`: Data transfer object for the retrieved statistics.

## 7. Potential Improvements

- **Performance Enhanecments:**
    - Analyze query execution plans to identify potential bottlenecks.
    - Ensure proper indexing of the `temperature_measure_date` column in the `meteo_swiss` table.
    - Consider caching frequently accessed data.
- **Code Readability:**
    - The SQL queries are quite long. Breaking them down into smaller, named subqueries or using common table expressions (CTEs) could improve readability.
- **Security Improvements:**
    - Validate input parameters (dates, maxRows) to prevent potential SQL injection attacks.
- **Scalability Considerations:**
    - Consider database partitioning or sharding to handle very large datasets.
    - Implement a caching layer to reduce database load.
    - Use connection pooling to improve database connection performance.
- **Error Handling:** Implement more specific error handling and logging for database connection failures and query errors.