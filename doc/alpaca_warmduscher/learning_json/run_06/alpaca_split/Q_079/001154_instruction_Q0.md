You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This class, `UUIDUtils`, provides utility functions for converting between standard UUIDs (Universally Unique Identifiers) and a shorter, text-based representation. This shorter representation is designed to be more compact, avoid special characters, and be visually distinct, making it suitable for use in systems where UUIDs are stored or transmitted as text. The class also provides a function to generate new short-text UUIDs.

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/UUIDUtils.java
- **Class Name(s):** `UUIDUtils`

## 3. Functional Requirements

- **Primary Operations**:
    - Convert a standard `UUID` to a 22-character short textual representation.
    - Parse a 22-character short textual representation back into a `UUID`.
    - Generate a new, unique short-text UUID.

- **User Inputs & Outputs**:
    - **`toShortText(UUID uuid)`**:  Input: `UUID` object. Output: `String` (22-character short-text representation).
    - **`fromShortText(String shortTextUUID)`**: Input: `String` (22-character short-text representation). Output: `UUID` object.
    - **`generateShortTextUUID()`**:  Input: None. Output: `String` (22-character short-text UUID).

- **Workflow/Logic**:
    - **`toShortText`**: Converts the UUID to a byte array, then encodes it using a Base58-like encoding.
    - **`fromShortText`**: Decodes the short text using the Base58-like decoder, and reconstructs the UUID from the resulting byte array.
    - **`generateShortTextUUID`**: Generates a random UUID, converts it to short text. If the length is less than 22, appends characters from another randomly generated short text to achieve the desired length.

- **External Interactions**:
    -  Uses the `Base58BitcoinFlavor` class for encoding and decoding (internal dependency).
    -  Uses `java.util.UUID` for UUID generation and representation.
    - Uses `org.apache.commons.lang3.StringUtils` for string manipulation (length checks and substring operations).

- **Edge Cases Handling**:
    - **`toShortText(null)`**: Returns an empty string.
    - **`fromShortText(null)` or `fromShortText("")`**: Returns `null`.
    - **`generateShortTextUUID()`**: Ensures the generated short text is always 22 characters long, appending characters if necessary.

## 4. Non-Functional Requirements

- **Performance**:
    - Encoding and decoding operations should be relatively fast, ideally taking milliseconds.
- **Scalability**:
    - The class is stateless and should scale well with increased load.
- **Security**:
    - The short-text representation does *not* provide security or encryption. It's simply a different format for representing the UUID.
- **Maintainability**:
    - Code is well-commented and uses descriptive variable names.
    -  The use of a separate `Base58BitcoinFlavor` class promotes modularity.
- **Reliability & Availability**:
    - The class is relatively simple and has minimal dependencies, increasing reliability.
- **Usability**:  The class provides clear and concise methods for converting between UUIDs and the short-text format.
- **Compliance**: N/A

## 5. Key Components

- **`toShortText(UUID uuid)`**: Converts a UUID to its short-text representation.
- **`fromShortText(String shortTextUUID)`**: Converts a short-text representation to a UUID.
- **`generateShortTextUUID()`**: Generates a new, unique short-text UUID.
- **`Base58BitcoinFlavor`**: (Internal Dependency) Encodes and decodes byte arrays to/from Base58-like format.
- **Error Handling**: Handles `null` inputs in `toShortText` and `fromShortText`.
- **Classes**: No subclasses are defined.
- **Modules**: The class is a self-contained module with limited external dependencies.

## 6. Dependencies

### 6.1 Core Language Features

- Data structures: byte arrays.
- String manipulation.
- Random number generation (via `UUID.randomUUID()`).

### 6.2 External Frameworks & Libraries

- **`org.apache.commons.lang3`**: Used for string manipulation utilities (StringUtils).

### 6.3 Internal Project Dependencies

- **`Base58BitcoinFlavor`**:  An internal class responsible for Base58-like encoding and decoding.

## 7. Potential Improvements

- **Performance Enhancements**:  Explore more efficient encoding/decoding algorithms if performance becomes critical.
- **Code Readability**: The code is already fairly readable.
- **Security Improvements**: This class doesn't inherently deal with security.
- **Scalability Considerations**: The class is already relatively scalable due to its stateless nature. Consider caching frequently used short text representations if the application requires very high throughput.