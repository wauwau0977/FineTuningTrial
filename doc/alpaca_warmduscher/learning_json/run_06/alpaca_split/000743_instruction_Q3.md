For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/data/meteoswiss/impl/MeteoDataServiceImpl.java' with name 'MeteoDataServiceImpl.java' where below a part of it is displayed...
```java
   private String callService(String url) {
       RestTemplate restTemplate = new RestTemplate();
       // important: set UTF8, otherwise RestTemplate will do ISO
       restTemplate.getMessageConverters().add(0, new StringHttpMessageConverter(StandardCharsets.UTF_8));
       return restTemplate.getForObject(url, String.class);
   }
```
What is the purpose of adding a `StringHttpMessageConverter` with `StandardCharsets.UTF_8` to the `RestTemplate`? Explain the potential issue without it, and why UTF-8 is chosen as the character encoding.