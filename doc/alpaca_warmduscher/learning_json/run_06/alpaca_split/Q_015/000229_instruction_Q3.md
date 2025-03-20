For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/heating-data.service.ts' with name 'heating-data.service.ts' where below a part of it is displayed...
```typescript
 static convertDate(utcDateText: string) {
   let x1 = moment.utc(utcDateText);
   return x1.toDate();
 }
 static convertDateToTime(utcDateText: string) {
   let x1 = moment.utc(utcDateText);
   return x1.toDate().getTime();
 }
```
What is the purpose of the `convertDate` and `convertDateToTime` methods, and why are they using the `moment.js` library to perform the date conversions? What differences are there between the returned values of both methods?