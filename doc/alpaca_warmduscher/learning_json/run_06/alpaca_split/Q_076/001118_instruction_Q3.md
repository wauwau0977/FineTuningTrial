For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/MailSend.java' with name 'MailSend.java' where below a part of it is displayed...
```java
 public String send(String subject, String content, String receiverMails) {
       if (StringUtils.isEmpty(mailSender) || StringUtils.isEmpty(mailPassword) || StringUtils.isEmpty(receiverMails)) {
           String msg = "Did not send email, as the configuration was invalid or no receiver was given.";
           log.error(msg);
           throw new ThException(msg);
       }
       // ... rest of the send method
   }
```
What is the purpose of the initial `if` statement within the `send` method, and why is it important to check for empty values before proceeding with the email sending process? What type of exception is thrown if the condition is met?