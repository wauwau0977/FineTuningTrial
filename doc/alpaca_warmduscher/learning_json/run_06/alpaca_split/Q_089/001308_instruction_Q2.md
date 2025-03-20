For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/DateTimeConfig.java' with name 'DateTimeConfig.java'... 
Examine the following code snippet:
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
What is the primary purpose of creating a `Formatter` bean like this, and how does it integrate with Spring's data binding process? Explain how a request parameter (e.g., a date string from an HTTP request) would be converted into a `LocalDate` object using this bean.