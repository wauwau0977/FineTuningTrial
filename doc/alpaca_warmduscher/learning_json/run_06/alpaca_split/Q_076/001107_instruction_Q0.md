You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary
This code defines a service `MailSend` responsible for sending email notifications. It encapsulates the email sending logic, including establishing a connection to an SMTP server (specifically Gmail), creating and configuring the email message, and handling potential exceptions during the sending process. The service retrieves email configuration (sender, password, recipients) from application properties.

## 2. File Information
- **File Location:** Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/MailSend.java
- **Class Name(s):** `MailSend`

## 3. Functional Requirements
- **Primary Operations**:
    - Send an email with a specified subject and content to a default list of recipients.
    - Send an email with a specified subject and content to a custom list of recipients.
- **User Inputs & Outputs**:
    - **Inputs:** Subject (String), Content (String), Receiver Email Addresses (String).
    - **Outputs:** Success message (String) upon successful email sending.  Throws a `RuntimeException` if sending fails, or a `ThException` if configuration is invalid.
- **Workflow/Logic**:
    1.  Retrieve email configuration (sender, password, recipients) from application properties.
    2.  Construct a `Session` object with SMTP server details (Gmail specific) and authentication credentials.
    3.  Create a `MimeMessage` object.
    4.  Set the sender, recipient(s), subject, and content of the message.
    5.  Use `Transport` to send the message.
    6.  Log the success/failure of sending the email.
- **External Interactions**:
    - SMTP server (Gmail) communication for sending emails.
- **Edge Cases Handling**:
    - **Invalid Configuration**: If the email sender, password, or receiver list is empty, a `ThException` is thrown.
    - **MessagingException**: Handles `MessagingException` during email sending and throws a `RuntimeException`.

## 4. Non-Functional Requirements
- **Performance**: Email sending should complete within a reasonable timeframe (e.g., less than 10 seconds) under normal network conditions.
- **Security**: Sensitive information like email password should be securely stored and handled (e.g., using environment variables or a secrets management system).
- **Maintainability**: The code is relatively modular and easy to understand. Configuration parameters are externalized.
- **Reliability & Availability**: The service should handle network errors and SMTP server issues gracefully and potentially implement retry mechanisms (not currently implemented).

## 5. Key Components
- **`send(String subject, String content)`**: Sends an email to the default recipient(s) specified in the configuration.
- **`send(String subject, String content, String receiverMails)`**: Sends an email to a specified list of recipients.
- **Session Creation**: Establishes a connection to the SMTP server and authenticates the sender.
- **Message Creation**: Constructs the email message with sender, recipients, subject, and content.
- **Error Handling**: Uses try-catch blocks to handle `MessagingException` and throws a `RuntimeException` to signal sending failures.
- **Logging**: Logs successful and failed email sending attempts.

## 6. Dependencies

### 6.1 Core Language Features
- Java 8 or higher
- Standard Java libraries:
    - `java.util.Properties`
    - `javax.mail.*`
    - `javax.mail.internet.*`
    - `java.time.LocalDateTime`

### 6.2 External Frameworks & Libraries
- **org.apache.commons.lang3**: Utilized for string validation (`StringUtils.isEmpty`).
- **org.slf4j**: Used for logging.
- **Spring Framework**: Used for dependency injection (@Service, @Value)

### 6.3 Internal Project Dependencies
- **`ThException`**: Custom exception class, likely defined within the Warmduscher project.

## 7. Potential Improvements
- **Performance Enhanecements:** Consider using asynchronous email sending to avoid blocking the main thread.
- **Security Improvements:**
    - Store email credentials securely (e.g., using environment variables, a secrets management system, or encrypted configuration files).
    - Consider using OAuth 2.0 for authentication with Gmail instead of storing the password directly.
- **Scalability Considerations:** Implement a message queue (e.g., RabbitMQ, Kafka) to buffer email requests and allow for horizontal scaling of the email sending service.
- **Retry Mechanism**: Implement a retry mechanism with exponential backoff to handle temporary network errors or SMTP server issues.
- **Configuration**: Provide more flexible configuration options, such as the ability to specify the SMTP server host and port.
- **Error Handling**: More specific error handling and logging of the exception information.
- **Testing**: Add unit tests to verify the functionality and error handling of the service.