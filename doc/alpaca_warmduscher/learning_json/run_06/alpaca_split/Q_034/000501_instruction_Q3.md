For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/entities/meteoSwissEntity.ts' with name 'meteoSwissEntity.ts' where below a part of it is displayed...
```typescript
 constructor(public id: string,
             public stationId: string,
             public stationName: string,
             public temperature: number,
             public temperatureMin: number,
             public temperatureMax: number,
             public temperatureMeasureDate: Date,
             public temperatureMeasureDateMin: Date,
             public temperatureMeasureDateMax: Date,
             public windGustSpeed: number,
             public windGustSpeedMin: number,
             public windGustSpeedMax: number,
             public windMeasureDate: Date,
             public windMeasureDateMin: Date,
             public windMeasureDateMax: Date
 ) {
 }
```
What is the purpose of using the `public` keyword for each parameter in the constructor? How does this affect the class members?