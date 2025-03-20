For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/entities/soleInOutDeltaInOperationStatEntity.ts' with name 'soleInOutDeltaInOperationStatEntity.ts'... 
Looking at the `emptyInstance()` method:

```typescript
static emptyInstance() {
   return new SoleInOutDeltaInOperationStatEntity(new Date(), new Date(), 0, 0, 0, false, 0);
 }
```

What are the implications of creating a new `Date()` object for both `measurementDateStart` and `measurementDateEnd` each time `emptyInstance()` is called? How might this affect comparisons or long-term data storage?