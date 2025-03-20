For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/overview-current/overview-current-gauge.component.ts' with name 'overview-current-gauge.component.ts' where below a part of it is displayed... 

```typescript
myReload() {
   return this.heatingDataService.getCurrent(false)
     .subscribe((data: any) => {
       this.heatingEntity = HeatingEntity.ofWebService(data);
       this.receivedNewTHValue.emit(data);
     });
 }
```

Explain what the `myReload()` method does and how it interacts with `HeatingDataService` and the `heatingEntity` property.