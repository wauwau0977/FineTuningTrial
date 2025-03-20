For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/DateTimeConfig.java' with name 'DateTimeConfig.java' where below a part of it is displayed...

```java
   @Bean
   public Formatter<LocalDate> localDateFormatter() {
       return new Formatter<LocalDate>() {
           @Override
           public LocalDate parse(String text, Locale locale) throws ParseException {
               return LocalDate.parse(text, dateFormat);
           }
           @Override
           public String print(LocalDate object, Locale locale) {
               return dateFormat.format(object);
           }
       };
   }
```

What is the purpose of creating a custom `Formatter` for `LocalDate`? How does this `Formatter` utilize the `dateFormat` defined earlier, and why is a custom implementation necessary instead of simply relying on Spring's default date handling?