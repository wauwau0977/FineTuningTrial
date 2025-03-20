For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/CorsFilter.java' with name 'CorsFilter.java' where below a part of it is displayed... 

```java
@Override
public void doFilter(ServletRequest request, ServletResponse r, FilterChain chain) throws IOException, ServletException {
    HttpServletResponse response = (HttpServletResponse) r;
    // ... CORS header additions ...
    chain.doFilter(request, response);
}
```

Explain the role of the `FilterChain` and what `chain.doFilter(request, response)` accomplishes within the `doFilter` method.