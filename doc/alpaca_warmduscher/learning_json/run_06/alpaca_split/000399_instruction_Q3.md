For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/boiler-chart/boiler-chart.component.ts' with name 'boiler-chart.component.ts' where below a part of it is displayed... 

```typescript
   series: [{
     name: 'Sole Eintritt',
     data: this.soleInTempMinMax,
     type: 'arearange',
     lineWidth: 2,
     color: '#2596be',
     fillOpacity: 0.5,
     zIndex: 0,
     marker: {
       enabled: false
     }
   }, {
     name: 'Sole Austritt',
     data: this.soleOutTempMinMax,
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

What is the purpose of the `zIndex` property within the series configuration for the 'SoleTemp' chart, and how does it affect the visual rendering of the chart?