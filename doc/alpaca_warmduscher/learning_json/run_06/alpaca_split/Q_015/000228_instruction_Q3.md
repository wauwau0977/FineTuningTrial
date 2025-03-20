For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/heating-data.service.ts' with name 'heating-data.service.ts' where below a part of it is displayed...
```typescript
 private static readonly CACHE_KEY_HISTORICAL: string = "CACHE_KEY_HISTORICAL";
 private static readonly CACHE_KEY_CURRENT: string = "CACHE_KEY_CURRENT";
 ...
 return this.cacheService.get(
     HeatingDataService.CACHE_KEY_HISTORICAL,
     () => this.http.get(this.serviceBaseURL + '/heatpump-data/getBetweenDates', {params: p}),
     evictCache);
```
What is the purpose of defining these `CACHE_KEY_*` constants, and how are they used in conjunction with the `cacheService` to improve the performance or efficiency of the service?