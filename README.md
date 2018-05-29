# Console analysis application for the most frequent matches among the most frequent verbs for python projects

This is a tutorial work for the second task in the OTUS “Python web-developer” course.
Link to a task: https://gist.github.com/Melevir/5754a1b553eb11839238e43734d0eb79

# Usage objective

The application analyses and shows how frequently the most common verbs in function names repeat in a python projects set.
For example, the result `('take', 5) 2` shows the verb `take` was found `5` times inside each project for all ‘2’ python projects.

# Main features:

- A programming language is Python 3.
- A projects set is established inside the code.
- Due to this application is for console usage, results are outputted in console in the form of column, where every string has a construction has mentioned in ` Usage objective`.
- Due to verbs determination is based on `nltk`-library algorithm, some words having different parts of speech may be recognized as not verbs.
- The application includes a file for Unit-test and proper testing data for this task.

#User guide

1. Clone or download with extracting this application.
2. Install required libraries:
```bash
$ pip install requiremets.txt
```
3. Put the application file `projects_functions_verbs.py` to inside the folder with python projects. Make sure that the folder `test_data` is not located inside the same folder where application file is.
4. `django` and `flask` projects are set as default. If there is requirement to point certain projects from a user’s set, open the application file and change the content of the variable `projects` pointing the folders names of projects.
5. Open console and launch the application file:
```bash
$ pyhon3 projects_functions_verbs.py
```
6. Take results in console.

#Testing options

1. For internal testing put the folder `test_data` to inside the folder where the application file `projects_functions_verbs.py` is and launch this application the same way has pointed above.
2. For Unit-test also testing put the folder `test_data` to inside the folder where the application file `projects_functions_verbs.py` is and launch the file `tests.py` the same way has pointed above.
