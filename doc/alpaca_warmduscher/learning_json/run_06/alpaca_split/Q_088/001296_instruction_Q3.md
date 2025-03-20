For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/CorsFilter.java' with name 'CorsFilter.java' where below a part of it is displayed... 

```java
response.addHeader("Access-Control-Allow-Headers", "Content-Type, *, X-Requested-With"); // X-Requested-With avoid not allowed
```

What is the purpose of including "X-Requested-With" in the `Access-Control-Allow-Headers` and why is it commented as avoiding a potential issue?