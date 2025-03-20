For Project 'Warmduscher' considering file in path 'Warmduscher/thclient/src/main/www/thserver-client/src/app/overview-current/overview-current.component.html' with name 'overview-current.component.html' where below a part of it is displayed... 
```html
<mat-card-title class="myTitle">
   Büelwisen Daten von {{ (heatingEntity.id !== null) ? (heatingEntity.measurementDate | date: 'HH:mm') : "..."}}
</mat-card-title>
```
What is the purpose of the ternary operator `(heatingEntity.id !== null) ? (heatingEntity.measurementDate | date: 'HH:mm') : "..."` and how does it affect the displayed time?