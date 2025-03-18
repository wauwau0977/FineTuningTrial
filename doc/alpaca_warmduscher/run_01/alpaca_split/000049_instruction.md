You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This interface `BoilerStatsByDayOfWeek` defines a data structure for representing aggregated boiler statistics grouped by day of the week. It's designed to hold pre-calculated values related to boiler performance differences (decrease and increase) and the number of records used for the calculation.  This interface is likely used for reporting and analysis of boiler efficiency over time.

## 2. File Information

- **File Location:** `Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/analytics/BoilerStatsByDayOfWeek.java`
- **Class Name(s):** `BoilerStatsByDayOfWeek`

## 3. Functional Requirements

- **Primary Operations**: The code defines a data contract for retrieving boiler statistics grouped by day of the week. It doesn’t perform calculations itself; rather, it outlines *what* data should be available.
- **User Inputs & Outputs**:  There are no direct user inputs or outputs.  This interface is used internally by the application to structure data retrieved from a database or calculated from other sources. Outputs are the values returned by the getter methods of the interface.
- **Workflow/Logic**:  The workflow involves retrieving or calculating the required statistical data (sum of boiler difference decrease, sum of boiler difference increase, and the number of records), then populating an object conforming to this interface to provide a structured data representation.
- **External Interactions**:  The interface itself does not have external interactions. However, implementations of this interface will likely interact with a database or other data source to retrieve the necessary statistics.
- **Edge Cases Handling**: Since it's an interface, it doesn’t handle edge cases directly. Implementations must handle potential null values, invalid data, or database connection errors.  The specific handling of such cases will depend on the broader application context.

## 4. Non-Functional Requirements

- **Performance**: Performance is dependent on the implementation and the data source. Retrieval of data should be efficient.
- **Scalability**: Scalability is dependent on the implementation and underlying data storage.
- **Security**: No direct security considerations within the interface itself. Security concerns will reside in the implementation and data access layers.
- **Maintainability**: The interface is relatively simple and easy to maintain due to its clear definition of data attributes.
- **Reliability & Availability**: Reliability and availability are dependent on the implementation and the data source.
- **Usability**: The interface is usable in that it provides a well-defined data structure for representing boiler statistics.
- **Compliance**: No specific compliance requirements are implied by the interface definition.

## 5. Key Components

- **Functions**:
    - `getDayOfWeekStartingMonday()`: Returns the day of the week as an integer, starting with Monday as 1.
    - `getDayOfWeekText()`: Returns a string representation of the day of the week.
    - `getSumBoilerDiffDecrease()`: Returns the sum of boiler differences that represent decreases.
    - `getSumBoilerDiffIncrease()`: Returns the sum of boiler differences that represent increases.
    - `getNumOfStatisticRecords1()`: Returns the number of statistic records used for calculating the other values.
- **Important logic flows**: The interface focuses on data representation; therefore, there's no complex logic flow within the interface itself.
- **Error handling**: The interface does not have explicit error handling.
- **Classes**: This is an interface, not a class.  It does not define subclasses.
- **Modules**: Part of the `com.x8ing.thsensor.thserver.db.entity.analytics` package.

## 6. Dependencies

### 6.1 Core Language Features
- Data structures: Primitive data types (Integer, Double, Long, String).

### 6.2 External Frameworks & Libraries
- **Jackson annotations**: The `@JsonPropertyOrder` annotation is used for JSON serialization ordering. Jackson is a popular JSON processing library.

### 6.3 Internal Project Dependencies
- No apparent internal dependencies beyond being part of the `Warmduscher` project.

## 7. Potential Improvements

- **Consider using an enum for `dayOfWeekStartingMonday`**: Instead of an Integer, using an enum would improve readability and type safety.
- **Documentation**: Add JavaDoc comments to explain the purpose of each getter method and the meaning of the returned values.
- **Naming**: Review the name `numOfStatisticRecords1` for clarity.  `recordCount` or `statisticRecordCount` would be more descriptive.
- **Data types**: Confirm the appropriate data types are being used for each attribute. For instance, consider if `Double` is necessary or if a more precise data type (e.g., `BigDecimal`) should be used for monetary or precise calculations.