For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/utils-service.service.ts' with name 'utils-service.service.ts'... 
Consider the following code snippet from the `getStandardIntervalsImpl` method:
```typescript
let month = 30.436875 * day;
// ...
intervals.push(new Interval("1m", "1 month", month));
intervals.push(new Interval("3m", "3 months", 3 * month));
intervals.push(new Interval("6m", "6 months", 6 * month));
```
What is the rationale behind using `30.436875` to calculate the number of seconds in a month? What are the implications of using this approximation, and could it affect the accuracy of the data collection intervals?