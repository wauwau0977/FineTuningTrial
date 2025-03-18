You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This Java class `Utils` provides a collection of static utility methods for common tasks within the 'Warmduscher' project.  These tasks include retrieving the client IP address from an HTTP request, calculating the median of a collection of numerical values, retrieving the last element of a collection, rounding doubles to BigDecimals, converting between timezones (UTC to Switzerland), creating a RestTemplate with defined timeouts, and converting objects to JSON strings. The class serves as a central location for reusable functionality, promoting code consistency and reducing redundancy.

## 2. File Information

- **File Location:** `Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/Utils.java`
- **Class Name(s):** `Utils`

## 3. Functional Requirements

- **Primary Operations**:
    - Client IP Address Retrieval: Extracts the client's IP address from an HTTP request, considering various header fields.
    - Median Calculation: Computes the median of a collection of numerical values, optionally limiting the number of samples used.
    - Last Element Retrieval: Retrieves the last element from a given collection.
    - BigDecimal Conversion: Converts a double to a BigDecimal with specified precision and rounding mode.
    - Timezone Conversion: Converts a LocalDateTime object from UTC to Switzerland (Europe/Zurich) timezone.
    - RestTemplate Creation: Creates a RestTemplate instance with predefined connection and read timeouts.
    - JSON Serialization: Converts an object to a JSON string.
- **User Inputs & Outputs**:
    - `getRequestIP()`: Input: `HttpServletRequest`. Output: String (IP Address or addresses).
    - `getMedian()`: Input: `Collection<T>`, `ToDoubleFunction<T>`, `int`. Output: `double` (Median).
    - `getLastElement()`: Input: `Collection<T>`. Output: `T` (Last element, or null if the collection is empty).
    - `toBigDecimalWithRounding()`: Input: `double`, `int`. Output: `BigDecimal` (Rounded value).
    - `convertUTCToSwitzerlandTime()`: Input: `LocalDateTime`. Output: `LocalDateTime` (Converted Time).
    - `formatLocalDateTimeToLocalSwitzerlandTime()`: Input: `LocalDateTime`. Output: `String` (Formatted Time).
    - `getRestTemplate()`: Output: `RestTemplate` instance.
    - `toJSON()`: Input: `Object`. Output: `String` (JSON representation of the object, or null if the object is null).
- **Workflow/Logic**:
    - `getRequestIP()` iterates through a predefined list of headers, returning the first non-empty value. If no header value is found, it returns the remote address of the request.
    - `getMedian()` retrieves values from the collection, limits the sample size if needed, and uses Apache Commons Math to calculate the median.
    - `getLastElement()` iterates the collection, returning the final element after traversing the collection.
    - `toBigDecimalWithRounding()` creates a `BigDecimal` from the double and sets the scale and rounding mode.
    - `convertUTCToSwitzerlandTime()` uses Java's time API to convert from UTC to Switzerland time zone.
    - `formatLocalDateTimeToLocalSwitzerlandTime()` converts from UTC and then format it using defined format.
    - `getRestTemplate()` creates a `SimpleClientHttpRequestFactory` with defined timeouts and uses it to create a `RestTemplate` instance.
    - `toJSON()` uses Jackson's ObjectMapper to serialize the object to JSON.  Handles potential `JsonProcessingException`.
- **External Interactions**:
    - Apache Commons Math library used for median calculation.
    - Jackson library for JSON serialization.
    - Java Time API for time zone conversion.
- **Edge Cases Handling**:
    - `getRequestIP()`: Handles empty or null header values gracefully.
    - `getMedian()`: Handles null entries, and null supplier.
    - `getLastElement()`: Returns `null` if the collection is `null` or empty.
    - `toBigDecimalWithRounding()`: The rounding mode handles the edge cases of double to BigDecimal conversion.
    - `convertUTCToSwitzerlandTime()`: Handles `null` input by returning `null`.
    - `toJSON()`: Returns null if the input is null and logs an error if JSON serialization fails.

## 4. Non-Functional Requirements

- **Performance**: Methods should execute efficiently for typical use cases.  The RestTemplate factory should provide reasonable connection and read timeouts.
- **Scalability**: The utility class itself doesn’t impose scalability limitations.  Scalability depends on the external libraries used.
- **Security**: No direct security concerns within the class itself. The RestTemplate could be used in insecure ways depending on how it is used by other components.
- **Maintainability**: The class is relatively small and well-structured. The use of static methods promotes modularity.
- **Reliability & Availability**: The class depends on the reliability of the external libraries (Apache Commons Math, Jackson).
- **Usability**: The static methods are easy to use from other parts of the application.
- **Compliance**: No specific compliance requirements.

## 5. Key Components

- **Functions**:
    - `getRequestIP()`: Retrieves client IP address.
    - `getMedian()`: Calculates the median of a collection.
    - `getLastElement()`: Retrieves the last element of a collection.
    - `toBigDecimalWithRounding()`: Converts a double to a BigDecimal with rounding.
    - `convertUTCToSwitzerlandTime()`: Converts a LocalDateTime from UTC to Switzerland time.
    - `formatLocalDateTimeToLocalSwitzerlandTime()`: Formats a LocalDateTime to a specific string format in Switzerland Time.
    - `getRestTemplate()`: Creates a RestTemplate with defined timeouts.
    - `toJSON()`: Converts an object to a JSON string.
- **Important Logic Flows**:  Each function encapsulates a specific, self-contained logic flow.
- **Error Handling**:  Functions handle null or empty inputs by returning appropriate default values or logging errors.
- **Classes**: No subclasses defined.
- **Modules**:  The class itself is a single module.

## 6. Dependencies

### 6.1 Core Language Features

- Data structures: `Collection`, `Iterator`
- Date and Time API: `LocalDateTime`, `ZoneId`, `DateTimeFormatter`
- Math API: `BigDecimal`, `RoundingMode`
- Logging: `org.slf4j.Logger`

### 6.2 External Frameworks & Libraries

- **Apache Commons Math**: Used for statistical calculations, specifically median calculation.
- **Jackson**: Used for JSON serialization and deserialization.
- **Spring Framework**: `RestTemplate` and `SimpleClientHttpRequestFactory` are used.

### 6.3 Internal Project Dependencies

- No internal project dependencies are explicitly defined in this code.

## 7. Potential Improvements

- **Performance Enhancements**: The RestTemplate factory could be cached to reduce object creation overhead.
- **Code Readability**: The `IP_HEADERS` array could be replaced with a `List` or `Set` for easier modification.
- **Security Improvements**:  The IP address retrieval logic should be reviewed to ensure it is resistant to IP spoofing attacks.
- **Scalability Considerations**:  If the application experiences high load, consider using a more robust logging framework or caching mechanism.
- **Testing**: Add unit tests to verify the functionality of each method, including edge cases.  Consider using mock objects to isolate dependencies.