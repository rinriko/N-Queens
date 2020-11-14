# Table of Contents
1. [Install Python](#install-python)
2. [Download project](#download-project)
3. [Set-up project](#set-up-project)
4. [Run project](#run-project)
5. [Help](#help)

Note: Follow step 1 if Python 3.7.3 is not installed. Follow step 2 and 3 if project has not been downloaded.

## <a name="install-python"></a> Install Python
1. Go to this [link](https://www.python.org/downloads/release/python-373/).
2. Download Python 3.7.3 for your Operating System (e.g., Mac OS X, Windows)
3. Install Python 3.7.3 by following this [link](https://realpython.com/installing-python/).

## <a name="download-project"></a> Download project
### First method (clone repository)
1. Open Command Prompt or Terminal. [More information](https://www.groovypost.com/howto/open-command-window-terminal-window-specific-folder-windows-mac-linux/).
2. Change the current working directory to the location where you want to download the project.
3. Clone repository:

```sh
$ git clone https://github.com/rinriko/N-Queens.git
```
Note: If Git is not installed, please complete the following [instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Or follow the [second method](#second-method) instructions.

### <a name="second-method"></a> Second method (download project)
1. Go to https://github.com/rinriko/N-Queens.
2. Above the list of files, click &#8595; Code.
3. Click "Download ZIP".
4. Save the zip file into a convenient location on your PC and start working on it.
5. Extract the ZIP file.


## <a name="set-up-project"></a> Set up project
### From the first method
1. Continue use Command Prompt or Terminal, type:
```sh
$ cd N-Queens
```
2. In order to install the project requirements, type:
```sh
$ make setup
```
### From the second method
1. Open Command Prompt or Terminal. [More info](https://www.groovypost.com/howto/open-command-window-terminal-window-specific-folder-windows-mac-linux/).
2. Change the current working directory to the location where you have the cloned directory. [More info](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/bash/bash-commands-to-manage-directories-files/#:~:text=Often%2C%20you%20may%20want%20to,to%20check%20the%20new%20path).
3. In order to install the project requirements, type:
```sh
$ make setup
```

## <a name="run-project"></a> Run project
Inside the N-Queens directory, use the Command Prompt or Terminal and type:

```sh
$ make run
```

## <a name="help"></a> Help
Inside the N-Queens directory, use the Command Prompt or Terminal and type:
```sh
$ make help
```

Note: More information about GUI: [Click link](https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter).