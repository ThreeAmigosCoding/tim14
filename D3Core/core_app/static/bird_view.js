function updateBirdView(){

    d3.select("#bird-canvas-svg g#bird-g").html(d3.select("#main-canvas-svg g").html());

    let birdViewNode=d3.select("#bird-canvas-svg g#bird-g").node();

    let scaleFactor = calculateScaleFactor();
    let translateFactor=[-birdViewNode.getBBox().x * scaleFactor, -birdViewNode.getBBox().y * scaleFactor];

    d3.select("#bird-canvas-svg g#bird-g")
        .attr("transform", "translate(" + translateFactor + ")" + " scale(" + scaleFactor + ")");
}

function calculateScaleFactor(){
    let mainCanvasNode=d3.select('#main-canvas-svg g').node();
    let mainCanvasWidth=mainCanvasNode.getBBox().width;
    let mainCanvasHeight=mainCanvasNode.getBBox().height;

    let birdWidth=document.getElementById("bird-canvas-svg").clientWidth;
    let birdHeight=document.getElementById("bird-canvas-svg").clientHeight;
    let scaleFactor=birdHeight/mainCanvasHeight;
    if ((birdWidth/mainCanvasWidth)<(birdHeight/mainCanvasHeight)) {
        scaleFactor = birdWidth / mainCanvasWidth;
    }

    return scaleFactor;
}