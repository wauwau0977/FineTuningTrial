For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/boiler-chart/boiler-chart.component.ts' with name 'boiler-chart.component.ts'... 

Consider the following code snippet related to the `chartOptionsWindGustMeteo` configuration:

```typescript
 series: [{
   name: 'Wind Spitze (Meteo Schweiz)',
   type: 'line',
   data: this.windGustMeteoSwiss,
   color: '#2596be',
 }]
```

If `this.windGustMeteoSwiss` is an empty array, what will be displayed on the chart, and why?  What could you do in the component to handle this scenario more gracefully from a user experience perspective?