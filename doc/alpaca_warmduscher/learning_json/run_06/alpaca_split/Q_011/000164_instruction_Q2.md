For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/app.module.ts' with name 'app.module.ts'... 
Consider this part of the code:
```ts
export const routes: Routes = [
 {path: 'dashboard', component: OverviewCurrentComponent},
 {path: 'insights', component: BoilerChartComponent},
 {path: 'about', component: AboutComponent},
 {path: '', redirectTo: 'dashboard', pathMatch: 'full'},
 {path: '**', redirectTo: 'dashboard', pathMatch: 'full'}
];
```
Explain the purpose of the last two routes (`{path: '', redirectTo: 'dashboard', pathMatch: 'full'}` and `{path: '**', redirectTo: 'dashboard', pathMatch: 'full'}`). How do they contribute to the user experience and the application's routing behavior?