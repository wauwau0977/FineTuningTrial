For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/MailSend.java' with name 'MailSend.java'... 
The `send` method includes a `try-catch` block that catches `MessagingException` and throws a `RuntimeException`. However, the code doesn’t log any information about the caught exception before throwing the new one.

Considering best practices for error handling and debugging, what information *should* you log within the `catch` block, and why is this important?  How would you modify the code to implement this logging?