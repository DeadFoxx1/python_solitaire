![image](https://github.com/user-attachments/assets/085c7a94-588e-4464-9fee-828ca60ee226)
# About:
I started this project as soon as I learned about what a python class is.  
Also, I don't remember how I got the card assets. some I made myself (by coloring over others)    
Also also (last one), This was originaly a school project :p  

# Dependencies:
python  
pygame  
pygbag (for running web version)

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
.\.venv\Scripts\activate
```
## 3. Install dependencies:
```sh
pip install -r requirements.txt
```
## 4. Run it :3
Normal (no debug and draw 3):
```sh
python main.py
```
For web version using pygbag:
```sh
pygbag --ume_block 0 main.py
```
Runs on localhost:8000  
There's a weird awaiting input screen so use --umn-block 0 to remove it  
Currently dosent support the use of the extra options

## 5. Extra options:
```sh
#see -h for help
python main.py -h
```
```
usage: main.py [-h] [-d DEBUG] [-c CARDSTODRAW]

options:
  -h, --help            show this help message and exit
  -d, --debug DEBUG     enables debug output
  -c, --cardstodraw CARDSTODRAW
                        number of cards to draw at a time (must be less then 24)
```
```sh
#easy mode
python  main.py -c=1

#debug mode
python main.py -d=True

#you can use both args at the same time
python main.py -d=True -c=1
```
# DEBUG:  
Run for debug output:
```sh
python main.py -d=True
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
invalid move (3CTrue to 13HTrue)

#a card drawing:
draw
```
