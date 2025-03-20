For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/boiler-chart/boiler-chart.component.ts' with name 'boiler-chart.component.ts'... 

Examine the following code:

```typescript
 chartOptionsSoleTemp: Highcharts.Options = {
   // ... (other configurations) ...
   series: [{
     name: 'Sole Eintritt',
     data: this.soleInTempMinMax,
     type: 'arearange',
     // ...
   }, {
     name: 'Sole Austritt',
     data: this.soleOutTempMinMax,
     type: 'arearange',
     // ...
   }]
   // ... (other configurations) ...
}
```

What is the purpose of using `type: 'arearange'` for both 'Sole Eintritt' and 'Sole Austritt' series? Explain what an area range chart represents, and how it’s being used to visualize the data in this context. What kind of data is expected in `this.soleInTempMinMax` and `this.soleOutTempMinMax` to make this visualization effective?