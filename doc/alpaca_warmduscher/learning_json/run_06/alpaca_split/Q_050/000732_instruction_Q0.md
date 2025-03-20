You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This code implements a service that retrieves meteorological data (temperature, sunshine duration, and wind gust speed) from the MeteoSwiss API.  It parses the JSON responses from the API, extracts relevant data for specified station IDs, and packages the results into a list of `MeteoSwissEntity` objects.  The service is designed to be active when the `SENSOR_MOCK` profile is not enabled.

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/data/meteoswiss/impl/MeteoDataServiceImpl.java
- **Class Name(s):** `MeteoDataServiceImpl`, `ResDateValue`

## 3. Functional Requirements

- **Primary Operations**: 
    - Fetch meteorological data from the MeteoSwiss API for specified station IDs.
    - Parse the JSON responses from the API.
    - Extract temperature, sunshine duration, and wind gust data.
    - Create and return a list of `MeteoSwissEntity` objects containing the extracted data.
- **User Inputs & Outputs**:
    - **Inputs**: Configuration properties for API URLs and station IDs (via Spring Boot `@Value`).
    - **Outputs**: A `List<MeteoSwissEntity>` containing the meteorological data for each specified station.
- **Workflow/Logic**:
    1. Initialize the service (sets up JSON path configuration).
    2. Retrieve JSON data for temperature, sunshine, and wind gust from the respective APIs using `callService()`.
    3. Iterate through the list of `stationIds`.
    4. For each station ID, extract the required data (temperature, sunshine, wind gust) from the JSON responses using `extractFromJSON()`.
    5. Create a `MeteoSwissEntity` object with the extracted data.
    6. Add the created entity to the list of entities.
    7. Return the list of `MeteoSwissEntity` objects.
- **External Interactions**:
    - **HTTP GET requests**:  The code makes HTTP GET requests to the MeteoSwiss API endpoints (defined by `@Value` properties: `urlSunshine`, `urlTemperature`, `urlWindGust`).
- **Edge Cases Handling**:
    - **API Unavailability**:  The code does not currently handle API unavailability explicitly.  A `RestTemplate` exception would occur, which would need to be caught and handled appropriately (e.g., logging, retrying, or returning a default value).
    - **Invalid JSON Response**:  The JSONPath parsing might fail if the API returns invalid JSON.  Error handling (try-catch blocks) should be implemented within `extractFromJSON()` to handle `JsonPathException` and provide appropriate logging or fallback behavior.
    - **Station ID Not Found**: If a `stationId` is not found in the JSON response, `JsonPath.read()` will return an empty list or `null`.  The code currently assumes that all station IDs will be present. The extraction logic should handle the case when the station ID is missing.
    - **Null Values**: JSON fields might contain null values. The code should handle these null values appropriately to prevent `NullPointerException`.

## 4. Non-Functional Requirements

- **Performance**: The service should be responsive, aiming for a completion time of under 5 seconds for retrieving and processing data for all configured stations.
- **Scalability**: The service is currently designed to handle a limited number of stations (defined by the `stationIds` list).  For a larger number of stations, caching mechanisms or asynchronous processing could be considered.
- **Security**: The code doesn't inherently handle security, but it depends on the security of the underlying HTTP connection and the MeteoSwiss API itself.
- **Maintainability**: The code is reasonably well-structured and uses descriptive variable names.  Adding comments to explain complex logic would improve maintainability.
- **Reliability & Availability**: The code’s reliability depends on the availability of the MeteoSwiss API and proper error handling.
- **Usability**: The service is intended for internal use within the `Warmduscher` project and doesn't have a direct user interface.
- **Compliance**: The service needs to adhere to the terms of service of the MeteoSwiss API.

## 5. Key Components

- **`MeteoDataServiceImpl`**: This class implements the `MeteoDataService` interface and contains the main logic for retrieving and processing data from the MeteoSwiss API.
- **`ResDateValue`**: A data class used to encapsulate the extracted data (measurement date, value1, value2, station name) from the JSON response.
- **`init()`**: Initializes the JSONPath configuration.
- **`getData()`**: Orchestrates the data retrieval and processing workflow.
- **`extractFromJSON()`**: Extracts data from the JSON response using JSONPath.
- **`callService()`**: Makes HTTP GET requests to the MeteoSwiss API.
- **Error Handling:** Limited. Requires enhancements to manage API failures and invalid JSON responses.

## 6. Dependencies

### 6.1 Core Language Features
- Data structures: `List`, `Date`
- Date/Time: `Instant`, `DateTimeFormatter`
- Standard Libraries: `java.net`, `java.util`

### 6.2 External Frameworks & Libraries
- **Spring Boot**: Used for dependency injection, configuration management, and HTTP client (`RestTemplate`).
- **Jackson**: Used for JSON parsing. (used implicitly by Spring Boot/RestTemplate)
- **Jayway JSONPath**: Used for parsing JSON and extracting data based on JSONPath expressions.
- **Lombok**: Used for generating boilerplate code (e.g., getters, setters, constructors).
- **SLF4J**: Used for logging.

### 6.3 Internal Project Dependencies
- None explicitly defined.

## 7. Potential Improvements

- **Performance Enhancements**:
    - **Caching**: Implement caching of API responses to reduce the number of requests and improve response time.
    - **Asynchronous Processing**: Use asynchronous processing to retrieve data from multiple APIs concurrently.
- **Code Readability**:
    - Add more comments to explain complex logic.
    - Consider refactoring long methods into smaller, more manageable units.
- **Security Improvements**:
    - Implement proper error handling and logging to prevent sensitive information from being exposed.
- **Scalability Considerations**:
    - Use a message queue (e.g., RabbitMQ, Kafka) to distribute the workload and handle a larger number of stations.
    - Consider using a database to store historical data and provide better query performance.
- **Error Handling**: Implement comprehensive error handling to catch and handle exceptions (e.g., API unavailability, invalid JSON responses) gracefully. Logging errors with appropriate context is crucial.
- **Unit Tests**: Add unit tests to verify the correctness of the code and ensure that it handles different scenarios correctly.
- **Configuration Externalization:** Move all configuration (URLs, station IDs) to a dedicated configuration file or environment variables for easier management and deployment.