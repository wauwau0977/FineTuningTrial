You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This class, `UUIDUtils`, provides utility methods for converting between standard UUIDs and a shorter, text-based representation. The purpose is to create a more compact and user-friendly format for representing UUIDs, suitable for storage in systems with length limitations or for display purposes. It also includes a method to generate random short UUIDs. The short text representation utilizes a Base58 encoding scheme and avoids potentially problematic characters.

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/UUIDUtils.java
- **Class Name(s):** `UUIDUtils`

## 3. Functional Requirements

- **Primary Operations**: 
    - Convert a standard UUID to a short (22-character) text representation.
    - Parse a short text representation back into a standard UUID.
    - Generate a random short text UUID.
- **User Inputs & Outputs**:
    - `toShortText(UUID uuid)`: Input - `UUID` object. Output - `String` (short text representation).
    - `fromShortText(String shortTextUUID)`: Input - `String` (short text representation). Output - `UUID` object.
    - `generateShortTextUUID()`: Input - None. Output - `String` (random short text UUID).
- **Workflow/Logic**:
    - `toShortText`: Converts the UUID to a byte array, then encodes it using a Base58 encoding scheme.
    - `fromShortText`: Decodes the Base58 encoded string to a byte array, then creates a UUID from the byte array.
    - `generateShortTextUUID`: Generates a UUID, converts it to a short text representation.  If the resulting short text is shorter than the expected fixed size (22 characters), it appends characters from another randomly generated short UUID to reach the target length.
- **External Interactions**:  None. The class operates entirely in memory.
- **Edge Cases Handling**:
    - `toShortText(null)`: Returns an empty string.
    - `fromShortText(null)` or `fromShortText("")`: Returns `null`.
    - `generateShortTextUUID()`: Handles potential length issues of generated short UUIDs by appending additional characters.

## 4. Non-Functional Requirements

- **Performance**: Encoding and decoding should be relatively fast, as these operations might be performed frequently.  No strict performance requirements specified.
- **Scalability**: Not applicable. The class handles single UUID conversions and does not involve any external resources.
- **Security**: The conversion is designed to produce “safe” characters, avoiding special or control characters. No encryption or sensitive data handling is involved.
- **Maintainability**: The code is relatively simple and well-commented, promoting maintainability.
- **Reliability & Availability**: The methods have basic null checks and should be reliable.
- **Usability**: The class provides a clear and straightforward API for UUID conversion.
- **Compliance**: No specific compliance requirements.

## 5. Key Components

- **Functions**:
    - `toShortText(UUID uuid)`: Converts a UUID to a Base58 encoded string.
    - `fromShortText(String shortTextUUID)`: Converts a Base58 encoded string back to a UUID.
    - `generateShortTextUUID()`: Generates a random UUID and converts it to a Base58 encoded string with fixed length.
- **Important logic flows**: Conversion between UUID and Base58 string; handling length inconsistencies in the `generateShortTextUUID` method.
- **Error handling**: Null checks for input parameters in `toShortText` and `fromShortText`.
- **Classes**: No subclasses defined.
- **Modules**:  The class is self-contained and doesn't rely on other complex modules.

## 6. Dependencies

### 6.1 Core Language Features

- `java.util.UUID`: Used for creating and manipulating UUID objects.
- `java.nio.ByteBuffer`: Used for converting between byte arrays and primitive data types.
- `java.lang.String`: Used for string manipulation.

### 6.2 External Frameworks & Libraries

- `org.apache.commons.lang3.StringUtils`: Used for string utility functions (checking for empty strings, getting string length, substring).

### 6.3 Internal Project Dependencies

- None.

## 7. Potential Improvements

- **Performance Enhanecements:** Benchmark the performance of the Base58 encoding and decoding to identify potential bottlenecks.
- **Code Readability:** The code is already reasonably readable but could be improved further by adding more descriptive variable names where appropriate.
- **Security Improvements:** While the current implementation avoids problematic characters, a more comprehensive security review could identify any potential vulnerabilities.
- **Scalability Considerations:** Not applicable. The class is not designed for high-volume operations.
- **Testing**: Add unit tests to cover all the functionalities, including edge cases. Specifically, ensure that the `generateShortTextUUID()` method consistently produces strings of the expected length.