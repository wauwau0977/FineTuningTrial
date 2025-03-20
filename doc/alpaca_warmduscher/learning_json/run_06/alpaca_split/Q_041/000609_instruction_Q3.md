For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/overview-current/overview-current.component.ts' with name 'overview-current.component.ts' where below a part of it is displayed...

```typescript
getShowerRecommendation(): String {
   let boilerTemp = this.heatingEntity.boilerTemp;
   if (boilerTemp > 60) {
     return "Super heiss: Die LegionellenSchaltung hat alles gegeben.";
   } else if (boilerTemp > 57) {
     return "Super heiss: Wahrscheinlich wegen Legionellen-Schaltung.";
   } else if (boilerTemp > 55) {
     return "Sehr heiss: Da könnte man ganze Badewannen füllen.";
   } //...and so on
```

What is the purpose of the `getShowerRecommendation()` method, and what does it return? Describe how the method determines the recommendation.