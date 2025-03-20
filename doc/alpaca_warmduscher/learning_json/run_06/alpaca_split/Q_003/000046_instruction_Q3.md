For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/polyfills.ts' with name 'polyfills.ts' where below a part of it is displayed...
```typescript
(window as any).__Zone_disable_requestAnimationFrame = true; // disable patch requestAnimationFrame
(window as any).__Zone_disable_on_property = true; // disable patch onProperty such as onclick
(window as any).__zone_symbol__UNPATCHED_EVENTS = ['scroll', 'mousemove']; // disable patch specified eventNames
```
Explain the implications of setting `__Zone_disable_requestAnimationFrame` to `true`. What specific behavior of Zone.js will be affected, and in what scenarios might disabling this patch be beneficial?