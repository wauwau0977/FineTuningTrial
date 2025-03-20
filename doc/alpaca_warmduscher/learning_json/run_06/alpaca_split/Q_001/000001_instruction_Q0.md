You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary

This file serves as the main HTML entry point for the Warmduscher web application. It sets up the basic structure, metadata, styling, and loading of the Angular application that displays heat pump statistics, graphs, and boiler temperatures. It configures the application as a Progressive Web App (PWA), enabling offline functionality and installation on various platforms.

## 2. File Information

- **File Location:** Warmduscher/thclient/src/main/www/thserver-client/src/index.html
- **Class Name(s):** N/A - This is an HTML file, not a class-based code file.

## 3. Functional Requirements

- **Primary Operations**: 
    - Loads the Angular application (`app-root`).
    - Configures the application as a PWA.
    - Provides a fallback message if JavaScript is disabled.
- **User Inputs & Outputs**: 
    - No direct user input. The HTML file sets up the environment for the Angular application, which then handles user interactions.
    - Outputs: The rendered web page containing the Warmduscher application.
- **Workflow/Logic**:
    1.  The browser loads the `index.html` file.
    2.  The HTML file defines the basic page structure and loads necessary assets (CSS, fonts, icons, manifest).
    3.  The `<app-root>` tag serves as a placeholder for the Angular application, which is then bootstrapped by the Angular runtime.
    4.  If JavaScript is disabled, a message prompts the user to enable it.
- **External Interactions**:
    - Loads fonts from Google Fonts (`fonts.googleapis.com`).
    - Loads Material Icons from Google Fonts (`fonts.googleapis.com`).
    - Loads icons from the `/assets/icons` directory.
    - Loads the `manifest.webmanifest` file, which is essential for PWA functionality.
- **Edge Cases Handling**:
    - Displays a "Please enable JavaScript" message if JavaScript is disabled in the browser.
    - Gracefully handles missing assets (images, manifest) – Angular application will likely handle these errors.

## 4. Non-Functional Requirements

- **Performance**: The file size should be minimized to ensure fast loading times. Assets should be optimized (compressed, cached).
- **Scalability**: N/A - This is a static HTML file and does not directly impact scalability. The scalability will be handled by the Angular application and the backend services.
- **Security**: The HTML file itself is not a significant security risk. However, proper security measures should be implemented in the Angular application and backend services.
- **Maintainability**:  The HTML should be well-formatted and easy to understand.  Clear comments can be added to explain specific configurations.
- **Reliability & Availability**: The HTML file should be available on the web server at all times.
- **Usability**: The HTML file provides the basic structure for the application. The Angular application built on top of it determines the overall usability.
- **Compliance**: Adheres to PWA standards for installation and offline functionality.

## 5. Key Components

- **`<head>` section**: Contains metadata, links to CSS, fonts, icons, and PWA manifest.
- **`<link>` tags**: Load external resources (CSS, fonts, icons).
- **`<meta>` tags**: Define metadata such as character set, title, viewport, and description.
- **`<base href="/">`**: Sets the base URL for all relative URLs in the application.
- **`<app-root>` tag**: Placeholder for the Angular application.
- **`<noscript>` tag**: Displays a message if JavaScript is disabled.
- **`mat-typography`, `mat-app-background` classes**: Material Design classes for styling.

## 6. Dependencies

### 6.1 Core Language Features

- HTML5
- CSS3

### 6.2 External Frameworks & Libraries

- **Google Fonts**: Provides Roboto font and Material Icons.
- **Material Design**: Used for theming and styling (via CSS classes).

### 6.3 Internal Project Dependencies

- **`assets/icons/icon-192x192_non_transparent_dark.png`**: App icon for PWA.
- **`manifest.webmanifest`**: PWA manifest file.

## 7. Potential Improvements

- **Performance Enhancements**:
    - Minify HTML, CSS, and JavaScript files.
    - Optimize images for web use.
    - Leverage browser caching.
- **Code Readability**: N/A - This is a static HTML file, and readability is already good.
- **Security Improvements**: N/A - This file does not present significant security risks.
- **Scalability Considerations**: N/A - This is a static file and does not affect scalability.