You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This code provides a Base58 encoding and decoding mechanism, specifically tailored for use cases like Bitcoin addresses. It allows for converting byte arrays to Base58 strings and vice versa, while also offering utility functions for encoding and decoding Unicode strings using this Base58 scheme. The implementation handles leading zeros efficiently and is designed to be a safe alternative to Base64, avoiding special characters like the equals sign.

## 2. File Information

- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/Base58BitcoinFlavor.java
- **Class Name(s):** Base58BitcoinFlavor

## 3. Functional Requirements

- **Primary Operations**:
    - Encode a byte array into a Base58 string.
    - Decode a Base58 string into a byte array.
    - Encode a Unicode string into a Base58 string.
    - Decode a Base58 string into a Unicode string.
    - Decode a Base58 string into a BigInteger
- **User Inputs & Outputs**:
    - **Encode (byte[]):** Input: `byte[]`. Output: `String` (Base58 encoded string).
    - **Decode (String):** Input: `String` (Base58 encoded string). Output: `byte[]`.
    - **Encode (String):** Input: `String` (Unicode string). Output: `String` (Base58 encoded string).
    - **Decode (String):** Input: `String` (Base58 encoded string). Output: `String` (Unicode string).
    - **Decode to BigInteger (String):** Input: `String` (Base58 encoded string). Output: `BigInteger`.
- **Workflow/Logic**:
    - **Encoding**: Converts a byte array to a Base58 representation by repeatedly converting 256-based digits to 58-based digits.  Handles leading zeros for optimization and correct representation.
    - **Decoding**: Converts a Base58 string back to a byte array by reversing the encoding process.  Handles potential invalid characters in the input string.
    - **Unicode String Encoding/Decoding:**  Encodes/Decodes a Unicode string to/from a byte array using UTF-8 encoding, and then uses the standard Base58 encode/decode methods.
- **External Interactions**:
    -  Uses `java.nio.charset.StandardCharsets` to encode and decode strings to byte arrays using the UTF-8 character set.
    -  Uses `java.math.BigInteger` for representing and converting Base58 strings to BigInteger.
- **Edge Cases Handling**:
    - **Invalid Characters in Decode:**  The `decode()` method throws a `RuntimeException` if the input string contains invalid characters (characters not present in the Base58 alphabet).
    - **Empty Input:** The `encode()` and `decode()` methods handle empty input gracefully, returning an empty string or an empty byte array, respectively.
    - **Leading Zeros:** The encoding and decoding process correctly handles leading zeros in the input data.

## 4. Non-Functional Requirements

- **Performance**:  Encoding and decoding operations should be relatively fast, suitable for use in real-time applications.  Specific performance targets (e.g., maximum execution time) are not defined in the code.
- **Scalability**:  The code is not inherently designed for massive scalability. Performance will likely degrade with extremely large input byte arrays or strings.
- **Security**: The Base58 encoding itself doesn't provide encryption or strong security. It's primarily a means of representing data in a URL-safe format.
- **Maintainability**: The code is reasonably well-structured and commented, making it relatively easy to understand and maintain.
- **Reliability & Availability**:  The code appears to be stable and reliable.  No specific fault tolerance mechanisms are implemented.
- **Usability**: The code provides a straightforward API for encoding and decoding Base58 strings.
- **Compliance**:  The code follows general Java coding conventions and doesn't have any specific compliance requirements.

## 5. Key Components

- **`encode(byte[] input)`**:  Encodes a byte array into a Base58 string.
- **`decode(String input)`**: Decodes a Base58 string into a byte array.
- **`encodeUnicodeStringToBase58String(String unicodeText)`**: Encodes a Unicode string to a Base58 string.
- **`decodeBase58ToUnicodeString(String base58Text)`**: Decodes a Base58 string to a Unicode string.
- **`decodeToBigInteger(String input)`**: Decodes a Base58 string to a BigInteger.
- **`divmod(byte[] number, int firstDigit, int base, int divisor)`**:  Private helper function that performs the division and modulo operations required for the encoding and decoding algorithms.
- **`ALPHABET`**:  The character array defining the Base58 alphabet.
- **`INDEXES`**: An array used for fast lookup of characters in the Base58 alphabet during decoding.

## 6. Dependencies

### 6.1 Core Language Features
- Data structures: Arrays, char arrays, byte arrays.
- Character encoding: `StandardCharsets.UTF_8`.
- Math: `BigInteger`.

### 6.2 External Frameworks & Libraries
- None. The code relies solely on standard Java libraries.

### 6.3 Internal Project Dependencies
- None. The code appears to be self-contained.

## 7. Potential Improvements

- **Performance Enhancements:**
    - Profile the code to identify potential bottlenecks, especially in the `divmod()` function.
    - Consider using a more efficient data structure for the `INDEXES` array if performance is critical.
- **Code Readability:**
    - The `divmod()` function could be further refactored to improve readability.
- **Security Improvements:**
    - The Base58 encoding itself doesn't provide security. If security is required, consider adding a checksum or other cryptographic mechanisms.
- **Scalability Considerations:**
    - For extremely large input data, consider using a stream-based approach to avoid loading the entire input into memory at once.
- **Error Handling:**
    - Consider returning more descriptive error messages in the `decode()` method instead of throwing a generic `RuntimeException`.
    - Implement better validation to avoid injection attacks on the decoded strings.