You are a developer of project 'Warmduscher'. It's your task to implement according to the specification below# IT Specification

## 1. Summary
This specification details the functionality of the `overview-current.component.sass` file, which contains SCSS styles for the `OverviewCurrentComponent` in the Warmduscher project. The component appears to be responsible for displaying current overview information, likely related to a boiler or heating system, and its styles customize the appearance of MatCard header text, boiler temperature display and spacing.

## 2. File Information
- **File Location:** `Warmduscher/thclient/src/main/www/thserver-client/src/app/overview-current/overview-current.component.sass`
- **Class Name(s):** `myHeader`, `textBig`, `boilerTemp`, `spacer` (These are CSS class names, not programming class names)

## 3. Functional Requirements
- **Primary Operations:** Defines the visual styling of a component displaying current overview data (presumably related to heating system).
- **User Inputs & Outputs:** This file does not handle direct user input. It defines styles that will be applied based on data displayed by the Angular component. Output is the rendered visual presentation of the component.
- **Workflow/Logic:** The styles are applied based on the component's data binding in the associated `.ts` and `.html` files.
- **External Interactions:** This file interacts with Angular Material components (specifically `mat-card-header-text`) via CSS styling.
- **Edge Cases Handling:** No explicit edge case handling is present in the stylesheet itself. Any edge cases would be handled within the component logic and data binding.

## 4. Non-Functional Requirements
- **Performance:** The stylesheet is relatively small and should not significantly impact performance.
- **Scalability:** The CSS classes are specific to this component and should not create scalability issues.
- **Security:** This file does not directly handle sensitive data and poses no security risk.
- **Maintainability:** The styles are relatively simple and straightforward, making them reasonably easy to maintain. However, the use of `::ng-deep` suggests potential future refactoring needs.
- **Reliability & Availability:** The stylesheet itself will always be available as a static asset.
- **Usability:** Styles improve component appearance and readability.
- **Compliance:** The styling is in compliance with the chosen Angular and Material design standards.

## 5. Key Components
- **`.myHeader`**:  Styles the header of a MatCard component, removing left margin from the text and adding bottom margin.
- **`.textBig`**: Applies bottom margin to increase spacing.
- **`.boilerTemp`**: Applies left margin to the boiler temperature element.
- **`.spacer`**:  Applies bottom margin to add spacing.
- **Important logic flows**: None. This is a stylesheet; there are no logic flows.
- **Error handling**: Not applicable.
- **Classes**: Not applicable, this is a SCSS file.
- **Modules**: Not applicable.

## 6. Dependencies

### 6.1 Core Language Features
- SCSS syntax.
- CSS selectors.

### 6.2 External Frameworks & Libraries
- **Angular Material:** The styles target Angular Material components (e.g., `mat-card-header-text`).

### 6.3 Internal Project Dependencies
- None apparent from the file content. Dependencies on other components are implied through the usage of Angular Material, which is likely a project-wide dependency.

## 7. Potential Improvements
- **Refactor `::ng-deep`:** The use of `::ng-deep` is deprecated and can cause issues with styling encapsulation. Explore alternative solutions, such as using component selectors or CSS variables, to achieve the desired styling without relying on deprecated features. This is the most important improvement.
- **Component-Specific Styling:** Consider if the styles could be more tightly scoped to the component using techniques like CSS Modules or component-level styles in Angular.
- **CSS Variables:** Implement CSS variables to allow for dynamic theming and customization of the component's appearance.
- **Code Readability:** While the code is relatively simple, adding comments could improve maintainability, especially if the styles become more complex in the future.