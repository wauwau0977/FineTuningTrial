You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This Java class `MailSend` provides functionality to send emails using SMTP. It’s designed to be a Spring-managed service, receiving configuration via `@Value` annotations (sender email, password, recipient emails). It supports sending emails to multiple recipients.  Error handling is implemented, throwing exceptions in case of invalid configuration or email sending failures. The class uses TLS for secure email transmission.

## 2. File Information

- **File Location:** `Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/MailSend.java`
- **Class Name(s):** `MailSend`

## 3. Functional Requirements

- **Primary Operations**: Sends emails with a specified subject and content to one or more recipients.
- **User Inputs & Outputs**:
    - **Inputs:**
        - `subject`: String - The subject of the email.
        - `content`: String - The body of the email.
        - `receiverMails`: String – Comma-separated string of receiver email addresses.  Default receivers are configured through Spring.
    - **Outputs:**
        - Returns "Email sent with success" if the email is sent successfully.
        - Throws a `RuntimeException` or `ThException` if there are configuration issues or errors sending the email.
- **Workflow/Logic**:
    1. Retrieves sender email, password, and default receiver emails from Spring configuration.
    2. Validates configuration (sender, password, and receiver emails are not empty).
    3. Creates SMTP properties (host, port, TLS enablement, authentication).
    4. Creates a JavaMail Session with the configured properties and authentication.
    5. Creates a MimeMessage with the sender, recipients, subject, and content.
    6. Sends the message using the Transport.
    7. Logs a success message or throws an exception if an error occurs.
- **External Interactions**:
    - **SMTP Server:** Interacts with an SMTP server (specifically Gmail's `smtp.gmail.com`) to send emails.
- **Edge Cases Handling**:
    - **Invalid Configuration:** Throws a `ThException` if the sender email, password, or receiver email is missing.
    - **SMTP Connection Errors:** Catches `MessagingException` during email sending and throws a `RuntimeException` with details.
    - **Invalid Receiver Email:**  While the code doesn't validate the format of the receiver email, invalid emails will likely lead to a `MessagingException` caught and re-thrown.



## 4. Non-Functional Requirements

- **Performance**: Email sending time depends on network conditions and SMTP server responsiveness.  No specific performance requirements are defined.
- **Scalability**:  Not designed for high-volume email sending. Scalability considerations would involve using a dedicated email service or queuing system for handling large numbers of emails.
- **Security**: Uses TLS for secure communication with the SMTP server.  Sensitive information (password) is stored in the application configuration and should be protected accordingly.
- **Maintainability**: The code is relatively straightforward and well-structured, with clear separation of concerns.
- **Reliability & Availability**:  Reliability depends on the SMTP server's availability and network connectivity.
- **Usability**: Easy to integrate within the application as a Spring-managed service.
- **Compliance**:  Compliance with email sending policies of the SMTP provider (e.g., Gmail's sending limits and terms of service).

## 5. Key Components

- **`send(String subject, String content)`**: Sends an email with the specified subject and content to the default configured recipients.
- **`send(String subject, String content, String receiverMails)`**: Sends an email with the specified subject and content to the provided list of recipient emails.
- **SMTP Property Configuration:** Sets up the necessary properties for connecting to the SMTP server (host, port, TLS enablement, authentication).
- **Session Creation:** Creates a JavaMail Session with the configured properties and authentication credentials.
- **Message Creation & Sending:** Creates a MimeMessage and sends it using the Transport.
- **Error Handling:** Catches `MessagingException` and throws a `RuntimeException`.

## 6. Dependencies

### 6.1 Core Language Features

- **Data structures:** Strings are used extensively for email addresses, subjects, and content.
- **Exception handling:** `try-catch` blocks are used to handle potential errors during email sending.
- **Logging:** Uses `org.slf4j.Logger` for logging information and errors.

### 6.2 External Frameworks & Libraries

- **Spring Framework:** Uses `@Service` annotation for dependency injection and managing the class as a Spring bean, and `@Value` for injecting configuration properties.
- **JavaMail API (javax.mail):**  Used for creating and sending emails.
- **Apache Commons Lang3:** Used for `StringUtils.isEmpty()` for checking String emptiness.
- **SLF4J:** For logging.

### 6.3 Internal Project Dependencies

- **`ThException`:** Custom exception class used to indicate configuration errors.

## 7. Potential Improvements

- **Performance Enhanecements:** For high-volume email sending, consider using an asynchronous email queuing system (e.g., RabbitMQ, Kafka) to offload email sending from the main application thread.
- **Code Readability:** The code is already reasonably readable.
- **Security Improvements:**
    - Consider using a more secure way to store the email password (e.g., environment variables, encrypted configuration files, secrets management service).
    - Implement input validation to prevent potential injection attacks (e.g., sanitize the subject and content).
- **Scalability Considerations:**  As mentioned above, utilize an asynchronous email queue for scalability.  Consider using a dedicated email service provider (e.g., SendGrid, Mailgun, AWS SES) for increased reliability and scalability.
- **Error Handling:** More specific exception handling could be implemented to provide more informative error messages.
- **Configuration:** Using a dedicated configuration file (e.g., application.properties or application.yml) for SMTP settings can make it easier to manage and update the configuration.