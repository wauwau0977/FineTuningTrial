For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/heating-data.service.ts' with name 'heating-data.service.ts'... 
Examine the following methods: 
```typescript
getHistorical(evictCache: boolean, from: Moment, to: Moment, maxRows: number, groupEveryNthSecond: number) {
   let p = new HttpParams()
     .set('start', from.toJSON())
     .set('end', to.toJSON())
     .set('maxRows', maxRows)
     .set('groupEveryNthSecond', groupEveryNthSecond)
   ;
   return this.cacheService.get(
      HeatingDataService.CACHE_KEY_HISTORICAL,
      () => this.http.get(this.serviceBaseURL + '/heatpump-data/getBetweenDates', {params: p}),
      evictCache);
 }
```
What are the potential security implications of directly using `from.toJSON()` and `to.toJSON()` to construct the HTTP parameters? How could these be mitigated?