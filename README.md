# dpla-similar-item-finder

This is a project designed as an experiment in serendipitous discovery in [DPLA](https://dp.la).  It contains a python script (in a couple of forms) that uses the DPLA API to search for items that might be similar to a given item in DPLA.

The bulk of the code makes up a Flask web application.  The meat of the DPLA querying code is in findItem.py.  There is also a Jupyter notebook version of essentially the same code, as well as various other python scripts that I created as practice and testing for the main project. 

Built in Python 3.9.9. Uses the [DPLA API](https://pro.dp.la/developers/api-codex) for interacting with DPLA dataset, and [DPyLA](https://github.com/bibliotechy/DPyLA/blob/master/README.md) for interacting with the api.

This is my first time using Flask, as well as Jupyter notebooks, and only my second real project in Python. I'm sure there are things I could be doing differently/better, so please reach out if you have suggestions to improve it!

A lot of the inspiration for this project, especially the Jupyter notebook version, comes from the [GLAM Workbench project](https://glam-workbench.net/).  Much of what I learned about Flask comes from Miguel Grinberg's [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).
