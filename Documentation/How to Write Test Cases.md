# How to Write Test Cases
Writing test cases is a great way to start to contribute to a Project or a Curiculum overall. If you find a problem in a program writing a test case to cover it the specific problem helps developers to making stronger code. This is particularly cructial for us because our students code will be verified using our test cases. Once you have written a new test case contact one of the contributors:  

[Edwin Wallis](https://github.com/meowskers)  
[Colleen Corrigan](https://github.com/collcorr72)  

And we can see if we can pull it into a our test cases. Each test file should test only one specific function or step.  
## For example:
Take the simple modified function "HelloWord(x)" in the python file "hi.py".  
It takes anything as its paramter and will always return the string "Hello World".   
One obvious test would be to input an int, lets say 1, and check that the function returns "Hello World".

##Creating a new test file
Step 1:  
Import the unitest module.  
```python
import unittest  
```
  
Step 2:  
Because of the structure of Projects we need to change directories to back out of the test structures. First we have to import system and then set the path. ".." backs out once. If the testing file is in the same directory as the file to be tested then you can ignore this step  
```python
import sys  
sys.path.insert(0,"..") 
```
  
Step 3:  
Next we need to set up the test class. 
```python
class MyTest(unittest.TestCase):
```

Step 4:  
Now we can write a test case in the class!  
```python
def test_Integer(self):  
    self.assertEquals(hi.HelloWorld(1),"Hello World") 
```
*Important* your test case must start with "test_" otherwise it will not register as a test case   
Step 5:  
We have to add the call and add the __name__=='main' guard
```python
if __name__ == '__main__':
    unittest.main()
```
Step 6:  
If we run the python file now it will test the python function and will report which tests have failed or passed.   
## Adding new test cases   
Keep writing new test cases. It is important to get to as close to 100% code coverage as you can. Another way to think of other test cases is to try and input values and try to get unexpected values. A different idea is to test random data this can be hard to verify sometimes but can be a very effective.  
 
To write a new test case just repeat Step 4 change the name and test something new. 
   
## TLDR 
Your file should look something like this:
```python
import unittest  
import sys  
sys.path.insert(0,"..")  
class MyTest(unittest.TestCase):  
    def test_Integer(self):  
        self.assertEquals(hi.HelloWorld(1),"Hello World)"   
    def test_String(self):  
        self.assertEquals(hi.HelloWorld("hi"),"Hello World)"  
    def test_List(self):  
        Foo = list()  
        self.assertEquals(hi.HelloWorld(Foo),"Hello World")
if __name__ == '__main__':
    unittest.main()
```
