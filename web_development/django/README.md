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
    source deactivate <myEnv>
    
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
   - `__init__.py` : treat the foler as the python package.
   - `admin.py` : register the module, so that Django will then use them with Django's admin interface.
   - `apps.py`: application specific configurations.
   - `models.py`: store the application's data models.
   - `tests.py`: test functions to test your code.
   - `views.py`: functions that handle requests and return response.
   - migrations folder: stores database specific information as it relates to the models.


- Add <my_app> info to the `INSTALLED_APPS` in `<my_project>/settings.py`.
- Coding [`views.py`](first_project/first_app/views.py) under the <my_app>
- Adding my app's URL pattern in [<my_project>/urls.py](first_project/first_project/urls.py)


### Django Template
The template will contain the static parts of an Html page.
- step1: Add the template directory path from the [`settings.py`](first_project/first_project/settings.py).  
- step2: Add the first [template app Html page](first_project/templates/first_template_app/index.html) under the ./templates/<template_folder>/<template_app_name>
- step 3: Add the contents inside of the double brackets in the Html Page(`{{ contents }}`) 
- step 4: From the [view.py](first_project/first_app/views.py) use the `render(request, <path_of_template_app>, context = <my_context>)` to pass the contents.

#### Adding Static
- step1: From the [`settings.py`](first_project/first_project/settings.py) file, add the STATICFILES_DIRS list variable.
- step2: On the top of the [Html file](first_project/templates/first_template_app/index.html),  Need to add the following lines to load staticfiles. `{% load static %}` 
- step3: And we can load the resources from the static folder by mentioning the relative position in `{% static '<path_of_the_file>' %}`

### Django Models
- step1: Adding models in the [<my_app>/models.py](/first_project/first_app/models.py)
- step2: Create Sql databases and update data.
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
