For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/data/meteoswiss/impl/MeteoDataServiceImpl.java' with name 'MeteoDataServiceImpl.java' where below a part of it is displayed...
```java
   private ResDateValue extractFromJSON(String json, String stationId, String value2Property) {
       DocumentContext parsed = JsonPath.parse(json);
       String basePath = "$[*][?(@.id=='" + stationId + "')].properties";
       String timeStamp = parsed.read(basePath + ".reference_ts");
       TemporalAccessor ta = DateTimeFormatter.ISO_INSTANT.parse(timeStamp);
       Instant i = Instant.from(ta);
       Date measureTimeStamp = Date.from(i);
       Double value1 = parsed.read(basePath + ".value");
       Double value2 = null;
       if (value2Property != null) {
           value2 = parsed.read(basePath + "." + value2Property);
       }
       return new ResDateValue(measureTimeStamp, value1, value2);
   }
```
Explain the purpose of the `extractFromJSON` method. Specifically, describe how it uses `JsonPath` to parse the provided `json` string and extract relevant data based on the `stationId`, and what kind of data is extracted. What role does the `value2Property` argument play?