For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/overview-current/overview-current.component.html' with name 'overview-current.component.html' where below a part of it is displayed...
```html
<div fxFlex.gt-xs="50" class="">
  <div class=""> Aussen-Temperatur</div>
  <div class="mat-display-2 textBig">{{heatingEntity.ireg300TempOutdoor | number: '1.1-1'}} °C</div>
  <div class="mat-caption">{{meteoSwissEntity.temperature | number: '1.1-1'}} °C : Meteo-Schweiz Kloten</div>
</div>
```
What is the purpose of the `number: '1.1-1'` pipe applied to both `heatingEntity.ireg300TempOutdoor` and `meteoSwissEntity.temperature`, and how does it format the displayed values?