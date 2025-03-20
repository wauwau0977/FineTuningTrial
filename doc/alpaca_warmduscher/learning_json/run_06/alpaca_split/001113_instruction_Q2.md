For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/MailSend.java' with name 'MailSend.java'... 
Consider this code snippet within the `send` method:

```java
Properties prop = new Properties();
// Sending email from gmail
// String host = "mail.your-server.de";
String host = "smtp.gmail.com";
// Port of SMTP
String port = "587";
prop.put("mail.smtp.socketFactory.port", port);
prop.put("mail.smtp.socketFactory.class", "javax.net.ssl.SSLSocketFactory");
```

What are the implications of hardcoding these properties (host, port, socket factory) directly within the code?  How could you improve this design for better flexibility and maintainability, especially considering potential changes to the email server configuration or the need to support different email providers?