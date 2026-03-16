## 2026-02-18 - Dual-Unit Visualization in Engineering Notebooks
**Learning:** Engineers often think in degrees (intuition) while models operate in radians (math). Presenting only one forces cognitive load.
**Action:** Use dual-axis plots (e.g., via `secondary_yaxis`) for angular data in scientific notebooks to bridge the gap between intuition and implementation without cluttering the primary data.

## 2026-02-20 - Visualizing Acceptance Criteria in Control Plots
**Learning:** Textual metrics (like "Settling Time: 3.5s") are abstract. Users must mentally map this value to the chart to verify it.
**Action:** Directly visualize acceptance criteria (e.g., shaded ±2% error bands) and performance events (e.g., settling time marker) on the plot to reduce cognitive load and provide immediate visual verification.

## 2026-03-06 - Accessible HTML Output in Jupyter Notebooks
**Learning:** When manually generating HTML for visualization outputs in Jupyter Notebooks (like custom styled tables), standard accessibility principles apply but are easily overlooked. Relying solely on color (like green background for optimal vs gray for weak) fails WCAG success criteria for users with visual impairments.
**Action:** Always include visually hidden (`sr-only`) text alongside color-coded information in HTML outputs. Use proper semantic markup (`aria-label` for tables, `scope="col"` and `scope="row"` for headers) even in programmatic outputs to ensure assistive technologies can correctly parse the data structures.

## 2026-03-16 - Accessible Pandas DataFrames
**Learning:** Raw pandas DataFrames rendered in Jupyter Notebooks lack screen reader context, making the tabular data inaccessible to visually impaired users.
**Action:** Always use `.style.set_table_attributes('aria-label="..."')` when displaying DataFrames to ensure the generated HTML table has a descriptive label for assistive technologies.
