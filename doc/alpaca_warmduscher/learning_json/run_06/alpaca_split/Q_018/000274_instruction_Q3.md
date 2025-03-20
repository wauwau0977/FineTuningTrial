For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/utils-service.service.ts' with name 'utils-service.service.ts' where below a part of it is displayed...
```typescript
private static getStandardIntervalsImpl(): Interval[] {
  let intervals: Interval[] = [];
  let second = 1;
  let minute = second * 60;
  let hour = minute * 60;
  let day = hour * 24;
  let month = 30.436875 * day; // in average (special years, normal years, etc)
  // ...rest of the function
}
```
What is the purpose of calculating `month` as `30.436875 * day`? Why isn't a fixed value (e.g., 30 days) used instead?