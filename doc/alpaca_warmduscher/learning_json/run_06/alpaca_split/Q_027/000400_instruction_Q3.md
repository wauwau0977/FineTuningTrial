For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/boiler-chart/boiler-chart.component.ts' with name 'boiler-chart.component.ts' where below a part of it is displayed...

```typescript
 chartOptionsSoleDeltaTemp: Highcharts.Options = {
   series: [{
     name: 'Sole Temperatur Unterschied',
     data: this.soleTempDelta,
     type: 'arearange',
     lineWidth: 2,
     color: '#2596be',
     fillOpacity: 0.5,
     zIndex: 0,
     marker: {
       enabled: false
     },
     zones: [{
       value: 0,
       color: '#2596be'
     }, {
       color: '#be3c25'
     }]
   }],
```

Explain the purpose of the `zones` array within the `series` configuration for the `chartOptionsSoleDeltaTemp` chart, and how it affects the visual representation of the data?