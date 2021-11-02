# DOM(Document Object Model)
DOM(Document Object Model) will allow us to interface our Javascript code to interact with HTML and CSS.
- `console.dir(document)` : Return HTML text of the page. 

## DOM Interfacetion
- Important document attributes:
    - document.URL - This is the actual URL of the website.
    - document.body - This is everything inside of the body.
    - document.head - This is everything in the head of the page.
    - documnet.links - These are all the links on the page.
- methods for grabbing elements from the DOM
    - document.getElementsByClassName() -- Returns list of all elements belonging to a class.
    - document.getElementsByTagName() -- Returns list of all elements with the tag.
    - document.querySelector() -- Returns the first object matching the CSS style selector.
    - document.getElementById() -- Returns the element with the id.
    - document.querySelectorAll() -- Returns all objects matchin the CSS style selector.

- example code: [part1_ColorChanger.js](part1_ColorChanger.js)

## Content Interaction
- Methods to interaction to contents:
    - myvariable.textContent - This returns just the __text__
    - myvariable.innerHTML - This returns the __actual html__
    - myvariable.innerText - This returns the __text without \n__ included
    - myvariable.getAttribute() - This returns the original attribute
    - myvariable.setAttribute() - This allowed you to set an attribute
- example code: [part2_Content.html](part2_Content.html)

## DOM Events
- Adding events on the elements: `elements.addEventListener("events_name","function_to_run()")`
- Many, many possible [Events](https://developer.mozilla.org/en-US/docs/Web/Events).
    - Click, Hovers, Double Clicks, Drags, etc...
- example code: [part3_events.html](part3_events.html)

### Quiz
Compelete a TicTacToe Border:[quiz.html](quiz.html)

## Reference
- DOM Events : https://developer.mozilla.org/en-US/docs/Web/Events