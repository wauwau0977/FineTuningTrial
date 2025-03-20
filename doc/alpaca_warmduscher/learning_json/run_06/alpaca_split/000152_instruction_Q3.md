For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/app.component.ts' with name 'app.component.ts' where below a part of it is displayed... 

```typescript
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass']
})
export class AppComponent {
  title = 'thserver-client';
  constructor() {
    console.log("Setup the page refresh mechanism all " + environment.fullPageRefreshInSeconds + " seconds.");
    // figure out a client id
  }
```

Explain the purpose of the `@Component` decorator and the role of the `constructor` method in this Angular component. What is the meaning of the `selector`, `templateUrl`, and `styleUrls` properties, and what's happening inside the `constructor`?