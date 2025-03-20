For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/MailSend.java' with name 'MailSend.java' where below a part of it is displayed... 
```java
   try {
       Message message = new MimeMessage(session);
       message.setFrom(new InternetAddress(mailSender));
       message.addRecipients(Message.RecipientType.TO, InternetAddress.parse(receiverMails, true));
       message.setSubject(subject);
       message.setText(content);
       Transport.send(message);
       log.info("Sent mail to=" + receiverMails + " subject=" + subject + " content=" + content);
   } catch (MessagingException e0) {
       RuntimeException e1 = new RuntimeException("Could not send email to " + receiverMails, e0);
       log.error("Email not sent", e1);
       throw e1;
   }
```
What is the purpose of the `try-catch` block surrounding the email sending process, and how does it handle potential `MessagingException` errors? Explain the actions taken when a `MessagingException` occurs.