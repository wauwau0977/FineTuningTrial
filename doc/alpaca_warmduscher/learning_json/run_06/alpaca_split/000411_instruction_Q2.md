For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/boiler-chart/boiler-chart.component.ts' with name 'boiler-chart.component.ts'... 

Examine the `chartOptionsHeatingDeltaTemp` configuration. Notice the `zones` property within the series definition:

```typescript
zones: [{
  value: 0,
  color: '#2596be'
}, {
  color: '#be3c25'
}]
```

What is the purpose of using `zones` in this configuration, and how does it visually affect the chart? What data characteristic is this intended to highlight?