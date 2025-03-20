For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/environments/environment.ts' with name 'environment.ts'... 
Looking at the following code snippet:

```typescript
export const environment = {
  production: false,
  serviceBaseURL: "https://www.mindalyze.com/pi11/",
  fullPageRefreshInSeconds: 10 * 60 * 5,
  "buildTimestampClient": "v01-20220220-093352"
};
```

How would you modify this code to allow for different configurations based on build type (e.g., development, production, staging) *without* directly editing this file? Explain your approach and what mechanisms Angular provides to achieve this.