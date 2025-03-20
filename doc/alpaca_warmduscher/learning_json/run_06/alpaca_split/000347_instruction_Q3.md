For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/boiler-chart/boiler-chart.component.html' with name 'boiler-chart.component.html' where below a part of it is displayed...
```html
<mat-card>
   <mat-card-subtitle>Boiler Statistik nach Stunden</mat-card-subtitle>
   <mat-card-content>
     <div class="chartHint mat-caption">
       Hinweis: Die Grafik zeigt, zu welcher Stunde des Tages der Boiler am stärksten gebraucht wurde.
       Diese Statistik funktioniert am besten über einen grösser Zeitraum von mehereren Tagen.<br>
       Anzahl Datenpunkte: {{boilerStatsByHourNumberOfStaticsRecords | number:'':'de-CH'}}
     </div>
     <div class="chartItem">
       <highcharts-chart
         [Highcharts]="highcharts"
         [options]="chartOptionsBoilerStatsByHour"
         [(update)]="chartUpdateFlag"
         [class.myLoading]="loadingBoilerByHour"
         class="chartStyle">
       </highcharts-chart>
       <mat-spinner
         *ngIf="loadingBoilerByHour"
         color="accent"
         class="myLoadingSpinner"></mat-spinner>
     </div>
   </mat-card-content>
 </mat-card>
```
Explain the purpose of the pipe `| number:'':'de-CH'` applied to the `boilerStatsByHourNumberOfStaticsRecords` variable. What effect does this pipe have on the displayed value, and why is it used in this context?