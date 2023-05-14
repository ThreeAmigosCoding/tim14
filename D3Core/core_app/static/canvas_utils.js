var panZoom = d3.select('#main-canvas-svg')
    .call(d3.behavior.zoom().on("zoom", function () {
        d3.select("svg g").attr("transform", "translate(" + d3.event.translate + ")" + " scale(" + d3.event.scale + ")")
    }));

