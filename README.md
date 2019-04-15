
A simple debug class which is used for output the messages.
The class doesn't need to be called, we've added the functions into built-in functions.
The purpose was to ease the work of developers, the new method:
Difference between them?
- Using the new method
```c
TraceError("str", 1, 4.0, (31, 22), [100, 200], True)
# No import needed.
# Allow to pass unlimited argument-lines, no data types check, can be everything you want: <int, float, string, tuple, list, boolean>.
```

- Using the old method
```c
import dbg
dbg.TraceError("just_one_string_allowed")
# Need to import the module dbg every time in every file where you want to use it.
# Allow to pass just one argument-line which need to be string, otherwise nothing happen.
```

# Built-In-Functions:
Built in or inbuilt function are that type of functions which are already defined or created in a program or in programming framework. 
User don’t need to create these type of functions. 
User or developer can directly use built in function by only call it.
This function is built into an application and can it can be accessed by end-users with simply call it.

# How-It-Works:
- **TraceError**(args) - function prints the given arguments to the text stream file syserr.txt
- **Tracef**(args) - function prints the given arguments to the console window (screen) while executable is compiled in a debug mode.
- **LogBox**(args) - function prints the given arguments to the dialog box that contains a system icon, a set of buttons, 
	and a brief application-specific message, such as status or error information.

# How-To-Call-Ex <TraceError>:
```python
TraceError('warning', 'error', 'unknown')
<< 0415 17:08:01130 :: warning
<< 0415 17:08:01130 :: error
<< 0415 17:08:01130 :: unknown

TraceError(100/2==50, 'set value to {}'.format(25))
<< 0415 17:06:01083 :: True
<< 0415 17:06:01083 :: set value to 25

TraceError([45, 100], (200, 1500, 32), 42.8, 500, "donald-trump", False)
<< 0415 17:08:01060 :: [45, 100]
<< 0415 17:08:01060 :: (200, 1500, 32)
<< 0415 17:08:01060 :: 42.8
<< 0415 17:08:01060 :: 500
<< 0415 17:08:01060 :: donald-trump
<< 0415 17:08:01060 :: False

TraceError("what-you-want")
<< 0415 17:08:01072 :: what-you-want
```
