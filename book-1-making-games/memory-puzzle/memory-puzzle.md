# Memory puzzle

http://inventwithpython.com/pygame/
http://inventwithpython.com/pygame/chapter3.html

- v1:    BASIC ARHITECTURE, timing, quit event. stable application
- v2:    mouse coordinates, events
- v3:    create playing grid, and clicked positions, game grid, boxes, transformations
- v3_2:  pixel, grid all using touples
- v4:    finished grid with dictionary, moved to card logic
- v5:    creating card icons, list, shuffle icons
- v6:    creating game logic and state transitions    
- v7:    add animation of turn card around after 2 sec

- Making Sure We Have Enough Icons
Tuples vs. Lists, Immutable vs. Mutable
One Item Tuples Need a Trailing Comma
Converting Between Lists and Tuples
The global statement, and Why Global Variables are Evil
Data Structures and 2D Lists
The “Start Game” Animation
The Game Loop
The Event Handling Loop
Checking Which Box The Mouse Cursor is Over
Handling the First Clicked Box
Handling a Mismatched Pair of Icons
Handling If the Player Won
Drawing the Game State to the Screen
Creating the “Revealed Boxes” Data Structure
Creating the Board Data Structure: Step 1 – Get All Possible Icons
Step 2 – Shuffling and Truncating the List of All Icons
Step 3 – Placing the Icons on the Board
Splitting a List into a List of Lists
Different Coordinate Systems
Converting from Pixel Coordinates to Box Coordinates
Drawing the Icon, and Syntactic Sugar
Syntactic Sugar with Getting a Board Space’s Icon’s Shape and Color
Drawing the Box Cover
Handling the Revealing and Covering Animation
Drawing the Entire Board
Drawing the Highlight
The “Start Game” Animation
Revealing and Covering the Groups of Boxes
The “Game Won” Animation
Telling if the Player Has Won
Why Bother Having a main() Function?