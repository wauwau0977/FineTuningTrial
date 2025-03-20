You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This Java class `MavenWrapperDownloader` is a standalone utility designed to download the Maven Wrapper JAR file. It checks for a `maven-wrapper.properties` file in the project's `.mvn/wrapper` directory. If present, it reads the `wrapperUrl` property to determine the download URL. Otherwise, it uses a default URL. The downloaded JAR is saved to `.mvn/wrapper/maven-wrapper.jar`. This allows projects to utilize the Maven Wrapper without requiring a full Maven installation, simplifying the build process.

## 2. File Information

- **File Location:** `Warmduscher/thserver/.mvn/wrapper/MavenWrapperDownloader.java`
- **Class Name(s):** `MavenWrapperDownloader`

## 3. Functional Requirements

- **Primary Operations**: Download the Maven Wrapper JAR file.
- **User Inputs & Outputs**:
    - **Input:** The program takes a single command-line argument, which represents the base directory of the project.
    - **Output:** The program downloads `maven-wrapper.jar` to `.mvn/wrapper/` within the project's base directory. It also outputs informational messages to the console regarding the download process.
- **Workflow/Logic**:
    1.  Accept project base directory as a command-line argument.
    2.  Check for the existence of `maven-wrapper.properties` file in `.mvn/wrapper/`.
    3.  If `maven-wrapper.properties` exists, read the `wrapperUrl` property to determine the download URL. If the property is not present, use the default download URL.
    4.  Create the output directory `.mvn/wrapper` if it doesn’t exist.
    5.  Download `maven-wrapper.jar` from the determined URL and save it to `.mvn/wrapper/maven-wrapper.jar`.
    6.  Print messages to the console indicating the status of the download.
- **External Interactions**:
    - **Network:** Downloads a file from a specified URL using HTTP.
    - **File System:** Reads and writes files to the local file system.
- **Edge Cases Handling**:
    - **File Not Found:** Handles the case where `maven-wrapper.properties` does not exist.
    - **Invalid URL:** Handles potential exceptions when opening the URL (e.g., invalid URL format, network connection issues).
    - **Directory Creation Failure:** Handles the case where the output directory cannot be created.
    - **File Download Failure:** Handles potential exceptions during file download (e.g., network interruption).
    - **Property Not Found**: Handles case where `wrapperUrl` property is not found in the properties file

## 4. Non-Functional Requirements

- **Performance**: The download process should be relatively quick, completing within a reasonable timeframe (e.g., less than 30 seconds) for a standard network connection.
- **Scalability**: Not directly applicable, as this is a standalone utility.
- **Security**: Ensure the download URL is from a trusted source to prevent downloading malicious files.
- **Maintainability**: Code should be well-structured and commented for easy understanding and modification.
- **Reliability & Availability**: The utility should be reliable and consistently download the Maven Wrapper JAR without errors.
- **Usability**: The utility is designed to be a command-line tool with simple usage: `java MavenWrapperDownloader <project_base_directory>`.
- **Compliance**: The license specified in the source code header should be adhered to (Apache 2.0 License).

## 5. Key Components

- **`main(String args[])`:** The entry point of the program. It handles the overall workflow, including reading the project directory, checking for the properties file, determining the download URL, and initiating the download process.
- **`downloadFileFromURL(String urlString, File destination)`:** Downloads a file from a given URL and saves it to the specified destination.  Uses `java.nio.channels` for efficient file transfer.
- **Error Handling:** `try-catch` blocks are used throughout the code to handle potential `IOExceptions` during file operations and network access.
- **`Properties` class:** Used to read the `wrapperUrl` property from the `maven-wrapper.properties` file.
- **`File` class**: Used to represent files and directories, and to perform file system operations.
- **No subclasses are defined.**
- **Modules:** The code is a single standalone class with no modular structure.

## 6. Dependencies

### 6.1 Core Language Features

- **Data structures:** `File`, `Properties`
- **File handling:** Reading and writing files, creating directories.
- **Networking:** `URL`, `ReadableByteChannel`, `Channels`
- **Input/Output**: `FileInputStream`, `FileOutputStream`

### 6.2 External Frameworks & Libraries

- None. The code uses only standard Java libraries.

### 6.3 Internal Project Dependencies

- None.  This is a standalone utility.

## 7. Potential Improvements

- **Performance Enhancements:**
    - Consider using a caching mechanism to avoid redundant downloads if the JAR already exists and is up-to-date.
- **Code Readability:**
    - Add more comments to explain complex logic.
- **Security Improvements:**
    - Validate the downloaded JAR file's checksum to ensure its integrity.
    - Sanitize the downloaded URL before use.
- **Scalability Considerations:**
    - Not applicable for this standalone utility.
- **Logging**: Implement a proper logging framework (e.g., Log4j, SLF4J) to provide more detailed information about the download process and any errors encountered.
- **Command-line arguments validation**: Add validation of the input command-line argument to ensure it is a valid directory.