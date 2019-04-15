#1) Search for:
import debugInfo
debugInfo.SetDebugMode(__DEBUG__)
# Add after:
""" BUILTIN - DEBUG FORMATTER
	__author__  = 'VegaS'
	__date__    = '2019-04-15'
	__version__ = '1.0'

	# A simple debug class which is used for output the messages.
	# The class doesn't need to be called, we've added the functions into built-in functions.
	# The purpose was to ease the work of developers, the new method:
	# Difference between them?
		>> Using the new method:
			TraceError("str", 1, 4.0, (31, 22), [100, 200], True)
			Tracef("str", 1, 4.0, (31, 22), [100, 200], True)
			LogBox("str", 1, 4.0, (31, 22), [100, 200], True)
			sys_err("str", 1, 4.0, (31, 22), [100, 200], True)
			_______________________________________________
			# No import needed, is a built-in function, you can call it everywhere.
			# The function sys_err or TraceError doing the same thing.
			# Allow to pass unlimited argument-lines, no data types check, can be everything you want: <int, float, string, tuple, list, boolean>.
			
		>> Using the old method:
			import dbg
			dbg.TraceError("just_one_string_allowed")
			dbg.Tracef("just_one_string_allowed")
			dbg.LogBox("just_one_string_allowed")
			_______________________________________________
			# Need to import the module dbg every time in every file where you want to use it.
			# Allow to pass just one argument-line which need to be string, otherwise nothing happen.

	# Built-In-Functions:
		Built in or inbuilt function are that type of functions which are already defined or created in a program or in programming framework. 
		User don’t need to create these type of functions. 
		User or developer can directly use built in function by only call it.
		This function is built into an application and can it can be accessed by end-users with simply call it.

	# How-It-Works:
		TraceError(args) - function prints the given arguments to the text stream file syserr.txt
		Tracef(args) - function prints the given arguments to the console window (screen) while executable is compiled in a debug mode.
		LogBox(args) - function prints the given arguments to the dialog box that contains a system icon, a set of buttons, 
			and a brief application-specific message, such as status or error information.
		sys_err(args) - same as TraceError.

	# How-To-Call-Ex <TraceError or sys_err>:
		sys_err('warning', 'error', 'unknown')
			<< 0415 17:08:01130 :: warning
			<< 0415 17:08:01130 :: error
			<< 0415 17:08:01130 :: unknown

		sys_err(100/2==50, 'set value to {}'.format(25))
			<< 0415 17:06:01083 :: True
			<< 0415 17:06:01083 :: set value to 25
		
		sys_err([45, 100], (200, 1500, 32), 42.8, 500, "donald-trump", False)
			<< 0415 17:08:01060 :: [45, 100]
			<< 0415 17:08:01060 :: (200, 1500, 32)
			<< 0415 17:08:01060 :: 42.8
			<< 0415 17:08:01060 :: 500
			<< 0415 17:08:01060 :: donald-trump
			<< 0415 17:08:01060 :: False

		sys_err("what-you-want")
			<< 0415 17:08:01072 :: what-you-want
"""
class DBG:
	# States
	STATE_SYS_ERR, STATE_CONSOLE, STATE_LOGBOX = range(0, 3)
	
	# Functionss
	FUNC_ADRESS_DICT = {
		STATE_SYS_ERR : lambda arg : dbg.TraceError(arg),
		STATE_CONSOLE : lambda arg : dbg.Tracen(arg),
		STATE_LOGBOX : lambda arg : dbg.LogBox(arg)
	}

	@staticmethod
	def Execute(state, lines):
		""" A execute method which allow you to send unlimited arguments lines for debugging. """
		# If the state is console (Tracef), check if compiled executable is in debug-mode or not.
		isDebugMode = True if not __DEBUG__ else False
		if state == DBG.STATE_CONSOLE and not isDebugMode:
			return

		# If argument lines is just a string, convert it into a tuple.
		if not isinstance(lines, (tuple, list)):
			lines = tuple([lines])

		for line in lines:
			execute = DBG.FUNC_ADRESS_DICT.get(state, DBG.STATE_SYS_ERR)
			# Convert the argument line into a string every time, so you can use any type of data for each line.
			execute('{}'.format(line))

__builtin__.TraceError = lambda *args : DBG.Execute(DBG.STATE_SYS_ERR, args)
__builtin__.Tracef = lambda *args : DBG.Execute(DBG.STATE_CONSOLE, args)
__builtin__.LogBox = lambda *args : DBG.Execute(DBG.STATE_LOGBOX, args)
__builtin__.sys_err = __builtin__.TraceError