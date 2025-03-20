For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/app.module.ts' with name 'app.module.ts' where below a part of it is displayed...
```typescript
export const routes: Routes = [
 {path: 'dashboard', component: OverviewCurrentComponent},
 {path: 'insights', component: BoilerChartComponent},
 {path: 'about', component: AboutComponent},
 {path: '', redirectTo: 'dashboard', pathMatch: 'full'},
 {path: '**', redirectTo: 'dashboard', pathMatch: 'full'}
];
```
What is the purpose of the `path: '**'` route in this Angular application, and how does it differ from the other routes defined?