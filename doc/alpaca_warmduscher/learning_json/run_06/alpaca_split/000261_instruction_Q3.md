For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/utils-service.service.spec.ts' with name 'utils-service.service.spec.ts' where below a part of it is displayed...

```typescript
it('find interval: 1 year 366 data points --> 1d', () => {
   let interval: Interval = service.getIntervalInSecondsForMaxDataPoints(366, new Date(2021, 1, 1), new Date(2022, 1, 1));
   console.log(interval);
   expect(interval).not.toBeNull();
   expect(interval.key).toEqual("1d");
});
```

Considering the pattern observed in the test cases, and specifically this test case, what can you infer about the logic of `service.getIntervalInSecondsForMaxDataPoints` regarding the relationship between the number of data points and the resulting interval key?