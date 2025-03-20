For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/MailSend.java' with name 'MailSend.java' where below a part of it is displayed... 
```java
   @Value("${thserver.mail.sender}")
   private String mailSender = "patrick.heusser.raspberry@gmail.com";
   @Value("${thserver.mail.password}")
   private String mailPassword;
   @Value("${thserver.mail.receivers}")
   private String receiverMailsDefault;
```
What is the purpose of using `@Value` annotation here and how does it relate to the application's configuration? Explain how these values are likely being provided to the `MailSend` class.