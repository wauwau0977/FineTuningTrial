For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/boiler-chart/boiler-chart.component.html' with name 'boiler-chart.component.html' where below a part of it is displayed...
```html
<mat-card>
   <mat-card-subtitle>Boiler Temperatur (°C)</mat-card-subtitle>
   <mat-card-content>
     <div class="chartItem">
       <highcharts-chart
         [Highcharts]="highcharts"
         [options]="chartOptionsBoilerAverageTemp"
         [(update)]="chartUpdateFlag"
         [class.myLoading]="loading"
         class="chartStyle">
       </highcharts-chart>
       <mat-spinner
         *ngIf="loading"
         color="accent"
         class="myLoadingSpinner"></mat-spinner>
     </div>
   </mat-card-content>
 </mat-card>
```
What is the purpose of the `[class.myLoading]="loading"` binding within the `<highcharts-chart>` element, and how does it interact with the `<mat-spinner>` element? Explain the visual effect this creates.