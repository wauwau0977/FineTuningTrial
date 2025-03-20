For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/MailSend.java' with name 'MailSend.java'... 
The `send` method accepts `receiverMails` as a String.  Consider this line within the method: `message.addRecipients(Message.RecipientType.TO, InternetAddress.parse(receiverMails, true));`

What potential issues could arise from directly parsing the `receiverMails` string, and how would you mitigate them to ensure the application handles invalid or malicious email addresses safely and reliably?