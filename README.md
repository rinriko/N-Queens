# Table of Contents
1. [N-queens Problem](#n-queens)
2. [Install Python to Local machine](#install-python)
3. [Install SAT Solver to Linux machine](#install-sat)
    - [More about MiniSat version 1.14](#more-sat)
4. [Download project to Local machine](#download-project)
5. [Set-up project](#set-up-project)
6. [Run project](#run-project)
7. [Help](#help)
8. [How to use this program](#how-to-use)

Note: 
- Follow step 2 if Python 3.7.3 is not installed on the local machine. 
- Follow step 3 if MiniSat version 1.14 is not installed on the Linux machine. 
- Follow step 4 and 5 if project has not been downloaded to the local machine.
- More information about GUI: [Click link](https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter).

----------------------------------------------------
## <a name="n-queens"></a> N-queens Problem

The n-queens puzzle is the problem of placing N queens on an N×N chessboard such that no two queens attack each other.
        
To encode the n-queens (n is a given number) problem into the DIMACS CNF format and solve it by the SAT solver, we need to encode the following constraints 
        1) no two queens on the same row, 
        2) no two queens on the same column, and 
        3) no two queens on the same diagonal. 
        
[More information](https://linuxize.com/post/how-to-use-nano-text-editor/).

----------------------------------------------------
## <a name="install-python"></a> Install Python to Local machine
1. Go to this [link](https://www.python.org/downloads/release/python-373/).
2. Download Python 3.7.3 for your Operating System (e.g., Mac OS X, Windows)
3. Install Python 3.7.3 by following this [link](https://realpython.com/installing-python/).
----------------------------------------------------
## <a name="install-sat"></a> Install SAT Solver to Linux machine
1. Connect to TTUnet VPN by following this [link](https://www.askit.ttu.edu/portal/app/portlets/results/viewsolution.jsp?guest=0&solutionid=181128172622147&hypermediatext=null).
2. Connect to the Linux server which name is `willow.cs.ttu.edu` by following this [link](https://www.linuxbabe.com/linux-server/ssh-windows). Note: `willow.cs.ttu.edu` is not a link. It is a machine name.
3. Download and install SAT Solver which is MiniSat version 1.14 to this Linux machine, type: 
```sh
$ wget http://minisat.se/downloads/MiniSat_v1.14_linux
$ chmod u+x MiniSat_v1.14_linux
```
### <a name="more-sat"></a> More about MiniSat version 1.14
- Carefully read this [link](https://dwheeler.com/essays/minisat-user-guide.html) for instructions on how to invoke MiniSat, how to save a solution, and how to get all solutions.
You will not need to use any of MiniSat’s optional flags.
- To run the MiniSat
    - Require input file in a simplified "DIMACS CNF" format, follow steps below to create the simple one to test, [More info](https://linuxize.com/post/how-to-use-nano-text-editor/).
        - To create input.cnf file, type:
        ```sh
        $ nano input.cnf
        ```
        - Paste the text below to the terminal,
        ```
        p cnf 5 4
        1 -5 4 0
        -1 5 3 4 0
        -3 -4 0
        -1 -2 3 -4 -5 0
        ```
        - To save the file, press `Ctrl+o`.
        - To exit nano press `Ctrl+x`.
    - To get the solution, type:
    ```sh
    $ ./MiniSat_v1.14_linux input.cnf output.txt
    ```
    - To read the solution, type:
    ```sh
    $ cat output.txt
    ```
    The output.txt should show as below,
    ```
    SAT
    1 -2 -3 4 5 0
    ```


-----------------------------------------------------
## <a name="download-project"></a> Download project to Local machine
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

----------------------------------------------------

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
----------------------------------------------------

## <a name="run-project"></a> Run project
Inside the N-Queens directory, use the Command Prompt or Terminal and type:

```sh
$ make run
```
----------------------------------------------------
## <a name="help"></a> Help
Inside the N-Queens directory, use the Command Prompt or Terminal and type:
```sh
$ make help
```

----------------------------------------------------

## <a name="how-to-use"></a> How to use this program
1.  Connect to TTUnet VPN by following this [link](https://www.askit.ttu.edu/portal/app/portlets/results/viewsolution.jsp?guest=0&solutionid=181128172622147&hypermediatext=null).
2. Enter your eraider username.
3. Enter your eraider password.
4. Select your options.