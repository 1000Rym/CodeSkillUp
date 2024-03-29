# Django
- Free and open source web framework(Pinterest, Instagram)
- Created in 2003, originated at the newspaper.

## Virtual environment for django conda
- What's different between `conda` and `pip`?
    1. Pip installs Python packages whereas conda installs packages which may contain software written in any language(They may also contain C or C++ libraries, R packages or any other software). 
    1. Conda has the ability to create isolated environment that can contain different versions of Python and/or the packages installed in them.

- Conda and Pip 
                         
|    Features           |               Conda VS Pip                     ||
| :---:                 |   :---:       |   :---:                         |
| command               |   `conda`     |   `pip`                         |
| manages               |   binaries    |   wheel or source               |
| can require compilers |   no          |   yes                           |
| create environment    | yes, built-in | no, requires virtualenv or venv |
| dependency checks     |   yes         |   no                            |
| package sources       |           Anaconda repo and cloud PyPI         ||


- Reference: [Understanding Conda and Pip](https://www.anaconda.com/blog/understanding-conda-and-pip)

### Create Virtaul environment for django
- Create an virtual environment [with specific version]
    ```bash
    conda create --name <myEnv> django [python=3.5]
    ```
- List virtual environmenst
    ```bash
    conda info --envs
    ```
- Activate virtual environemnt
    ```bash
    # Linux
    source activate <myEnv>

    # Windows
    activate <myEnv>
    ```
- Deactivate virtual environment
    ```bash
    # Linux
   conda deactivate
    
    # Windows
    deactivate <myEnv>
    ```

### Start First Project
- Create the project
    ```bash
    django-admin startproject <my_project>
    ```
- After command the folowing files created under the folder:
    - <my_project>
        - `__init__.py` : treat the foler as the python package.
        - `settings.py` : store project settigns.
        - `urls.py`: store all of the URL patterns.
        - `wsgi.py`: acts as the Web Server Gateway, deploy web app to production
    - `manage.py`: associate with many commands for builing web app.

- Run the server
    ```bash
    python manage.py runserver
    ```

### Start First App
- Start the application
    ```bash
    python manage.py startapp <app_name>
    ```
- After the command, we can see the following files generated.
   - `__init__.py` : Treat the foler as the python package.
   - `admin.py` : Register the module, so that Django will then use them with Django's admin interface.
   - `apps.py`: Application specific configurations.
   - `models.py`: Store the application's data models.
   - `tests.py`: Test functions to test your code.
   - `views.py`: Functions that handle requests and return response.
   - Migrations Folder: Stores database specific information as it relates to the models.


- Add <my_app> info to the `INSTALLED_APPS` in `<my_project>/settings.py`.
- Coding [`views.py`](first_project/first_app/views.py) under the <my_app>
- Adding my app's URL pattern in [<my_project>/urls.py](first_project/first_project/urls.py)


### Django Template
The template will contain the static parts of an Html page.
- step1: Add the template directory path from the [`settings.py`](first_project/first_project/settings.py).  
- step2: Add the first [template app HTML page](first_project/templates/first_template_app/index.html) under the ./templates/<template_folder>/<template_app_name>
- step 3: Add the contents inside of the double brackets in the Html Page(`{{ contents }}`) 
- step 4: From the [view.py](first_project/first_app/views.py) use the `render(request, <path_of_template_app>, context = <my_context>)` to pass the contents.

#### Adding Static
- step1: From the [`settings.py`](first_project/first_project/settings.py) file, add the STATICFILES_DIRS list variable.
- step2: On the top of the [HTML file](first_project/templates/first_template_app/index.html),  Need to add the following lines to load staticfiles. `{% load static %}` 
- step3: And we can load the resources from the static folder by mentioning the relative position in `{% static '<path_of_the_file>' %}`

### Django Models
- step1: Adding models in the [<my_app>/models.py](/first_project/first_app/models.py)
- step2: Create SQL databases and update data.
    ```shell
    # Initiate entire project
    python manage.py migrate 

    # Register changes to application
    python manage.py makemigrations <my_app>

    # Commit the changes to the project
    python manage.py migrate
    ```
- step3-1: Update and load data by shell.
    ```python
    # going to shell command
    python manage.py shell

    # from the shell
    >>> from first_app.models import Topic
    >>> print(Topic.objects.all())

    # generate a topic data t
    >>> t = Topic(top_name = 'Social Network')
    >>> print(Topic.objects.all())

    # Result
    <QuerySet [<Topic: Social Network>]>
    ```

- step 3-2: Load the data by admin interface.
    - step a: register the models to the [<my_app>/admin.py](/first_project/first_app/admin.py)
    - step b: create super user : `python manage.py createsuperuser`
    - step c: visiting and editing: `http:<your server address>/admin`

### Population Scripts
- step1: download the faker library. 
    - `pip install faker`
    - link: https://faker.readthedocs.io
- step2: make the mock data with the faker library ([example code](first_project/first_app_populate.py)).

### MTV(Models-Templates-Views)
- step1: In the [view.py](first_project/first_app/views.py) file, import models.
- step2: Use the view to query the model for data.
- step3: Pass results from the model to the template. 
- step4: Edit the [template](first_project/templates/first_template_app/index.html) so that it is ready to accept and display the data from the model.
    - `{% <logic(if, for, etc...)> %}`
    - `{{ <data_only>  }}`
- step5: Map a URL to the View.

### Django Forms 
- Advantages
    - Quickly generate HTML form widgets.
    - Validate data and process it into a Python data structure.
    - Create form versions of models, quickly update models from forms.

- How to use?
    - Add [form.py](/basicforms/basicapp/form.py) 
    - Import form module from the [views.py](/basicforms/basicapp/views.py)
        - Add post action.
    - From the page read the from as the followng.
        - 1 `form.as_p`: Follows the parent form style.
        - 2 `<% csrf_token %>` [cross-site request forgery](https://owasp.org/www-community/attacks/csrf): Add CSRF token (security code generated by user side and checked by backend)to avoid CSRF attacks.

#### Form Validation.
- Adding a check for empty fileds, or validate.
    - the validation method as a element in the list passed to the parameter in the forms Filed function can check the validation method directly.
    - Using `validators` from `django.core` can directly check the validation.
- Adding a clean method or the entire form.
    - add `def clean_<var>` method to check specific variable validation.
    - add `def clean` method to check all variables.

- Code: [form.py](/basicforms/basicapp/form.py)

#### ModelForm
Steps:
- step1: Using the `django.forms.ModelForm` to directly connect model to form([code](ProTwo/AppTwo/forms.py)).
    - From the `Meta class` choose model and field.
        - option1: `fileds = ("filed1", "field2")` to use target field.
        - option1: `fields = __all__`  to Use all field.
        - option2: `exclude = ["filed1", "field2"]` to not use excluded field.

- step2: From [views.py](ProTwo/AppTwo/views.py) read the form and if the form is valid `form.save(commit=true)` to submit the form and commit to databases.

### How to use URL Template Tagging 
To use template URL tagging do the following things:
- step1: Add the [my_app/urls.py](/learning_templates/basic_app/urls.py) 
    - Add `app_name ` variable.
    - Add path of each template URL in urls. 
- step2: All of the urls registered in the urls.py can be used as template tagging. 
    - From the [html page](/learning_templates/templates/basic_app/relative.html) change the URL as follows:
    ```php
    <!-- Original -->
    <a href= "baiscapp/thankyou">Thanks </a>
    <!-- Changed to -->
    <a href = "% url 'basic_app:thankyou' %"> Thanks </a>
    ```
### Template Inheritance
Main steps for inheritance as the follows:
- step1: Find the repetitive parts of your project.
- step2: Create a base [template](/learning_templates/templates/basic_app/basic.html) of them. 
- step3: Set the tags in the base template from the [file](/learning_templates/templates/basic_app/index.html).
    ```php
    <!-- Anything outside of this blocks can be inheritated. -->
    {% block <block_name> %}
    {% block endblock %}
    ```
- step4: Extend and call those tags anywhere.
    - Extends the template. 
    - Add the contents in side of the blocks.
    
    ```php
    {% extends '<template_path>' %}
        {% block <block_name> %}
        <!-- Add your contents  -->
        {% endblock % }
    ```
### Template Filters
- The general form for a template filter is : `{{value | filter:"parameter"}}`
- [Built-in template tags and filters](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/)
- Use pipe operater(`|`) to filter.
    - {{ text|upper }}
    - {{ number|add:"99" }}

#### Custom Templates
- Make the custom [template python file](/learning_templates/basic_app/templatetags/my_templates.py) under the `templatetags` package. 
    - `import` the `template` from `django`
    - Use the `register=template.Load()` to register custom function.
        - Custom function can be registered by decorator `@register.filter(<function_name>)`
        - Directly register function by passing function arguments to `register.filter()` 
- From the [templates](/learning_templates/templates/basic_app/index.html) do following things
    - load the template python file: `{% load <my_templates> %}`
    - load the templatefiltertags. 
- [Other Reference Link](https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/)

## User Authentication
- Required libraries for user authentifcation: 
    - `pip install bcrypt`
    - `pip install 'django[argon2]'`

- To work with the images:
    - `pip install pillow`

- Import the following python packages, add login and logout feature :
    - Code from [views.py](learning_users/basic_app/views.py)
    ```python
    from django.contrib.auth import authenticate, login, logout
    from django.http import HTTPResponseRedirect, HTTPResponse
    from django.urls import reverse
    from django.contrib.auth.decorators import login_required
    ```

    - add `user_login(request)`
        - use login module
    - add `logout(request)`, `special(request)`
        - use login_required module as decorator.

## Class View
- Define a class which is inherited from `View`
    - define `get()` method to response.
    - can not use template.

### Class Template View
- Define a class that inherited from `TemplateView`
    - set the basic html file in `template_name`
    - can inject data from `get_context_data()`


## Advanced Topic: CBV(Class Based View)
Django Provides powerful tools to use OOP and classes to use define views.

- Function Based View VS Class Based View
    ```python
    # Function Based View
    def index(request):
        return render(request, 'index.html')

    def IndexView(TemplateView):
        template_name = 'index_html'
    ```

- How to do it?
    ```python
    from django.views.generic. import view
    ```
- New Models
- New Templates



    


- Reference:
    - https://docs.djangoproject.com/en/3.2/topics/auth/passwords/

