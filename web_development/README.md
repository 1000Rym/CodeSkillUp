# Introduction
This page is made for learning django. The following contents are contained in this page. 

- Django Bootcamp?
    - Front-End : what you see as a user on the website.
        - HTML(HyperText Markup Laguage)
        - CSS(Cascading Style Sheets)
        - Javascript(Allows you to add interactivity)
    - Back-End : what to show you on the front-end. 
        - The Language : Python
        - The Framework : Django(fast, secure, scalable)
        - The Database : SQLite

## HTML
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


Reference: 
- [1] w3school.com
- [2] developer.mozilla.com

