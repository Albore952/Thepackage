# Data analysis
<<<<<<< HEAD
- Document here the project: mlproject
=======
- Document here the project: Thepackage
>>>>>>> 5f77ae081e984562abd8bc59e00d70b001bbde7c
- Description: Project Description
- Data Source:
- Type of analysis:

Please document the project the better you can.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

<<<<<<< HEAD
Check for mlproject in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/mlproject`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "mlproject"
git remote add origin git@github.com:{group}/mlproject.git
=======
Check for Thepackage in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/Thepackage`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "Thepackage"
git remote add origin git@github.com:{group}/Thepackage.git
>>>>>>> 5f77ae081e984562abd8bc59e00d70b001bbde7c
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
<<<<<<< HEAD
mlproject-run
=======
Thepackage-run
>>>>>>> 5f77ae081e984562abd8bc59e00d70b001bbde7c
```

# Install

<<<<<<< HEAD
Go to `https://github.com/{group}/mlproject` to see the project, manage issues,
=======
Go to `https://github.com/{group}/Thepackage` to see the project, manage issues,
>>>>>>> 5f77ae081e984562abd8bc59e00d70b001bbde7c
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
<<<<<<< HEAD
git clone git@github.com:{group}/mlproject.git
cd mlproject
=======
git clone git@github.com:{group}/Thepackage.git
cd Thepackage
>>>>>>> 5f77ae081e984562abd8bc59e00d70b001bbde7c
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
<<<<<<< HEAD
mlproject-run
=======
Thepackage-run
>>>>>>> 5f77ae081e984562abd8bc59e00d70b001bbde7c
```
