You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This code defines the configuration options for multiple Highcharts within a TypeScript Angular component named `BoilerChartComponent`. Each chart visualizes different heating-related data, including temperatures (heating return, heating supply, outdoor, delta), compressor hours, operation charts, and wind speed. The component configures various chart properties like data series, types, colors, axes, tooltips, legends, and general styles.  The goal is to present historical and real-time heating system data in a visually informative manner.

## 2. File Information

- **File Location:** `Warmduscher/thclient/src/main/www/thserver-client/src/app/boiler-chart/boiler-chart.component.ts`
- **Class Name(s):** `BoilerChartComponent` (although only the chart option definitions are provided in this snippet)

## 3. Functional Requirements

- **Primary Operations:** Define and configure various Highcharts for visualizing heating system data.
- **User Inputs & Outputs:** This code snippet itself does not handle user inputs. It *outputs* configuration objects used by the Highcharts library to *display* data. The data source is assumed to be available to the component and fed into these chart configurations.
- **Workflow/Logic:** The code defines multiple chart option objects. Each object describes a specific chart with its specific data series, appearance, and behavior.  The chart configuration is likely used to initialize a Highcharts instance within the `BoilerChartComponent`.
- **External Interactions:**  The code interacts with the Highcharts JavaScript library. It's also implicitly dependent on the data source that provides the values for the charts.
- **Chart Types:** The code configures the following chart types:
    - Area charts (for temperatures)
    - Line charts (for temperatures, compressor hours, outdoor temperature, wind speed)
    - Operations chart (details not provided but likely custom visualization)

## 4. Data Definitions

The following data sources are implied to be available within the component:

*   `compressorHours`: Array of numerical values representing compressor operating hours.
*   `outdoorTempAverage`: Array of numerical values representing average outdoor temperature.
*   `outdoorTempAverageMeteo1`: Array of numerical values representing average outdoor temperature from Meteo-Schweiz (Kloten).
*   `outdoorTempAverageMeteo2`: Array of numerical values representing average outdoor temperature from Meteo-Schweiz (Schaffhausen).
*   `windGustMeteoSwiss`: Array of numerical values representing wind gust speed from Meteo Schweiz.
*   Heating return temperature data (implied by chart configuration).
*   Heating supply temperature data (implied by chart configuration).
*   Delta temperature data (implied by chart configuration).

## 5. Technical Details

*   **Technology Stack:** TypeScript, Angular, Highcharts
*   **Chart Configuration:**  Uses the Highcharts configuration object format to specify chart properties.
*   **Styling:**  Defines colors, fonts, and other styling properties for the charts.
*   **Timezone Handling:**  The `timezoneOffset` property is consistently set to `new Date().getTimezoneOffset()` to ensure charts display data in the correct local time.
* **Dynamic Axes:** The 'Operation Chart' configuration includes a dynamically added yAxis and series.

## 6. Assumptions

*   The `BoilerChartComponent` is responsible for fetching the necessary data and providing it to the Highcharts library.
*   The Highcharts library is properly integrated into the Angular application.
*   The data formats are compatible with the Highcharts library.
*   The component will appropriately handle cases when data is unavailable or incomplete.

## 7. Future Considerations

*   **Data Filtering and Aggregation:** Implement functionality to filter and aggregate data for different time periods.
*   **Interactive Features:** Add interactive features such as zooming, panning, and tooltips.
*   **Error Handling:**  Implement robust error handling to gracefully handle data errors or connection issues.
*   **Data Source Abstraction:** Abstract the data source to make it easier to switch between different data providers.
* **Unit Tests:** Create unit tests to verify the correctness of the chart configurations.