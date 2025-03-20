You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This code defines a Spring Data JPA repository interface `MeteoSwissRepository` for interacting with a database table named `meteo_swiss`.  The repository provides standard CRUD operations for `MeteoSwissEntity` objects, as well as a custom query to retrieve the last `maxRows` entries for a given `stationId`, ordered by `temperature_measure_date` in descending order. This is likely part of a system collecting and storing weather data from MeteoSwiss for use in a heat pump control or monitoring application ('Warmduscher').

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/dao/meteoswiss/MeteoSwissRepository.java
- **Class Name(s):** `MeteoSwissRepository`

## 3. Functional Requirements

- **Primary Operations**:
    - Perform standard Create, Read, Update, and Delete (CRUD) operations on `MeteoSwissEntity` objects.
    - Retrieve the last N weather entries for a specific station.
- **User Inputs & Outputs**:
    - **Inputs**: `stationId` (String), `maxRows` (Integer), `MeteoSwissEntity` objects for create/update, ID for delete.
    - **Outputs**: `List<MeteoSwissEntity>` (for `getLastEntries`), `MeteoSwissEntity` (for read/update operations), success/failure indicators for CRUD operations.
- **Workflow/Logic**:
    - CRUD operations follow standard JPA repository behavior.
    - `getLastEntries` executes a native SQL query to fetch the last entries based on `stationId` and `maxRows`. Results are ordered by `temperature_measure_date` in descending order.
- **External Interactions**:
    - **Database Interaction**: Interacts directly with a relational database to store and retrieve `MeteoSwissEntity` data. The SQL query is executed against the database.
- **Edge Cases Handling**:
    - `stationId` being null or empty: The query might return unexpected results or throw an exception (depending on the database configuration and query execution).
    - `maxRows` being negative or zero: The query might return an empty list or throw an exception.
    - Database connection failure: Standard JPA error handling should be in place to handle database connectivity issues.

## 4. Non-Functional Requirements

- **Performance**: `getLastEntries` should execute efficiently for reasonable values of `maxRows`. Performance depends heavily on database indexing.
- **Scalability**: The repository's performance should scale adequately with the number of `MeteoSwissEntity` records in the database, especially considering the expected load and frequency of `getLastEntries` calls.
- **Security**:  The application should protect against SQL injection vulnerabilities in the native query, potentially by using parameterized queries if feasible.  Database access credentials must be secured.
- **Maintainability**: The interface is relatively simple and should be easy to maintain.
- **Reliability & Availability**:  The repository relies on the reliability of the underlying database. Proper database backups and recovery mechanisms are essential.
- **Usability**:  The interface is straightforward to use for other parts of the application.

## 5. Key Components

- **Functions**:
    - `getLastEntries(String stationId, int maxRows)`: Retrieves the last N weather entries for a given station ID, ordered by date.
    - Standard JPA repository methods (`save`, `findById`, `delete`, etc.):  Provide the CRUD functionalities.
- **Important logic flows**:
    - The `getLastEntries` query directly fetches the requested data from the database.
- **Error handling**: Standard JPA exception handling should be implemented in the calling service/component.
- **Classes**:  `MeteoSwissRepository` is an interface extending `CrudRepository`.
- **Modules**:  Part of the data access layer (DAO) of the application.

## 6. Dependencies

### 6.1 Core Language Features
- Data structures (Lists)
- String manipulation

### 6.2 External Frameworks & Libraries
- **Spring Data JPA**: Provides the `CrudRepository` interface and handles database interactions.
- **Spring Framework**: Provides the dependency injection and other core functionalities.

### 6.3 Internal Project Dependencies
- `com.x8ing.thsensor.thserver.db.entity.MeteoSwissEntity`:  The entity class representing the data stored in the `meteo_swiss` table.

## 7. Potential Improvements

- **Performance Enhancements**:
    - Add an index on `meteo_swiss.station_id` and `meteo_swiss.temperature_measure_date` to improve the performance of the `getLastEntries` query.
- **Code Readability**:  The code is already quite readable due to its simplicity.
- **Security Improvements**: Consider using Spring's named parameter support to avoid potential SQL injection issues.  While unlikely with simple integer parameters, it’s a good practice.
- **Scalability Considerations**:
    - If the `meteo_swiss` table grows very large, consider partitioning the table based on `station_id` or `temperature_measure_date` to improve query performance.
    - Implement caching to store frequently accessed data in memory, reducing the load on the database.