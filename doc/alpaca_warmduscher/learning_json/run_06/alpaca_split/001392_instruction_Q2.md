For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/email/EmailService.java' with name 'EmailService.java'... 
Consider the following code snippet:
```java
@ResponseBody
public String send(
        @RequestParam(defaultValue = "Test from raspberry") String subject,
        @RequestParam(defaultValue = "This is a test only") String content) {
    return mailSend.send(subject, content);
}
```
What does the `@ResponseBody` annotation do in this context, and what would happen if it were removed?  Explain the implications for the HTTP response.