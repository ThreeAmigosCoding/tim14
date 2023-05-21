var panZoom = d3.select('svg#main-canvas-svg')
    .call(d3.behavior.zoom().on("zoom", function () {
        d3.select("svg#main-canvas-svg g").attr("transform", "translate(" + d3.event.translate + ")" + " scale(" + d3.event.scale + ")")
    }));

