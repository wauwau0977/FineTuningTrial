For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/DateTimeConfig.java' with name 'DateTimeConfig.java' where below a part of it is displayed...

```java
   @Bean
   public FormattingConversionService conversionService() {
       DefaultFormattingConversionService conversionService =
               new DefaultFormattingConversionService(false);
       DateTimeFormatterRegistrar registrar = new DateTimeFormatterRegistrar();
       registrar.setDateFormatter(dateFormat);
       registrar.setDateTimeFormatter(dateTimeFormat);
       registrar.registerFormatters(conversionService);
       return conversionService;
   }
```

Explain the role of `FormattingConversionService` and `DateTimeFormatterRegistrar` in this method. How does this method contribute to Spring's ability to handle date and time conversions?