For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/utils-service.service.ts' with name 'utils-service.service.ts'... 
Consider the following code within `getStandardIntervalsImpl`:
```typescript
let intervals: Interval[] = [];
// ... push intervals ...
Interval.sort(intervals);
return intervals;
```
Discuss the potential benefits and drawbacks of creating and sorting the `Interval` array *every* time the `getStandardIntervals` method is called. Suggest an alternative approach and explain how it would address these concerns.