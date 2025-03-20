For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/email/EmailService.java' with name 'EmailService.java'... 
The `EmailService` class utilizes constructor injection:
```java
public EmailService(MailSend mailSend) {
    this.mailSend = mailSend;
}
```
Explain the benefits of using constructor injection in this scenario, compared to field injection (@Autowired on the `mailSend` field).  Specifically, consider testability and dependency management.