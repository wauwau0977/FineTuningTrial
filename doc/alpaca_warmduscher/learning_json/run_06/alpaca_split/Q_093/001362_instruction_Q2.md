For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/dialogflow/DialogFlowWebhookController.java' with name 'DialogFlowWebhookController.java'... 
Consider this section of the code:

```java
StringWriter stringWriter = new StringWriter();
JsonGenerator jsonGenerator = jacksonFactory.createJsonGenerator(stringWriter);
jsonGenerator.enablePrettyPrint();
jsonGenerator.serialize(response);
jsonGenerator.flush();
return stringWriter.toString();
```

What is the purpose of this code snippet and what are the benefits of using `enablePrettyPrint()`? What alternative approach could you use to achieve the same outcome with less code?