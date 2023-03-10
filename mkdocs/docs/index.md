# Getting started.  

For full source project : [https://github.com/AmedBrook/AI-EMS](https://github.com/AmedBrook/AI-EMS).



## Project layout.
---
    data/
        external/
        interim/
        processed/
        raw/
        .gitkeepg
    mkdocs/
        docs/
            img/
            javascripts/
                        mathjax.js
            ...
        site/
            ...
        mkdocs.yml
    models/
        .gitkeep
    notebooks/
        .gitkeep
        IEMS_v0.1.4.ipynb
    references/
        .gitkeep
    reports/
        figures/
        ...
    src/
        data/
        features/
        models/
        tests/
        visualization/
        __init__.py
        .gitkeep
    .env
    .gitignore
    Changelog.md
    Gurobi-license.txt
    LICENSE
    Makefile
    README.md
    requirements.txt
    test_environment.py
    setup.py
    setup.cfg

<br>
<br>
---
## Packages walk-through.
---

This is a quick guide on how to install the required packages if you have decided for whatever reason to go through installations one by one and setting up the project without passingg by the setup.py or using make for this matter. Though you still have to go through the manual installation for [Mathjax](https://github.com/AmedBrook/Pulp_MILP-Hybrid-Energy-Optimization#mathjax) setup.

##### matplotlib.

In order to install matplotlib package run one of the following commands : 

* Using Anaconda package index : `$ conda install -c conda-forge matplotlib` 

* Using Python package index (Pypi) : `$ python -m pip install matplotlib` 


##### numpy.

In order to install numpy package run one of the following commands : : 

* Using Anaconda package index : `$ conda install -c anaconda numpy`

* Using Python package index (Pypi) : `$ python -m pip install numpy` 

    
##### Mkdocs. 

To install Mkdocs packages, run one of the following commands: 

* Using Python package index (Pypi) : `$ python -m pip install mkdocs`


* Using Anaconda package index (Conda) : `$ conda install -c conda-forge mkdocs` 


* To create new mkdocs project : 
	
	`$ python -m mkdocs new [name of the project]` 

* To preview your documentation, you need to locate in the docs directory created with the last command and then run: 

    `$ python -m mkdocs serve` 
	
* To see the rendered changes browse within the output https address returned by the last command.
For more guidance on mkdocs, see [here](https://www.mkdocs.org/user-guide/).

##### flake8. 

To analyse code syntax and debug make sure each single peace of code follows the PEP8 and other coding standards we use flake8 linter to do so. 
In order to install flake8 run on of the follwing commands : 

* Using Anaconda package index : `$ conda install -c anaconda flake8` 

* Using Python package index (Pypi) : `$ python -m pip install flake8` 


##### Mathjax. 

Mathjax is a Javascript library that can display mathimatical notations in the browser using LaTex or other. 
In order to integarate Mathjax within Mkdocs do the following: 

* Install pymdown-extensions (Pypi): `$ python -m pip install pymdown-extensions` 

* Within your mkdocs folder create the following: 

```
 			mkdocs_______
      			|___ docs
		      			|___ javascripts
             			|     		|___ mathjax.js
			    		|           
```									


* Add the following script lines in the configuration file `mkdocs.yml` :

```yaml
extra_javascript:

    javascripts/mathjax.js
    https://polyfill.io/v3/polyfill.min.js?features=es6
    https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
```

<br>

---
## Setup options.
---
<br>

### Standalone setup.
----

###### Environment.

* `$ conda create --AI-EMS ` - Create a new environment aside of the root, and name it somthing recognisable, we named here as HEO_model, we have used here python version 3.9.7. to do so you tape.

###### Requirements and Dependencies.

 Before stating the setup process you need to have <em>`setuptools`</em> installed, if you don't have it already do through the following commands:

* Python package index (Pypi) : `$ pip install setuptools`

* Anaconda package index (Conda) : `$ conda install -c conda-forge setuptools`

 Now that you have <em>`setuptools`</em> in you environment, in order to install all packages and dependencies at once run the command : 

*  `$ python -m pip install -e .`

<br>

### Pre-configured setup.
----


While the manual installation can walk you through around the various commands basics for each used packages in the project, chances are you might already know those commands and you don't want to bother yourself about taping every single command, so that's why we have provided the possibility to use `make` scripting, to make life easy for you. You find in the following the commands you will need to do this. 


In case you have make installed in your system, for Linux based system it comes already installed in your system you don't need to install anything just skeep this part to {...}. For windows based systems there are multiple ways to get GNU make installed, like for example Cygwin, Nmake, Cmake..., however we recommand to go for [chocolatey](https://community.chocolatey.org/packages/make), we think it's the most straighforward way to install make for windows systems with less effort. 

#### chocolatey.


 First thing first, we will install chocolatey, make sure you are using the Powershell command as an admin,
	
* Then run this command first : 
```bash
Get-ExecutionPolicy 
```

* If it returns Restricted, then run : 
```bash
Set-ExecutionPolicy AllSigned or Set-ExecutionPolicy Bypass -Scope Process
```

* Now, to install `chocolatey` run the following command by coping it at once and past it in command line, then hit enter:

```bash
 Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) 

```

Please check [chocolatey](https://community.chocolatey.org/packages/make) website for more guidance !
    

#### Make.


* Now that you have `chocolatey` installed, we can install `make` by running the command : 

``` 
     $ choco install make --version=3.81
```

Once make installation is done, and assuming that you have downloaded the project files in your local machine it's very easy to workout everything. 

* To create the conda environment run the command : 
 
```	
	 $ make create_env
```

* To setup the project run the command : 

``` 
	 $ make setup
```
<br>
<br>
