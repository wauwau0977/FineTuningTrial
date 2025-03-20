You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This code defines a JPA repository interface (`HeatPumpRepository`) for interacting with a database containing heat pump data. It provides several methods for querying and aggregating this data, allowing for analysis of heat pump performance and statistics. The queries are complex SQL statements utilizing window functions and subqueries to derive meaningful insights from the raw data. The primary function is to retrieve and process heat pump data for reporting and analytical purposes.

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/dao/HeatPumpRepository.java
- **Class Name(s):** `HeatPumpRepository`

## 3. Functional Requirements

- **Primary Operations:**
    - Retrieve boiler stats by hour.
    - Retrieve boiler stats by day of the week.
    - Retrieve sole in/out temperature difference statistics while the compressor is running.

- **User Inputs & Outputs:**
    - **Inputs:** `Date measurement_date_start`, `Date measurement_date_end`, `int group_every_nth_second`, `int maxRows`
    - **Outputs:** `List<BoilerStatsByHour>`, `List<BoilerStatsByDayOfWeek>`, `List<SoleInOutDeltaInOperationStats>`

- **Workflow/Logic:**
    - Each method corresponds to a specific SQL query.
    - The SQL queries perform data filtering, aggregation, and calculation.
    - Window functions are used to calculate moving averages, totals, and ranks.
    - Subqueries are used to break down complex calculations into smaller steps.
    - Data is filtered based on the provided date range.

- **External Interactions:**
    - Database interaction via JPA.
    - The queries assume a specific database schema with tables like `heat_pump`.

- **Edge Cases Handling:**
    - The queries handle potential edge cases such as missing data or invalid date ranges through the database query logic itself (e.g. `WHERE` clauses).
    - Some queries filter out initial startup phases and periods shortly before compressor shutdown.
    -  Error handling is delegated to the database and JPA implementation. No explicit try/catch blocks are present in the repository interface.

## 4. Non-Functional Requirements

- **Performance:** The performance depends on the database schema, indexing, and query optimization. Complex queries may require significant database resources.
- **Scalability:**  Scalability depends on the underlying database's ability to handle increasing data volumes and query load.
- **Security:** Security is dependent on the overall application and database security measures. No explicit security measures are present in the repository itself.
- **Maintainability:** The SQL queries are complex and can be difficult to understand and maintain. Refactoring could improve readability.
- **Reliability & Availability:** Reliability and availability depend on the database system.
- **Usability:** The repository interface provides a clear API for accessing heat pump data. However, the complex SQL queries make understanding the underlying data model challenging.

## 5. Key Components

- **Functions:**
    - `getBoilerStatsByHour(Date measurement_date_start, Date measurement_date_end)`: Retrieves boiler stats aggregated by hour.
    - `getBoilerStatsByDayOfWeek(Date measurement_date_start, Date measurement_date_end)`: Retrieves boiler stats aggregated by day of the week.
    - `getSoleDeltaInOperationStats(int group_every_nth_second, int maxRows)`: Retrieves sole in/out temperature difference statistics.
- **Important logic flows:**
    - Each query follows a specific logic flow: Filtering, Aggregation, Calculation.
    - Window functions are used extensively to calculate moving averages and totals.
- **Error handling:** Implicit error handling through the JPA provider and database.
- **Classes:** Single interface `HeatPumpRepository`. No subclasses.
- **Modules:** Part of the `thserver` module within the `Warmduscher` project.

## 6. Dependencies

### 6.1 Core Language Features

- Java Persistence API (JPA)
- `java.util.Date`
- `java.util.List`

### 6.2 External Frameworks & Libraries

- **Spring Data JPA:**  Used for defining the repository interface and interacting with the database.  (Implicit dependency based on interface definition)

### 6.3 Internal Project Dependencies

- None explicitly declared in the code snippet. Dependencies are managed within the `thserver` project's build configuration.

## 7. Potential Improvements

- **Performance Enhanecements:**
    - Optimize SQL queries by adding appropriate indexes to the database tables.
    - Consider using database-specific optimization techniques.
    - Cache frequently accessed data.
- **Code Readability:**
    - Refactor complex SQL queries into smaller, more manageable subqueries or stored procedures.
    - Add comments to explain the logic behind each query.
    - Consider using a query builder to generate the SQL queries programmatically.
- **Security Improvements:**
    - Implement input validation to prevent SQL injection attacks.
    - Sanitize all user inputs before using them in SQL queries.
- **Scalability Considerations:**
    - Use database partitioning to distribute data across multiple servers.
    - Implement connection pooling to improve database performance.
    - Consider using a distributed caching system to handle large volumes of data.