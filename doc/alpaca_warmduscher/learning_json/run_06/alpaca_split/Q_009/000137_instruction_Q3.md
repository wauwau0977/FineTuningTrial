For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/app.component.spec.ts' with name 'app.component.spec.ts' where below a part of it is displayed...
```typescript
 it('should create the app', () => {
   const fixture = TestBed.createComponent(AppComponent);
   const app = fixture.componentInstance;
   expect(app).toBeTruthy();
 });
```
...What does `TestBed.createComponent(AppComponent)` do and why is accessing `fixture.componentInstance` important in this test? Explain the purpose of `expect(app).toBeTruthy()`.