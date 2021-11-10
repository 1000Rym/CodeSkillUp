# Virtual Environments
When we are running project, and those require different versions. Install the project with the single global command is not recommended. In this case, virtual environment can make you devide the developing enviroment to multiple python evironments. 

## Creating a Virtual Environment
1. Check current pip environment
```bash
which python3
```
2. From the Project folder create the venv environment.
```bash
python3 -m venv <my_venv>
# See the structure of the venv environment
tree <my_venv>
```
3. Activating a virtual environment. 
```bash
source ./<my_env>/bin/actitvate
# Check the venv pip
which pip
```
4. Deactivate the environment
```bash
deactivate
```
