For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/app.module.ts' with name 'app.module.ts'... 
Examine this section within the `providers` array:
```ts
{provide: LOCALE_ID, useValue: 'de-CH'},
{provide: MAT_DATE_LOCALE, useValue: 'de-CH'}
```
What is the purpose of these providers, and why are both `LOCALE_ID` and `MAT_DATE_LOCALE` being set to `'de-CH'`? Explain the difference between the two.