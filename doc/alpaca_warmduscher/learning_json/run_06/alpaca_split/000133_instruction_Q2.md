For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/app.component.spec.ts' with name 'app.component.spec.ts'... 
Consider this test:

```typescript
it('should render title', () => {
   const fixture = TestBed.createComponent(AppComponent);
   fixture.detectChanges();
   const compiled = fixture.nativeElement as HTMLElement;
   expect(compiled.querySelector('.content span')?.textContent).toContain('thserver-client app is running!');
});
```

What is `fixture.detectChanges()` and why is it necessary in this test? What potential issues could arise if `fixture.detectChanges()` was omitted?