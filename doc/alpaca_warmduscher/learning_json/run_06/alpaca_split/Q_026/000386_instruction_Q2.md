For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/boiler-chart/boiler-chart.component.ts' with name 'boiler-chart.component.ts'... 

The `adjustTimeAndReload()` method is responsible for updating the date range used to fetch data. Looking at the following snippet:

```typescript
 private adjustTimeAndReload() {
   let now = moment();
   let lastActiveSinceSeconds = now.diff(this.lastUserActivationTime, 'seconds');
   let updateDatesRequired = false;
   if (lastActiveSinceSeconds > 180) {
     updateDatesRequired = true;
   }
   console.log('adjustTimeAndReload. ' +
     ' lastActiveSinceSeconds: ' + lastActiveSinceSeconds
     + " updateDatesRequired:" + updateDatesRequired
     + " lastUserActivationTime:" + this.lastUserActivationTime.format());
   if (updateDatesRequired) {
     this.myForm.patchValue({
         customFromDate: moment().subtract(24, "hours").toDate(),
         customFromDateTimePart: moment().format('HH'),
         customToDate: moment().toDate(),
         customToDateTimePart: moment().add(1, "hours").format('HH'),
       }
     );
     this.lastUserActivationTime = now;
     if (this.router.url.indexOf("insights") > 0) {
       // this.snackBar.open("Datum für Graph aktualisiert", '', {
       //  duration: 2000
       // });
     }
     this.calculateAutoInterval();
   }
   this.myReload();
 }
```

What is the purpose of the `lastUserActivationTime` variable, and how does this method use it to determine when to refresh the data displayed in the chart? Explain the logic behind the 180-second threshold.