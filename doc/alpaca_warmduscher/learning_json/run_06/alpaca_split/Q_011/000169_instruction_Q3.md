For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/app.module.ts' with name 'app.module.ts' where below a part of it is displayed...
```typescript
providers: [
   {provide: MAT_DATE_LOCALE, useValue: 'de-CH'},
   {provide: LOCALE_ID, useValue: 'de-CH'},
   {provide: HTTP_INTERCEPORS, useClass: MyHttpInterceptor, multi: true},
   {provide: LocationStrategy, useClass: HashLocationStrategy},
   // ... other providers
 ],
```
What is the purpose of the `LocationStrategy` provider set to `HashLocationStrategy`, and what is the difference between it and the default `PathLocationStrategy`?