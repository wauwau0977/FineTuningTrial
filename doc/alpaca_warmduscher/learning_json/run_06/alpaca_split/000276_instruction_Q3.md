For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/utils-service.service.ts' with name 'utils-service.service.ts' where below a part of it is displayed...
```typescript
static compare(a: Interval, b: Interval): number {
  if (!a || !b) {
    return 0;
  }
  if (a.intervalInSeconcs === b.intervalInSeconcs) {
    return 0;
  } else {
    return a.intervalInSeconcs > b.intervalInSeconcs ? 1 : -1;
  }
}
static sort(intervals: Interval[]) {
  intervals.sort((a, b) => Interval.compare(a, b));
}
```
Explain the purpose of the `Interval.compare` and `Interval.sort` methods. Why are both needed, and how do they work together?