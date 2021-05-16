![Fluent Logo](fluent.png)

The official coding language to create apps in rOS, Fluent Beta 0.3.

## Installation
To install, type the following.
```
$ git clone https://github.com/Resist-Tech/Fluent.git
```
Your code will be stored in the `code.fl` file. Running the `compile.py` will run the program. If you want to store your code in a different file, pass the file name as a command line argument when running the `compile.py`.  

## Commands
### Window
The window command works with windows. Here are some examples.
```
window create app
window rename app Resist App
window size app 800 600
window run app
```
`app` is the name of our variable. You could easily specify `window create screen` and it would work just fine. You can have multiple windows this way.

### Place
The place command places widgets such as the button or entry. You would do this.
```
window create app
button create app home
place button x=50 y=50 width=50 height=50
```
None of the describe parameters (eg. x, y) are required. They are set by default to 0, 0, 0, and 0 respective to the usual order.

### Entry
The entry command creates multi-line input fields. They are widgets. Here is an example on how to use them.
```
window create app
entry create app search
place search x=100 y=50 width=100 height=50
```

### Button
The button command creates buttons. They are widgets. Look at this example.
```
window create app
button create app home
place button x=50 y=50 width=50 height=50
```

## Other
### Comments
Comments can be called by using `//`. They are useful when referencing or defining authors.
```
// Resist App
// By Resist Corporation
```
Inline comments can also be used. 
```
window create app // creates app
window rename /* rename command */ app Resist App
window size app 800 600
window run app
```
