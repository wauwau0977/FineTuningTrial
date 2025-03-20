For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/utils/mutex/GlobalSynced.java' with name 'GlobalSynced.java' where below a part of it is displayed... 

```java
public void requestOperation(MutexOperation<T> m) {
    try {
        // lock and potentially wait if required
        reentrantLock.lock();
        if (hooks != null) {
            hooks.before(syncedObject);
        }
        m.operateGlobalSynced(syncedObject);
    } catch (Throwable t1) {
        try {
            if (hooks != null) {
                hooks.after(syncedObject); // always call after
            }
        } catch (Throwable t2) {
            log.error("Error in after hook", t2);
        }
    } finally {
        reentrantLock.unlock();
    }
}
```

What is the purpose of the `try-catch-finally` block in the `requestOperation` method, and why is it important that the `hooks.after()` method is *always* called, even if an exception occurs during the operation?