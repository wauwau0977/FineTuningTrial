For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/services/info/InfoService.java' with name 'InfoService.java'... 
Considering the `getInfo()` method:
```java
@RequestMapping("/general")
@ResponseBody
public InfoBean getInfo() {
    return infoBean;
}
```
What are the potential advantages and disadvantages of using dependency injection (as demonstrated with `infoBean`) in this context, and how might you test this method effectively?