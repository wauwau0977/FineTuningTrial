You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This Java class, `MavenWrapperDownloader`, is a standalone application designed to download the `maven-wrapper.jar` file, which is essential for using the Maven Wrapper. It checks for a custom download URL in a `maven-wrapper.properties` file. If found, it uses that URL; otherwise, it downloads the jar from the default Apache Maven repository. The downloaded jar is saved to the `.mvn/wrapper` directory of the current project. It is primarily used in projects utilizing the Maven Wrapper to ensure the necessary bootstrapping components are available.

## 2. File Information

- **File Location:** `Warmduscher/thserver/.mvn/wrapper/MavenWrapperDownloader.java`
- **Class Name(s):** `MavenWrapperDownloader`

## 3. Functional Requirements

- **Primary Operations:** Downloads the `maven-wrapper.jar` file.
- **User Inputs & Outputs:**
    - **Input:** Command-line argument representing the base project directory.
    - **Output:** The `maven-wrapper.jar` file placed in the `.mvn/wrapper` directory. Console output indicating the download status (success/failure).
- **Workflow/Logic:**
    1. Receives the base project directory as a command-line argument.
    2. Checks for the existence of the `maven-wrapper.properties` file in the `.mvn/wrapper` directory.
    3. If the properties file exists, it reads the `wrapperUrl` property.
    4. If the `wrapperUrl` property is present, it uses that URL for the download. Otherwise, it uses the default download URL.
    5. Downloads the `maven-wrapper.jar` from the determined URL.
    6. Saves the downloaded file to the `.mvn/wrapper` directory.
    7. Outputs status messages to the console indicating the progress of the download.
- **External Interactions:**
    - Makes an HTTP request to download the `maven-wrapper.jar` file.
    - Reads a properties file (`.mvn/wrapper/maven-wrapper.properties`).
    - Creates a directory (`.mvn/wrapper`) if it does not exist.
    - Writes the downloaded jar file to disk.
- **Edge Cases Handling:**
    - **File Not Found:** Handles the case where the `maven-wrapper.properties` file does not exist.
    - **Invalid URL:** Handles potential exceptions during the HTTP request (e.g., invalid URL, network errors).
    - **Directory Creation Failure:** Handles the case where the `.mvn/wrapper` directory cannot be created.
    - **IO Exceptions:** Catches and handles potential IO exceptions during file reading/writing.

## 4. Non-Functional Requirements

- **Performance:** The download should complete within a reasonable timeframe, typically a few seconds depending on network conditions.
- **Scalability:** The downloader is a standalone application and doesn't require scalability.
- **Security:** No sensitive data is handled. Ensure the default and custom URLs point to trusted sources.
- **Maintainability:** The code is relatively straightforward and well-commented.
- **Reliability & Availability:** The downloader should reliably download the jar unless external factors (network connectivity, server unavailability) prevent it.
- **Usability:** The application is designed to be used as a part of the build process, primarily by developers.
- **Compliance:** The code is licensed under the Apache License 2.0.

## 5. Key Components

- **`main(String[] args)`:** The entry point of the application. Handles command-line arguments, file existence checks, property loading, and error handling.
- **`downloadFileFromURL(String urlString, File destination)`:**  Downloads a file from a given URL and saves it to the specified destination. Handles the network connection and file writing.
- **Logic Flows:** The primary logic flow involves checking for the properties file, determining the download URL, and downloading/saving the jar file.
- **Error Handling:** The code uses `try-catch` blocks to handle potential IO exceptions and network errors.
- **Classes:**  Only one class, `MavenWrapperDownloader`, is defined. No subclasses.
- **Modules:** No explicit modules. The code is a single standalone application.

## 6. Dependencies

### 6.1 Core Language Features

- **File I/O:**  Used for reading the properties file and writing the downloaded jar.
- **Properties:** Used to read the download URL from the configuration file.
- **Data Structures:**  Basic use of `String` and `File` objects.
- **Networking:**  Uses `URL` and `ReadableByteChannel` to download the file.

### 6.2 External Frameworks & Libraries

- **None:** The code utilizes only core Java libraries.

### 6.3 Internal Project Dependencies

- **None:**  The code is self-contained and doesn't depend on any other parts of the Warmduscher project.

## 7. Potential Improvements

- **Performance Enhancements:**  Consider using a more efficient download mechanism, such as a buffered input stream, to improve download speed.
- **Code Readability:**  While already reasonably readable, consider adding more comments to explain complex logic.
- **Security Improvements:** Validate the downloaded file's checksum to ensure its integrity and prevent potential tampering.
- **Scalability Considerations:** Not applicable, as this is a single-use downloader.
- **Logging:** Implement a proper logging mechanism instead of relying solely on `System.out.println`. This would provide more detailed information for debugging and monitoring.
- **Testing:** Add unit tests to verify the functionality of the downloader, including the handling of different scenarios (e.g., invalid URL, network errors).