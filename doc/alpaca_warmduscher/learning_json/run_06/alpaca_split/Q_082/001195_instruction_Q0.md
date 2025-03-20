You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This class, `Utils`, provides a collection of static utility methods for common operations within the 'Warmduscher' project.  It includes methods for retrieving client IP addresses from HTTP requests, calculating medians from collections, getting the last element of a collection, converting and formatting dates, handling JSON serialization, and creating a RestTemplate with preconfigured timeouts. These methods are designed to be reusable across different components of the application.

## 2. File Information

- **File Location:** `Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/Utils.java`
- **Class Name(s):** `Utils`

## 3. Functional Requirements

- **Primary Operations:**
    - IP Address Retrieval: Extract client IP address from an HTTP request.
    - Median Calculation: Calculate the median of a collection of values.
    - Last Element Retrieval: Retrieve the last element of a collection.
    - Date Conversion: Convert date/time between UTC and Switzerland timezones.
    - Date Formatting: Format a date/time object into a specific string format for Switzerland.
    - JSON Serialization: Convert an object into a JSON string.
    - RestTemplate Creation: Create a RestTemplate instance with specified connection and read timeouts.

- **User Inputs & Outputs:**
    - `getRequestIP()`: Input - `HttpServletRequest`. Output - `String` (IP address or addresses).
    - `getMedian()`: Input - `Collection<T>`, `ToDoubleFunction<T>`, `int`. Output - `double` (median).
    - `getLastElement()`: Input - `Collection<T>`. Output - `T` (last element or null).
    - `toBigDecimalWithRounding()`: Input - `double`, `int`. Output - `BigDecimal`.
    - `convertUTCToSwitzerlandTime()`: Input - `LocalDateTime`. Output - `LocalDateTime`.
    - `formatLocalDateTimeToLocalSwitzerlandTime()`: Input - `LocalDateTime`. Output - `String` (formatted date/time).
    - `getRestTemplate()`: Input - None. Output - `RestTemplate`.
    - `toJSON()`: Input - `Object`. Output - `String` (JSON string).

- **Workflow/Logic:**
    - `getRequestIP()`: Iterates through a predefined list of HTTP headers commonly used to store client IP addresses. Returns the first non-null and non-empty header value.
    - `getMedian()`:  Calculates the median of a subset of the input collection, handling a limit on the number of values used for the calculation.
    - `getLastElement()`: Iterates through the collection to retrieve the last element.
    - `toBigDecimalWithRounding()`: Converts a double to a BigDecimal and rounds it to the specified precision using `RoundingMode.HALF_UP`.
    - `convertUTCToSwitzerlandTime()`: Converts a LocalDateTime from UTC to the Europe/Zurich timezone.
    - `formatLocalDateTimeToLocalSwitzerlandTime()`: Converts a LocalDateTime to Switzerland time and then formats it according to a predefined pattern.
    - `getRestTemplate()`: Creates and configures a `RestTemplate` with specified connection and read timeouts.
    - `toJSON()`: Serializes an object to a JSON string using Jackson library. Handles potential exceptions during serialization.

- **External Interactions:**
    - `getRestTemplate()`:  Uses `SimpleClientHttpRequestFactory` to configure the RestTemplate, which is used for making HTTP requests.
    - `toJSON()`: Uses Jackson's `ObjectMapper` for JSON serialization.
    - Date/Time operations leverage Java's `java.time` package for timezone conversions and formatting.

- **Edge Cases Handling:**
    - `getRequestIP()`: Handles cases where none of the expected headers are present by returning the remote address of the request.
    - `getMedian()`: Handles null input collections and a negative limit by setting the limit to 0.  It also handles cases where the collection size is smaller than the limit.
    - `getLastElement()`: Handles null or empty collections by returning null.
    - `toJSON()`: Handles potential `JsonProcessingException` during serialization by logging the error and returning an empty string.
    - `convertUTCToSwitzerlandTime()`: Handles null `LocalDateTime` input by returning null.

## 4. Non-Functional Requirements

- **Performance:**  Methods are generally designed for quick execution.  The `getMedian()` method's performance may depend on the size of the input collection and the specified limit.
- **Scalability:** The class is stateless and therefore inherently scalable.
- **Security:** No specific security requirements are directly addressed within this class, but the IP address retrieval should be used carefully and validated to prevent IP spoofing.
- **Maintainability:** The code is relatively simple and well-structured, with clear method names and comments.
- **Reliability & Availability:** The class is reliable as it handles edge cases and potential exceptions.
- **Usability:** The methods are easy to use and integrate into other components.
- **Compliance:**  No specific compliance requirements.

## 5. Key Components

- **Functions:**
    - `getRequestIP()`: Retrieves client IP address from an HTTP request.
    - `getMedian()`: Calculates the median of a collection.
    - `getLastElement()`: Retrieves the last element of a collection.
    - `toBigDecimalWithRounding()`: Rounds a double to a specified precision.
    - `convertUTCToSwitzerlandTime()`: Converts UTC time to Switzerland time.
    - `formatLocalDateTimeToLocalSwitzerlandTime()`: Formats a LocalDateTime to a string for Switzerland.
    - `getRestTemplate()`: Creates a RestTemplate with configured timeouts.
    - `toJSON()`: Serializes an object to a JSON string.
- **Important Logic Flows:**  See Functional Requirements - Workflow/Logic.
- **Error Handling:**  See Functional Requirements - Edge Cases Handling.
- **Classes:** No subclasses are defined.
- **Modules:** This class is a single module providing utility functions.

## 6. Dependencies

### 6.1 Core Language Features

- Data structures: `Collection`, `List`, `Iterator`.
- Date/Time API: `java.time` package (LocalDateTime, ZoneId, DateTimeFormatter).
- BigDecimal: for precise decimal calculations.
- Exception handling: `try-catch` blocks for handling potential errors.

### 6.2 External Frameworks & Libraries

- **Jackson Core/Databin**: Used for JSON serialization (within the `toJSON` method).
- **Apache Commons Math3:** Used for calculating the median (within the `getMedian` method).
- **SLF4J:** Used for logging.
- **Spring Web:** Used for creating a `RestTemplate` instance (although not strictly required).

### 6.3 Internal Project Dependencies

- None identified at this time.

## 7. Potential Improvements

- **Performance Enhancements:** For very large collections in `getMedian()`, consider using more efficient algorithms for finding the median.
- **Code Readability:** While generally readable, adding more detailed Javadoc comments would enhance maintainability.
- **Security Improvements:**  Implement robust IP address validation in `getRequestIP()` to prevent IP spoofing.
- **Scalability Considerations:**  No specific scalability concerns are apparent at this time.  If the application experiences high load, consider caching frequently used data (e.g., timezone information).
- **Testing:** Add unit tests for each method to ensure proper functionality and edge case handling.