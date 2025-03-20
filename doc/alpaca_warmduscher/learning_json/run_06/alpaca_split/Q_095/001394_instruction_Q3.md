For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/email/EmailService.java' with name 'EmailService.java' where below a part of it is displayed...
```java
   @RequestMapping("/send")
   @ResponseBody
   public String send(
           @RequestParam(defaultValue = "Test from raspberry") String subject,
           @RequestParam(defaultValue = "This is a test only") String content) {
       return mailSend.send(subject, content);
   }
```
What do the `@RequestMapping` and `@ResponseBody` annotations do in this method, and how do they contribute to the functionality of this endpoint?