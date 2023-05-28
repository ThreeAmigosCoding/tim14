var panZoom = d3.select('svg#main-canvas-svg')
    .call(d3.behavior.zoom().on("zoom", function () {
        d3.select("svg#main-canvas-svg g").attr("transform", "translate(" + d3.event.translate + ")" + " scale(" + d3.event.scale + ")")
    }));

document.getElementById('apply-search').addEventListener('click', function() {
    let layoutType = location.href.split('/').pop();
    let queryString = document.getElementById('search-input').value.trim();
    if (queryString === "") return
    location.href = "/search/" + layoutType + "/" + queryString;
});

document.getElementById('reset-graph-btn').addEventListener('click', function() {
    let layoutType = location.href.split('/').pop();
    location.href = "/reset/" + layoutType;
});

document.getElementById('apply-filter').addEventListener('click', function () {
    let layoutType = location.href.split('/').pop();
    let attributeName = document.getElementById('filter-input-attribute').value.trim();
    let operator = document.getElementById('filter-input-operator').value.trim();
    let operand = document.getElementById('filter-input-operand').value.trim();
    // some validation for operation e.g. "operands, attributes, operators"

    let operation = attributeName + " " + operator + " " + operand;
    location.href = "/filter/" + layoutType + "/" + operation;
});
