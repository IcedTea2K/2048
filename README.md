# ![2048 Logo](https://upload.wikimedia.org/wikipedia/commons/8/8a/2048_logo.png)

## Descriptions
This game is my end-of-year resolution. I started the project a while back but really got into it in the last two weeks of Decemeber. And I finished it 5 minutes before the new year!! 

Anyway, it's the classic 2048 game that took over the internet a few years back. The premise is quite simple: combine like squares to get highest score as possible. The control is only the arrow keys on the keyboard.

## Requirements
- Python3 interpreter 
- Pygame module
- And that's all!

## How it's made
For those interested, here's a few things that help recreate the game:

- As a 4x4 square, the grid includes 16 different cells. It's very helpful to create Rect object for each of them. The Rect can then be used as location and destination for the squares. For example, if the square is at (0,0) or top-left, pressing right will have it travel to (0,3) top-right (unless there are some squares blocking its way).
- Squares are contained in a single 1D array. They are not stored in any particular order so, the list needs to be organized before the squares can be moved in ```moveSquares()```. 
- There is also a dict called ```occupiedCells``` which as the name suggests, keeps track of the cells that are occupied. This allows the squares to stop before other squares or combing with them if they have the same number. 
- The function ```updateSquares()``` is the one filtering out those that are "disabled" or absorbed to other squares. It's mainly active when all square are done moving. It also spawns squares randomly with ```spawnSquares()``` (when all the animaiton is done).
- The graphics side of the game is quite simple after getting used to the pygame module. Especially, ```pygame.Rect```, ```pygame.Surface``` and ```pygame.Font```. 
  - ```pygame.Rect``` contains the position and size of the surface. Most of re-positioning can be done through rect whose effects can then be seen after blitting the surface onto Screen.
  - ```pygame.Surface```, despite the above description of rect, when doing something with scaling, the effects need to be done on both objects. After ```pygame.inflate_ip()``` the rect by some amount, ```pygame.transform.scale()``` the surface by the same amount using rect. Or else, the surface will appear moving for some reason.
  - ```pygame.Font``` needs to be created with every desired font and font size. The ```render``` method will create a surface for the text whose rect can be obtained using ```Surface.get_rect()``` with specified position. Then they can be blit onto the screen. 

## TODO:
- ~~Add more comprehensive README~~
- Clean up the code
