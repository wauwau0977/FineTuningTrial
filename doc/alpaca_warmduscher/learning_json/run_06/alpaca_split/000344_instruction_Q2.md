For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/boiler-chart/boiler-chart.component.html' with name 'boiler-chart.component.html'... 

Looking at the following code snippet, focusing on the date selection form:

```html
<div class="date-selector">
   <form [formGroup]="myForm" (ngSubmit)="onMyFormSubmit()">
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
     <div class="example-label-container">
       <label id="example-name-label" class="example-name-label">Anzahl Datenpunkte</label>
       <label class="example-value-label">
         {{myForm.value.chartDataPoints}}
         <span *ngIf="myForm.value['intervalAutoMatching']"> ~ {{autoSelectedInterval.name}} </span>
       </label>
     </div>
     <mat-slider
       formControlName="chartDataPoints"
       class="mySlider"
       max="3000"
       min="1"
       step="1"
       thumbLabel="true"
       aria-labelledby="example-name-label">
     </mat-slider>
     <mat-checkbox formControlName="intervalAutoMatching">Interval auto matching</mat-checkbox>
   </form>
</div>

How does the application handle scenarios where the user provides an invalid date range (e.g., 'to' date is before 'from' date)? Describe the expected behavior and what parts of the application (beyond this HTML snippet) would be responsible for enforcing this validation.