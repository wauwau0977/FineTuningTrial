For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/web/MyRequestInterceptor.java' with name 'MyRequestInterceptor.java' where below a part of it is displayed...
```java
if (MySessionFilter.isSessionRelevantRequest(request)) {
           SessionRequest sessionRequest = new SessionRequest();
           sessionRequest.setPath(path);
           sessionRequest.setSessionId(sessionId);
           sessionRequest.setClientId(clientId);
           sessionRequest.setClientVersion(clientVersion);
           sessionRequest.setIp(ip);
           sessionRequest.setProcessingTime(dtProcessing);
           sessionRequest.setHttpStatus(String.valueOf(response.getStatus()));
           sessionRequest.setException(ex != null ? ex.getMessage() : null);
           sessionRequestRepository.save(sessionRequest);
           long dtTotal = System.currentTimeMillis() - startTime;
           log.info("Got request and saved it. dtTotal=" + dtTotal + " " + sessionRequest);
       } else {
           log.info("Did receive a request which was not persisted. url=" + path);
       }
```
Explain the purpose of the conditional `if (MySessionFilter.isSessionRelevantRequest(request))` and what data is being saved to the database if the condition is true.