For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/utils-service.service.spec.ts' with name 'utils-service.service.spec.ts'... 
Consider the following snippet, representing a hypothetical part of the `getIntervalInSecondsForMaxDataPoints` implementation:

```typescript
const secondsInDay = 86400;
const calculatedIntervalSeconds = totalSeconds / dataPoints;

if (calculatedIntervalSeconds <= secondsInDay) {
  return "1d";
}
```

What potential issues could arise from using a *literal* value like `86400` (seconds in a day) directly in the comparison? How could you improve this code to make it more robust and maintainable?