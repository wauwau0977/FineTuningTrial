For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/app.component.ts' with name 'app.component.ts' where below a part of it is displayed... 

```typescript
myFullPageRefresh(): void {
  window.location.reload();
}
subscribe = interval(environment.fullPageRefreshInSeconds * 1000).subscribe(
  val => {
    console.log("Execute full page refresh... ")
    this.myFullPageRefresh();
  }
);
```

Describe the functionality of the `myFullPageRefresh()` method and how it interacts with the `interval` observable subscription to achieve a full page refresh at a specified interval. What are potential drawbacks of this approach?