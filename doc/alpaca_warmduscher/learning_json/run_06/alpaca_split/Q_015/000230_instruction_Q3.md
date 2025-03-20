For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/heating-data.service.ts' with name 'heating-data.service.ts' where below a part of it is displayed...
```typescript
 getMeteoSwissHistorical(evictCache: boolean, from: Moment, to: Moment, maxRows: number, groupEveryNthSecond: number, stationIds?: Set<string>, doNotCache?: boolean) {
   let p = new HttpParams()
     .set('start', from.toJSON())
     .set('end', to.toJSON())
     .set('maxRows', maxRows)
     .set('groupEveryNthSecond', groupEveryNthSecond)
   ;
   if (stationIds != null) {
     let stationIdList: string = '';
     stationIds.forEach(s => stationIdList = stationIdList + s + ",");
     p = p.set('stationId', stationIdList);
   }
   return this.cacheService.get(
     HeatingDataService.CACHE_KEY_METEO_HISTORICAL,
     () => this.http.get(this.serviceBaseURL + '/meteo-swiss/getBetweenDates', {params: p}),
     evictCache, doNotCache);
 }
```
Explain the purpose of this `getMeteoSwissHistorical` method. Specifically, what does it do with the `stationIds` parameter, and what is the function of the optional `doNotCache` parameter? How are the parameters used to construct the HTTP request?