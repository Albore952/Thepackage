from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

<<<<<<< HEAD
setup(name='mlproject',
=======
setup(name='Thepackage',
>>>>>>> 5f77ae081e984562abd8bc59e00d70b001bbde7c
      version="1.0",
      description="Project Description",
      packages=find_packages(),
      install_requires=requirements,
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
<<<<<<< HEAD
      scripts=['scripts/mlproject-run', 'scripts/mlproject-computedist'],
=======
      scripts=['scripts/Thepackage-run'],
>>>>>>> 5f77ae081e984562abd8bc59e00d70b001bbde7c
      zip_safe=False)
