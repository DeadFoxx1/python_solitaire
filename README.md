# About:
I started this project as soon as I learned about what a python class is.  
THIS MEANS ITS TRASH!!!  
Honestly don't know what I was doing with this lol  
Also this was before I had a GitHub account so thats why the commits are all wonky  
Also also, I don't remember how I got the card assets. some I made myself (by coloring over others)    
Also also also (last one), This was originaly a school project :p 

# Dependencies:
python  
pygame

# Setup:
## 1. Clone the repo and make a virtual environment:
```sh
git clone https://github.com/DeadFoxx1/python_Solitaire
cd python_Solitaire
python -m venv .venv
```
## 2. Activate the venv:
### macOS/Linux:
```sh
source .venv/bin/activate
```
### On Windows:
```sh
 .venv\Scripts\activate
```
## 3. Install dependencies:
```sh
pip install -r requirements.txt
```
## 4. Run it :3
```sh
python main.py
```

# Additional Notes:
1. Is it normal for a python repo README to have instructions on how to make a virtual environment?  
This is literally my first repo so idk what the standard is.  

2. The terminal is set to output the contents of each column for debug purposes (might make a toggle in the future)  
each card object \__str__() is shown like this:
```sh
#5 of clubs that is face down:
5CFalse
```  

3. Face cards are still their number value:
```sh
#king of clubs facing up:
13CTrue
```
4. Foundations and the very top of the columns are also card objects:
```sh
#all tops of the top columns are:
140True

#the foundations (specific to their suit):
0HTrue 
```
5. The contents of the columns are printed before the bottom of the columns are set face up so they are all printed as face down initially (might fix later)

6. a successful move is printed as:
```sh
#valid move:
move 1STrue to 0STrue

#invalid move:
invalid move

#a card drawing:
draw
```
