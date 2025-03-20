For Project 'Warmduscher' considering file in path 'Warmduscher/thserver/src/main/java/com/x8ing/thsensor/thserver/db/dao/HeatPumpRepository.java' with name 'HeatPumpRepository.java' where below a part of it is displayed... 
```java
 @Query(value = "select hour_of_day                            as hourOfTheDay,\n" +
           "      sum(boiler_temp_max_decrease_in_window) as sumBoilerDiffDecrease,\n" +
           "      sum(boiler_temp_max_increase_in_window) as sumBoilerDiffIncrease,\n" +
           "      max(num_of_statistic_records_1)        as numOfStatisticRecords1\n" +
           "from (\n" +
           "        select min(measurement_date_t0)               as measurement_date_t0,\n" +
           "               max(measurement_date_t1)               as measurement_date_t1,\n" +
           "               day_of_week_starting_monday,\n" +
           "               day_of_week_text,\n" +
           "               hour_of_day,\n" +
           "               min(boiler_temp_max_decrease_in_window) as boiler_temp_max_decrease_in_window,\n" +
           "               max(boiler_temp_max_increase_in_window) as boiler_temp_max_increase_in_window,\n" +
           "               max(num_of_statistic_records_1)        as num_of_statistic_records_1\n" +
           "        from (\n" +
           "                 select year1,\n" +
           "                        doy,\n" +
           "                        day_of_week_starting_monday,\n" +
           "                        day_of_week_text,\n" +
           "                        hour_of_day,\n" +
           "                        boiler_temp,\n" +
           "                        measurement_date,\n" +
           "                        measurement_date_t0,\n" +
           "                        measurement_date_t1,\n" +
           "                        case when boiler_temp_max_decrease_in_window > 0 then 0 else boiler_temp_max_decrease_in_window end    boiler_temp_max_decrease_in_window,\n" +
           "                        case when boiler_temp_max_increase_in_window <= 0.11 then 0 else boiler_temp_max_increase_in_window end boiler_temp_max_increase_in_window,\n" +
           "                        num_of_statistic_records_1\n" +
           "                 from (\n" +
           "                          select year1,\n" +
           "                                 doy,\n" +
           "                                 day_of_week_starting_monday,\n" +
           "                                 day_of_week_text,\n" +
           "                                 hour_of_day,\n" +
           "                                 boiler_temp,\n" +
           "                                 measurement_date,\n" +
           "                                 measurement_date_t0,\n" +
           "                                 measurement_date_t1,\n" +
           "                                 -1.0 * GREATEST(boiler_temp_window_tMax - boiler_temp_window_t1, boiler_temp_window_t0 - boiler_temp_window_tMin) boiler_temp_max_decrease_in_window,\n" +
           "                                 GREATEST(boiler_temp_window_tMax - boiler_temp_window_t0, boiler_temp_window_t1 - boiler_temp_window_tMin)       boiler_temp_max_increase_in_window,\n" +
           "                                 boiler_temp_window_t0,\n" +
           "                                 boiler_temp_window_t1,\n" +
           "                                 boiler_temp_window_tMin,\n" +
           "                                 boiler_temp_window_tMax,\n" +
           "                                 num_of_statistic_records_1\n" +
           "                          from (\n" +
           "                                   select measurement_date,\n" +
           "                                          extract(year from measurement_date)  year1,\n" +
           "                                          extract(doy from measurement_date)   doy, -- day of the year\n" +
           "                                          extract(hour from measurement_date)  hour_of_day,\n" +
           "                                          extract(minute from measurement_date) minute_of_hour,\n" +
           "                                          first_value(measurement_date) over ( partition by year1, doy, hour_of_day order by minute_of_hour)                     measurement_date_t0,\n" +
           "                                          last_value(measurement_date) over ( partition by year1, doy, hour_of_day order by minute_of_hour)                      measurement_date_t1,\n" +
           "                                          first_value(boiler_temp) over ( partition by year1, doy, hour_of_day order by minute_of_hour)                          boiler_temp_window_t0,\n" +
           "                                          last_value(boiler_temp) over ( partition by year1, doy, hour_of_day order by minute_of_hour)                           boiler_temp_window_t1,\n" +
           "                                          min(boiler_temp) over ( partition by year1, doy, hour_of_day order by minute_of_hour)                                  boiler_temp_window_tMin,\n" +
           "                                          max(boiler_temp) over ( partition by year1, doy, hour_of_day order by minute_of_hour)                                  boiler_temp_window_tMax,\n" +
           "                                          num_of_statistic_records_1\n" +
           "                                   from (\n" +
           "                                            select measurement_date,\n" +
           "                                                   extract(year from measurement_date)  year1,\n" +
           "                                                   extract(doy from measurement_date)   doy, -- day of the year\n" +
           "                                                   extract(hour from measurement_date)  hour_of_day,\n" +
           "                                                   extract(minute from measurement_date) minute_of_hour,\n" +
           "                                                   extract(dow from measurement_date) as day_of_week_starting_sunday,\n" +
           "                                                   To_Char(measurement_date, 'DAY')     day_of_week_text,\n" +
           "                                                   count(1) over ()                     num_of_statistic_records_1,\n" +
           "                                                   h1.boiler_temp\n" +
           "                                            from heat_pump h1\n" +
           "                                            where 1 = 1\n" +
           "                                              and measurement_date >= :measurement_date_start " +
           "                                              and measurement_date <= :measurement_date_end  " +
           "                                            order by year1, doy, hour_of_day, minute_of_hour\n" +
           "                                        ) h2\n" +
           "                                ) h3\n" +
           "                      ) h4\n" +
           "             ) h5\n" +
```
What is the purpose of the nested `over` clauses, like `first_value(boiler_temp) over ( partition by year1, doy, hour_of_day order by minute_of_hour)`? Explain how these clauses work in the context of this query.