# Virtual Studio Code Debugger Guide

This step-by-step guide will take you though Virtual Studio (VS) code setup to getting used to this powerful tool.
The hope is by the time you have finished reading this, you will be able to find and fix bugs in your code efficiently.

## Setup

Lets start at the very beginning, the VS code installlation.
[Go to the VS Code website](https://code.visualstudio.com) and download the correct version. 
I recommend that you download the stable version.
Now, follow the steps to complete the installation process.
Right about now you should be ready to get started with coding so simply open a project and we can go on to the next steps.

## Key Debugging Actions and Information

This section contains a basic overview of debugger funtions and other good features. 
Getting used to using each of these steps is essential to understanding and utilizing the debugger effectively.

### Step Over (F10): 

This command moves the debugger to the next line of code in the same scope. 
If the next line contains a function call, 'Step Over' will execute that function completely without pausing inside it, essentially "stepping over" the function. 
It's useful for skipping functions you know are working correctly.

### Step Into (F11): 

When you use 'Step Into', if the current line of code contains a function call, the debugger will enter that function and pause at its first line, effectively "stepping into" it.
This action is used when you want to inspect the workings of a function in detail, especially if you suspect there's an issue inside it.

### Step Out (Shift + F11):

This command is used when you're done inspecting a function and want to return to the calling function. 
'Step Out' will execute the rest of the current function's code and pause when it returns to the function that called it. 
It's a way to quickly exit the current function context when you either are done inspecting a function, are in a deeply nested function, are inspecting the wrong function, or simply want to optimize your time and move to a more pressing issue.

### Continue (F5): 

This resumes the execution of your code until it reaches the next breakpoint (a manually set pause point). 
If there are no further breakpoints, the program will run to completion. 
It's used when you want to skip to specific parts of your code marked by breakpoints.

### Pause (F5): 

The 'Pause' action (often mapped to a different key) allows you to suspend a running program to start debugging at the current execution point. 
It's useful when you want to start inspecting a program that's currently running, but not at a breakpoint. 
Pause is also useful when you encounter errors that are hard to replicate when just stopping at a breakpoint.

### Watch Variables: 

In many debugging environments, you can add variables to a list to watch them more closely. 
This list shows the current values of these variables in real-time as the code executes. 
It's beneficial for tracking how values change, especially in loops or complex functions.

### Inspect Variables: 

By simply hovering over variables in your code during a debugging session, you can see their current values. 
It's a quick way to check and inspect variable values without adding them to a watch list.

### View Call Stack: 

The call stack shows the sequence of function calls that led to the current point of execution. 
It's very useful for understanding the path your program took to get to its current state, especially when dealing with complex function calls and recursion.

### Restart (⇧⌘F5): 

This command stops the current execution of the program and starts it over again from the beginning, using the same run configuration. 
It's helpful when you want to rerun your program from the start to test changes or re-examine its behavior.

### Stop (⇧F5): 

This command terminates the current debugging session. It stops the execution of your program immediately. 
Use this when you're done debugging or if you want to halt a running program that's not behaving as expected.

## Tips

1. Understand Breakpoints: Familiarize yourself with different types of breakpoints like standard, conditional, and logpoint. Standard breakpoints pause execution, conditional ones are triggered when certain conditions are met, and logpoints log messages to the console without stopping the code.
2. Step Through Code Effectively: Learn the difference between 'Step Over', 'Step Into', 'Step Out', and 'Continue' commands. 'Step Into' takes you inside function calls, while 'Step Over' moves to the next line of code without going into functions. Understanding each of these will allow you to effective traverse your code within the debugger.
3. Configure Launch.json: Familiarize yourself with launch.json for advanced debugging configurations. Ceating a launch configuration file is beneficial because it allows you to configure and save debugging setup details
4. Learn Keyboard Shortcuts: Familiarize yourself with VS Code's keyboard shortcuts for debugging. This can significantly speed up your debugging process.
