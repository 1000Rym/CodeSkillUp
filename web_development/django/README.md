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
    condo info --envs
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
- After command the following files created under the folder:
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
- Adding my app's URL patten's in [<my project> urls.py](first_project/first_project/urls.py)