For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/boiler-chart/boiler-chart.component.ts' with name 'boiler-chart.component.ts' where below a part of it is displayed...

```typescript
 series: [{
   name: 'Heizung Rücklauf',
   data: this.heatingInTempMinMax,
   type: 'arearange',
   lineWidth: 2,
   color: '#2596be',
   fillOpacity: 0.5,
   zIndex: 0,
   marker: {
     enabled: false
   }
 }, 
 {
   name: 'Heizung Vorlauf',
   data: this.heatingOutTempMinMax,
   type: 'arearange',
   lineWidth: 2,
   color: '#be3c25',
   fillOpacity: 0.5,
   zIndex: 1,
   marker: {
     enabled: false
   }
 }]
```

Explain the purpose of the `arearange` chart type used for the "Heizung Rücklauf" and "Heizung Vorlauf" series. What kind of data is suitable for this chart type, and what does `zIndex` control in this context?