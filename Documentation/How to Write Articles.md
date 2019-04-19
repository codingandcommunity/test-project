# TestArticles
A series of test markdown articles for use in testing the backend for the companion applications Spaceport and Co-Pilot

## How articles should be structured
The markdown file of the article should contain a header which will contain all metadata of the article ie. title, author, date,... and even links to other articles such as the next and the previous article. The metadata should be seperated from article content by three stars. ie.

title: Comments in Python
author: John Smith
date: 4/2/19
next: [Step 2](@step_2.md) ///links not creating within "---"
prev: [Intro](@intro.md)
jump to: @step1.md

***

The markdown file should then contain the content of the article. ie.

---

It is sometimes hard to understand the code you wrote and especially to other people. Comments allow us to make notes in our code and even tell the computer to ignore certain lines of code. You can create a comment by writing `#` before your note or line of code. For example,

```python

# this a comment

# the next line will be ignored
# x = 2
a = 3

```
You can tell the computer to ignore multiple lines by using `"""`

```python

"""
Everything inside of here will be ignored.
y = 2 + 5
z = y * 6
"""

```
---

Make sure the content of the article is concise and suited toward a younger audience.
