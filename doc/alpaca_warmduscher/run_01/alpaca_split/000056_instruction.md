You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This code defines a Spring Data JPA repository interface (`MeteoSwissRepository`) for accessing and querying data related to weather measurements from MeteoSwiss. It provides basic CRUD operations for `MeteoSwissEntity` objects and a custom query to retrieve the most recent temperature measurements for a specific station. The primary goal is to efficiently retrieve historical weather data from the `meteo_swiss` table for use within the Warmduscher application.

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/dao/meteoswiss/MeteoSwissRepository.java
- **Class Name(s):** `MeteoSwissRepository`

## 3. Functional Requirements

- **Primary Operations**: 
    - Persistence: Create, read, update, and delete `MeteoSwissEntity` records.
    - Data Retrieval: Retrieve historical temperature measurements from the database.
- **User Inputs & Outputs**:
    - *Inputs:* `stationId` (String), `maxRows` (Integer).
    - *Outputs:* A `List<MeteoSwissEntity>` containing the latest temperature entries.
- **Workflow/Logic**:
    - The `CrudRepository` interface provides standard CRUD operations on the `MeteoSwissEntity` entities.
    - The `getLastEntries` query retrieves records from the `meteo_swiss` table, filtering by `station_id` and ordering by `temperature_measure_date` in descending order.  It then limits the result set to `maxRows`.
- **External Interactions**:
    - Database interaction: Directly interacts with the database to store and retrieve `MeteoSwissEntity` records.
- **Edge Cases Handling**:
    - If `stationId` does not exist, the query will likely return an empty list.
    - If `maxRows` is negative or zero, the behavior is database-dependent.  It may return all rows, an empty list, or throw an error.
    - Database connection errors.

## 4. Non-Functional Requirements

- **Performance**:  The `getLastEntries` query should execute quickly, ideally within a few hundred milliseconds, even with a large number of records in the `meteo_swiss` table. Indexing of `station_id` and `temperature_measure_date` columns is crucial.
- **Scalability**: The repository should be able to handle a large number of concurrent requests without significant performance degradation. Database connection pooling and efficient query execution are vital.
- **Security**: Database access should be secured with appropriate authentication and authorization mechanisms.
- **Maintainability**: The interface is simple and well-defined, promoting easy maintenance and modification.
- **Reliability & Availability**:  The repository should be reliable and available, with appropriate error handling and recovery mechanisms.
- **Usability**: The interface provides a simple and intuitive way to access weather data.

## 5. Key Components

- **`MeteoSwissRepository` Interface:**  Defines the data access methods for `MeteoSwissEntity` objects.
- **`getLastEntries()` Function:** Executes a native SQL query to retrieve the latest entries for a given station.
- **`CrudRepository`**: Provides default implementations for common CRUD operations.
- **`MeteoSwissEntity` Class:** Represents a row in the `meteo_swiss` table.
- **Error Handling:** The Spring Data JPA framework handles exceptions that occur during database interactions.

## 6. Dependencies

### 6.1 Core Language Features

- Java Collections Framework (List)
- Data types (String, Integer)

### 6.2 External Frameworks & Libraries

- **Spring Data JPA**: Provides the `CrudRepository` interface and other data access features.
- **Spring Framework**: Required for dependency injection and other core functionalities.

### 6.3 Internal Project Dependencies

- **`com.x8ing.thsensor.thserver.db.entity.MeteoSwissEntity`**: The entity class representing the data in the `meteo_swiss` table.

## 7. Potential Improvements

- **Performance Enhancements**:
    - Add indexes to the `station_id` and `temperature_measure_date` columns in the `meteo_swiss` table to speed up the `getLastEntries` query.
    - Consider caching frequently accessed data to reduce database load.
- **Code Readability**: The code is already quite readable due to its simplicity.
- **Security Improvements**:  Ensure database connection parameters are securely stored and accessed. Implement appropriate access control mechanisms to protect the database.
- **Scalability Considerations**:  Implement database connection pooling to handle a large number of concurrent requests. Consider using a read-replica database to distribute read load.  Consider pagination for queries that return large result sets.