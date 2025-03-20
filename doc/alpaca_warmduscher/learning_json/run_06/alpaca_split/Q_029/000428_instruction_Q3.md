For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/cache/cache.service.spec.ts' with name 'cache.service.spec.ts' where below a part of it is displayed... 

```typescript
let service: CacheService;
 beforeEach(() => {
   TestBed.configureTestingModule({});
   service = TestBed.inject(CacheService);
 });
```

Explain the role of the `let service: CacheService;` declaration and its relation to `service = TestBed.inject(CacheService);`. What would happen if the `let` keyword was omitted?