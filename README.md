
# Metin2 Builtin Debug Formatter

A simple debug class which is used for output the messages.
The class doesn't need to be called, we've added the functions into built-in functions.
The purpose was to ease the work of developers, the new method:
Difference between them?
- Using the new method
```py
TraceError("str", 1, 4.0, (31, 22), [100, 200], True)
# No import needed.
# Allow to pass unlimited argument-lines, no data types check, can be everything you want: <int, float, string, tuple, list, boolean>.
```

- Using the old method
```py
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
<< 415 17:8:1130 :: warning
<< 415 17:8:1130 :: error
<< 415 17:8:1130 :: unknown

TraceError(100/2==50, 'set value to {}'.format(25))
<< 415 17:6:1083 :: True
<< 415 17:6:1083 :: set value to 25

TraceError([45, 100], (200, 1500, 32), 42.8, 500, "donald-trump", False)
415 17:8:1094 :: [45, 100]
415 17:8:1094 :: (200, 1500, 32)
415 17:8:1094 :: 42.8
415 17:8:1094 :: 500
415 17:8:1094 :: donald-trump
415 17:8:1094 :: False

TraceError("what-you-want")
<< 415 17:8:1072 :: what-you-want
```
