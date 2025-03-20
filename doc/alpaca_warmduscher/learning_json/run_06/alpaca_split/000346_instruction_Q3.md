For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/boiler-chart/boiler-chart.component.html' with name 'boiler-chart.component.html' where below a part of it is displayed...
```html
<div fxLayout.xs="column" fxLayout.gt-xs="row" fxFill>
         <div fxLayout.gt-xs="row">
           <mat-form-field class="smallFormElement" appearance="fill">
             <mat-label>von</mat-label>
             <input matInput (click)="customFromDate.open()" [matDatepicker]="customFromDate"
                    formControlName="customFromDate">
             <mat-datepicker-toggle matSuffix [for]="customFromDate"></mat-datepicker-toggle>
             <mat-datepicker #customFromDate></mat-datepicker>
           </mat-form-field>
           <mat-form-field class="smallFormElement" appearance="fill">
             <mat-label>Zeit (Stunde)</mat-label>
             <input matInput type="number" formControlName="customFromDateTimePart">
           </mat-form-field>
           <div style="width: 1em"></div>
         </div>
         <div fxShow.gt-sm style="width: 25px"></div>
         <div fxLayout.gt-xs="row">
           <mat-form-field class="smallFormElement" appearance="fill">
             <mat-label>bis</mat-label>
             <input autocomplete="off" matInput [matDatepicker]="customToDate" formControlName="customToDate">
             <mat-datepicker-toggle matSuffix [for]="customToDate"></mat-datepicker-toggle>
             <mat-datepicker #customToDate></mat-datepicker>
           </mat-form-field>
           <mat-form-field class="smallFormElement" appearance="fill">
             <mat-label>Zeit (Stunde)</mat-label>
             <input matInput type="number" formControlName="customToDateTimePart">
           </mat-form-field>
         </div>
       </div>
```
Describe how the `fxLayout` directives (`fxLayout.xs`, `fxLayout.gt-xs`, `fxFill`) are used to control the layout of the date and time input fields.  How does the layout change based on screen size, and what is the purpose of the `fxFill` directive?