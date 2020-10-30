<h1 align="center">
    Fairfield College Preparatory School<br>
    Computer Programming - Mr. Mesquita<br>
    HW 6-4
</h1>

<h2 align="center">
    Due before 8:30 AM on 10/30 (10 pts.)<br>
    https://classroom.github.com/a/c4gLS6_s
</h2>

### The Calendar Module

---

Answer each of the following questions in the same Python file named `hw6-4.py`. In your heading, put your name and the date you began working on the file. You will need the `calendar` module for this assignment so be sure to import it at the beginning of your file.

The first line of each question should be a comment with `Question #` where the `#` is the number of the question. The next lines should the use functions of the module that completes the desired task.

*Example*

``` python
# Question 0
your answer to the question
```

1. Try adding the following statement to your file:
    ```python
    calendar.TextCalendar().pryear(2020)
    ```
    Run the file and see what happens.

2. Observe that the week starts on Monday. Assume that you wanted to change this to help one of the Jesuits, who argues that his week begins Sunday. Read the documentation for `TextCalendar` and see how you can help him print a calendar that suits his needs.

3. Find a function in the calendar module that will print only the month in which your birthday occurs this year.

4. Try adding the following statement to your file:
    ``` python
    calendar.LocaleTextCalendar(6, "SPANISH").pryear(2020)
    ```
   Try other languages including one that doesn't work and see what happens. Be sure to add a new copy of this statement for each language you try. When you try one that doesn't work, comment it out after seeing what happens.

5. Experiment with `calendar.isleap`. What does it expect as an argument? What does it return as a result? What type of value is this? *Hint: You will need print statements for this question*

<p align="center">	Be sure to commit your code before the deadline. Only the latest commit will be graded.</p>
