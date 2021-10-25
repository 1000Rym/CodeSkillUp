# Basic Knowlege of HTML
In this page, we are going to look at basic knowledge of HTML tags.

## Introductions
- Hyper Text Markup Language. 
    - HTML Basics : ([basics.html](html/HTML_LEVEL_ONE/basics.html))
        - Tagging
            - Heading can be `<h1>` ~ `<h6>`
            - Use `<p>` to seperate paragraph.
                - Note that html dosen't have any indentation.
            - `<b>` stands for bold style, `<i>` stands for italic in old fashion.
            - `<strong>` stands for bold, `<em>`(emphasis) stands for italic. 
        - Lists
            - Ordered List: Use `<ol>` to create an ordered list.
            - Unorderd List: Use `<ul>` to create an unorderd list.
        - Dives and Spans : Grouping and adding styles by combination features with css. 
            - `<div>` : Group together all of inside elements.
            - `<span>` : Adding style on the inline elements of the container.
        - Attributes : Adding link or referencing the image.
            - `<img>`: Adding an image. 
                - `src` : path of the image(or link)
                - `alt` : Alter message when the contents is missing.
            - `<a>`: adding anchor(reference)

- Table's Tag: ([table.html](html/HTML_LEVEL_TWO/table.html))
    - `<table>`
        - could add attribute `bolder`
    - `<thead>` : Table head
        - `<th>`: Subitem of table head.
    - `<tr>` : Table Row
        - `<td>`: Table Column(Subitem of table row).

- Form(`form`:[form.html](html/HTML_LEVEL_TWO/form.html))
    - `input`
        - `type="text"`: input text type value.
        - `type="email"`: input email type value.
        - `type="password"` : input password type value.
        - `type="color"`  : choose the color.
        - `placeholder=` : Show the user hidden hint value.
        - `required`: The option for fillup the value before submit.
        - `type="submit"` : post the value.
        - `lable for`:  Use `lable for` to link the id with `input id`.
        - Radio Button
            - `type="radio"` the option value should share same `name`.
    - Drop down menus
        - `select` tags with `option` items.
    - Text Area inputs
        - `textarea` with `rows` and `cols` attributes.

Quiz: 
1) Simple Table: [quiz.html](HTML_LEVEL_TWO/quiz.html)
2) Simple Table: [quiz2.html](HTML_LEVEL_TWO/quiz2.html)