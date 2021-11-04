# jQuery
- jQuery is a Javascript Library.
- It is a large single.js file that has many pre-built methods and objects.

## Simple jQuery Script 
### jQuery Basic
```javascript
// Select an h1 tag.
var x = $('h1'); //select h1 tags.

// change the color attribute red.
x.css("color","red");

// define a css.
var newCss = {
"color":"white",
"background":"blue",
"border":"red"
};

// set the css once.
x.css(newCss);

// choose the multiple li
var listItems = $('li'); 

// change the list item elements.
listItems.css("color","red"); // All
listItems.eq(0).text("I am the first item."); // First
listItems.eq(-1).text("I am last item."); // Last

//Change the input attribute
$('input').eq(0).attr('value', 'new value'); 
$('input').eq(0).attr('type', 'checkbox')
$('input').eq(0).val('value')

// About class
// add class. 
$('h1').addClass('turndRed')
// remove class
$('h1').removeClass('trunRed')
//toggle class.
$('h1').toggleClass('turndRed') // toggle On
$('h1').toggleClass('turndRed') // toggle Off
```

### jQuery Event
Events: https://api.jquery.com/category/events/
Effects: http://api.jquery.com/category/effects/

```javascript
// click event way1.
$('h1').click(function()){
    console.log("Clicked H1");
}

// click event way2 - use on method instead.
$('h1').on('click', function(){
    console.log("Clicked H1");
})

// keyboard event.
$('input').eq(0).keypress(function(event){
    // when pressed an enter key
    if(event.which === 13){
        $('h1').toggleClass("turnRed")
    } 
})

// effect - fade out
$('.container').fadeOut(3000);
```

### Quiz: Connect 4 
