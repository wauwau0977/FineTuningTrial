For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/dao/HeatPumpRepository.java' with name 'HeatPumpRepository.java'... 

Consider the following code snippet from the `getSoleDeltaInOperationStats` method:

```java
select min(measurement_date)                                  measurement_date_start,
       max(measurement_date)                                  measurement_date_end,
       count(1)                                               number_of_probes,
       di10compressor1,
       round(cast(avg(sole_in) - avg(sole_out) as numeric), 1) sole_in_out_delta_in_operation_avg, -- most interesting column!
       round(cast(avg(sole_in) as numeric), 1)                sole_in_avg,
       min(sole_in)                                           sole_in_min,
       max(sole_in)                                           sole_in_max,
       round(cast(avg(sole_out) as numeric), 1)               sole_out_avg,
       min(sole_out)                                          sole_out_min,
       max(sole_out)                                          sole_in_max
from (
    -- ... (inner queries) ...
) h1
group by seq_id, di10compressor1
order by measurement_date_start asc
```

Explain the purpose of the `seq_id` field in the `group by` clause. What problem does it solve, and how does it contribute to the overall logic of this query?