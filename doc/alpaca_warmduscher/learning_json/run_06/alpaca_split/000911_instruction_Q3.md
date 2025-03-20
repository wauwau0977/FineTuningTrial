For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/entity/SessionDevice.java' with name 'SessionDevice.java' where below a part of it is displayed...
```java
   @Override
   public boolean equals(Object o) {
       if (this == o) return true;
       if (o == null || getClass() != o.getClass()) return false;
       SessionDevice that = (SessionDevice) o;
       return sessionId != null ? sessionId.equals(that.sessionId) : that.sessionId == null;
   }

   @Override
   public int hashCode() {
       return sessionId != null ? sessionId.hashCode() : 0;
   }
```
Explain the purpose of overriding the `equals()` and `hashCode()` methods in this class.  How do these overrides contribute to the correct functioning of collections (e.g., `HashSet`, `HashMap`) when working with `SessionDevice` objects?