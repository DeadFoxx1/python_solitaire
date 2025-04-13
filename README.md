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
#normal (no debug and draw 3)
python main.py

#easy mode
python  main.py --cardstodraw=1

#debug mode
python main.py --debug=True

#you can use both args at the same time
python main.py --debug=True --cardstodraw=1
```
# DEBUG:  
Run for debug output:
```sh
python main.py --debug=True
```
Each card object \__str__() is shown like this:
```sh
#5 of clubs that is face down:
5CFalse
```  
Face cards are still their number value:
```sh
#king of clubs facing up:
13CTrue
```
Foundations and the very top of the columns are also card objects:
```sh
#all tops of the top columns are:
140True

#the foundations (specific to their suit):
0HTrue 
```
Other moves:
```sh
#valid move:
move 1STrue to 0STrue

#invalid move:
invalid move

#a card drawing:
draw
```
