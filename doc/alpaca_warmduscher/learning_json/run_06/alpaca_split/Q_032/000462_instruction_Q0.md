You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary
This code defines a TypeScript class, `BoilerStatsDayOfWeekEntity`, designed to hold statistical data for a specific day of the week, related to boiler performance. It encapsulates data like the day of the week (as a number and text), the sum of boiler differences (increase & decrease), and the number of statistic records associated with that day. The class provides methods for creating instances, including an empty instance and one initialized from web service data.

## 2. File Information
- **File Location:** Warmduscher/thclient/src/main/www/thserver-client/src/app/entities/boilerStatsDayOfWeekEntity.ts
- **Class Name(s):** `BoilerStatsDayOfWeekEntity`

## 3. Functional Requirements
- **Primary Operations**: The primary operation is to represent and store boiler statistics for a single day of the week.
- **User Inputs & Outputs**: This class does not directly handle user input or output.  It serves as a data container for data received from a backend service (Web Service) and potentially passed to UI components.
- **Workflow/Logic**:
    1. The constructor initializes the object with provided data.
    2. `emptyInstance()` returns a default instance with zero values for all fields.
    3. `ofWebService()` creates an instance from a data object received from a web service, returning an empty instance if the input data is null.
- **External Interactions**: The `ofWebService` method interacts with data received from an external web service. This assumes the external service provides an object with the following keys: `dayOfWeekStartingMonday`, `dayOfWeekText`, `sumBoilerDiffIncrease`, `sumBoilerDiffDecrease`, `numOfStatisticRecords1`.
- **Edge Cases Handling**:
    - `ofWebService()` handles null input data by returning an empty instance. This prevents errors when processing data from the web service.

## 4. Non-Functional Requirements
- **Performance**: The class is a simple data container and should have minimal performance overhead.
- **Scalability**: The class is not directly involved in scalability concerns. Scalability will be handled by the systems that utilize instances of this class.
- **Security**: This class does not handle sensitive data directly, so security concerns are minimal. However, the data *within* the class, when sourced externally, should be validated for integrity and potential injection attacks at the point of consumption (e.g., in a controller or service).
- **Maintainability**: The class is well-structured and easy to understand, promoting maintainability.
- **Reliability & Availability**: The class itself is reliable as it only encapsulates data. Reliability depends on the source of the data and the systems that use the instances.
- **Usability**: The class is designed to be used by other components within the `Warmduscher` application and provides a clear and concise representation of boiler statistics.
- **Compliance**: No specific compliance requirements are apparent for this class.

## 5. Key Components
- **Functions:**
    - **Constructor:** Initializes the `BoilerStatsDayOfWeekEntity` object with the provided data.
    - **`emptyInstance()`**: Returns an instance with default (empty) values.
    - **`ofWebService(data: any)`**: Creates an instance from data received from a web service.
- **Important logic flows**: The main logic flow involves creating instances of the class, either with direct values or from web service data.
- **Error handling**: The `ofWebService` method provides basic error handling by returning an empty instance when the web service data is null.
- **Classes**:  No subclasses are defined.
- **Modules**: This class is a standalone entity within the `app.entities` module.

## 6. Dependencies

### 6.1 Core Language Features
- **TypeScript Classes:** Utilizes TypeScript class syntax for object creation and encapsulation.
- **Data Types:** Uses primitive data types like `number` and `string`.

### 6.2 External Frameworks & Libraries
- None. This class doesn't rely on external frameworks or libraries.

### 6.3 Internal Project Dependencies
- None. This class is self-contained within the project.

## 7. Potential Improvements
- **Type Safety:** While TypeScript is used, consider using more specific types instead of `any` for the `data` parameter in `ofWebService` to improve type safety and reduce potential runtime errors. Define an interface or type alias for the expected web service data structure.
- **Validation:** Add validation logic to the constructor or a static method to ensure that the input data is valid (e.g., numbers are within acceptable ranges).
- **Immutability:** Consider making the class immutable to prevent accidental modification of data.  This could be achieved by using `readonly` properties.
- **Documentation:** Add JSDoc comments to the class and methods to improve documentation and code understandability.