You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This interface defines a data structure for representing boiler statistics aggregated by day of the week. It serves as a data transfer object (DTO) to present pre-calculated statistics from the database, including the sum of boiler difference decreases, increases, and the number of records contributing to those sums, all broken down by day of the week. It is designed to be used in reporting and analysis of boiler performance.

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/analytics/BoilerStatsByDayOfWeek.java
- **Class Name(s):** `BoilerStatsByDayOfWeek`

## 3. Functional Requirements

- **Primary Operations:** Represent boiler statistics by day of the week. Provide access to aggregated data.
- **User Inputs & Outputs:** This interface doesn’t directly take input from a user or provide output directly. Instead, it *defines* the structure of data that will be populated and consumed by other parts of the application (e.g., a service layer that queries the database and returns data conforming to this interface). The output is the data structured as per the interface’s getters.
- **Workflow/Logic:** The interface represents a static data structure. The logic resides in the code that *populates* this interface with data, typically a database query or calculation.
- **External Interactions:** No external interactions directly within the interface itself. Interactions occur in the code that *uses* this interface, potentially involving:
    - Database Queries: To retrieve raw data for aggregation.
    - Reporting/Visualization Tools: To display the aggregated statistics.
- **Edge Cases Handling:** No edge case handling is defined *within* the interface itself. The implementation that uses this interface must handle scenarios like:
    - Missing data.
    - Invalid or unexpected values.
    - Empty result sets.

## 4. Non-Functional Requirements

- **Performance:** The interface itself has minimal performance implications. Performance is determined by the efficiency of the data retrieval and aggregation process.
- **Scalability:** The interface does not directly impact scalability.
- **Security:** The interface does not directly address security concerns. Data security depends on the implementation and the underlying data sources.
- **Maintainability:** The interface is simple and well-defined, enhancing maintainability. Any changes to the data structure require updates to both the interface and the implementation.
- **Reliability & Availability:** The interface itself does not affect reliability or availability.
- **Usability:** The interface is easy to understand and use by developers.
- **Compliance:** No specific compliance requirements are applicable to this interface alone.

## 5. Key Components

- **Functions:** This interface defines *getter* methods:
    - `getDayOfWeekStartingMonday()`: Returns the day of the week as an integer, starting with Monday as 1.
    - `getDayOfWeekText()`: Returns the day of the week as a human-readable string.
    - `getSumBoilerDiffDecrease()`: Returns the sum of boiler difference decreases for the specified day.
    - `getSumBoilerDiffIncrease()`: Returns the sum of boiler difference increases for the specified day.
    - `getNumOfStatisticRecords1()`: Returns the number of statistic records that contributed to the calculations.
- **Important logic flows:** No logic flows within the interface itself.
- **Error handling:** No error handling within the interface.
- **Classes:** This is an interface, not a class. It doesn't have subclasses.
- **Modules:** Belongs to the `com.x8ing.thsensor.thserver.db.entity.analytics` package.

## 6. Dependencies

### 6.1 Core Language Features

- Basic Java language features.
- Data structures (implicitly used to store the returned values).

### 6.2 External Frameworks & Libraries

- **Jackson Annotations:** `@JsonPropertyOrder` is used for controlling the order of properties when serializing to JSON.  Requires Jackson library.

### 6.3 Internal Project Dependencies

- None explicitly defined within this interface itself.



## 7. Potential Improvements

- **Consider Data Types:** Review the data types (e.g., `Double` for sums) to ensure they are appropriate for the expected range of values and precision requirements. Consider using `BigDecimal` for financial calculations to avoid floating-point precision issues.
- **Naming Conventions:** While the naming is adequate, consider using more descriptive names to improve clarity. For instance, `NumOfStatisticRecords1` could be renamed to `numberOfRecords`.
- **Immutability:** Consider making the interface immutable to prevent accidental modification of the data. This can be achieved by defining all fields as `final` and providing only getter methods. However, since this is an interface, immutability is enforced by the implementing class.