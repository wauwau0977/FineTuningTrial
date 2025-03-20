For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/overview-current/overview-current-gauge.component.ts' with name 'overview-current-gauge.component.ts' where below a part of it is displayed... 

```typescript
gaugeChartOptions: Highcharts.Options = {
   chart: {
     type: 'gauge',
     plotBorderWidth: 0,
     plotShadow: false
   },
   title: {
     text: 'Speedometer'
   },
   pane: {
     startAngle: -150,
     endAngle: 150,
   },
   // the value axis
   yAxis: [{
     min: 20,
     max: 65,
     minorTickInterval: 'auto',
     minorTickWidth: 1,
     minorTickLength: 10,
     minorTickPosition: 'inside',
     minorTickColor: '#666',
     tickPixelInterval: 30,
     tickWidth: 2,
     tickPosition: 'inside',
     tickLength: 10,
     tickColor: '#666',
     labels: {
       step: 2,
       //rotation: 'auto'
     },
     title: {
       text: 'km/h'
     },
     plotBands: [{
       from: 20,
       to: 30,
       color: '#55BF3B' // green
     }, {
       from: 30,
       to: 50,
       color: '#DDDF0D' // yellow
     }, {
       from: 50,
       to: 65,
       color: '#DF5353' // red
     }]
   }],
   series: [{
     name: 'Speed',
     type: 'gauge',
     data: [80],
     tooltip: {
       valueSuffix: ' km/h'
     }
   }]
 }
```

Explain the purpose of the `gaugeChartOptions` property and how the `yAxis` and `series` configurations contribute to creating the gauge chart. Specifically, what do the `plotBands` define?