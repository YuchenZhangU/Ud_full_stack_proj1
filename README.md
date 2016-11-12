## How to run the code?
Download the three python files and make them under the same fold. Run the entertainment_center.py file.
Example: In command line, type:
```python
python entertainment_center.py
```

## How the program works?
In entertainment_center.py, 6 movive objects are constructed as instance of Class Moive defined in media.py. The 6 moive objects are wrapped into a iterable list and passed as a parameter into function open_movies_page defined in fresh_tomatoes.py. The function renders the page template by the data of moive attributes, creates an html page and finally open it.

## Python Fils
**entertainment_center.py**  - define moive objects and execute page generation function

**media.py**  - define Moive Class

**fresh_tomatoes.py**  - page template and the function to render, create and open page