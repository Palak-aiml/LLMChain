// Minimal JS for visual builder and dashboard

document.addEventListener("DOMContentLoaded", function() {
    const builder = document.getElementById("builder");
    builder.innerHTML = `<p>Drag and drop chain components here (UI prototype).</p>`;

    const metrics = document.getElementById("metrics");
    metrics.innerHTML = `<p>Metrics and traces will appear here (UI prototype).</p>`;
});
