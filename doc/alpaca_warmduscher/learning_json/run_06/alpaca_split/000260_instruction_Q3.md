For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/utils-service.service.spec.ts' with name 'utils-service.service.spec.ts' where below a part of it is displayed...

```typescript
it('find interval: 1 week 10 data points --> 1d', () => {
   let interval: Interval = service.getIntervalInSecondsForMaxDataPoints(10, new Date(2021, 1, 1), new Date(2021, 1, 8));
   console.log(interval);
   expect(interval).not.toBeNull();
   expect(interval.key).toEqual("1d");
});
```

What is the purpose of `expect(interval.key).toEqual("1d");`? Explain what this assertion is verifying, and how it relates to the function being tested.