For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/app.component.spec.ts' with name 'app.component.spec.ts' where below a part of it is displayed...
```typescript
 it('should render title', () => {
   const fixture = TestBed.createComponent(AppComponent);
   fixture.detectChanges();
   const compiled = fixture.nativeElement as HTMLElement;
   expect(compiled.querySelector('.content span')?.textContent).toContain('thserver-client app is running!');
 });
```
...Explain what `fixture.detectChanges()` does and why it’s necessary before querying the DOM in this test. What is the purpose of the assertion `expect(compiled.querySelector('.content span')?.textContent).toContain('thserver-client app is running!');`?