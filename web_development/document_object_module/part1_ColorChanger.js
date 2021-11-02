// Get a Random number.
function getRandomColor(){
  var color = "#"
  var hexChars = "0123456789ABCDEF"

  for(var i = 0 ; i < 6; i++){
    index = Math.floor(Math.random() * hexChars.length);
    color +=hexChars[index];
  }
  return color;
}

// Set the randomColorMaker
function setColor(object, color){
  object.style.color = color;
}

// Select header element.
var header = document.querySelector("h1");

//Set random color of the header each 0.5 seconds
setInterval(function () {setColor(header,getRandomColor())},500);
