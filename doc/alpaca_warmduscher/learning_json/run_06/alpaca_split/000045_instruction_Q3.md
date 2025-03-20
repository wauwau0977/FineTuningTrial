For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/polyfills.ts' with name 'polyfills.ts' where below a part of it is displayed...
```typescript
/**
 * By default, zone.js will patch all possible macroTask and DomEvents
 * user can disable parts of macroTask/DomEvents patch by setting following flags
 * because those flags need to be set before `zone.js` being loaded, and webpack
 * will put import in the top of bundle, so user need to create a separate file
 * in this directory (for example: zone-flags.ts), and put the following flags
 * into that file, and then add the following code before importing zone.js.
 * import './zone-flags';
 */
```
What is the purpose of creating a separate `zone-flags.ts` file and why is it necessary to import it *before* `zone.js`? Explain the benefits of this approach in the context of Angular's Zone.js patching.