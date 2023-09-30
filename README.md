# Dialogue
A dialogue class for pygame with text crawl
It has two functions, init (the constructor) and update
init takes in 11 arguments (out of which the last 4 are optional)
```
def __init__(self,
    font:pygame.font.Font,
    text:str,
    outline_color:tuple,
    background_color:tuple,
    padding_color:tuple,
    text_color:tuple,
    pos:tuple,
    key:int=pygame.K_SPACE,
    speed:int=8,
    wraplimit:int=250,
    h:int=75)
```
font:pygame.font.Font - It is a pygame.font.Font object, can also take in a pygame.font.Sysfont i think

text:str - It is the text you want the dialogue to display

outline_color:tuple - The color of the border of the dialogue

padding_color:tuple - The color of the padding between the border and the text, has the same width as the border

background_color:tuple - The color behind the text

text_color:tuple - The color of the text the dialogue should display

pos:tuple - Where the dialogue should blit itself to

key:int=pygame.K_SPACE - This argument has to be a pygame.K_ something object, essentially one of the pygame constants which represent a key on the keyboard. It is the key the user presses which tells the dialogue the user wants to move on to the next dialogue or close it. The dialogue itself does not do anything, but when the user presses whatever key you passed in, if the text is finished crawling, the done attribute (a bool) is set to true. You can access this attribute, see its value and do whatever you like with the dialogue class when done is true. There is also another attribute called written which is a bool. When the text is done crawling, it becomes true. It also becomes true if the player clicks on the dialogue, which causes the full text to appear at once (basically a way to skip the dialogue typing and just get the whole dialogue at once). 

speed:int=4 - This is the speed you want your text typed at. IT SHOULD ALWAYS BE SMALLER THAN max_speed (the class attribute before the constructor). If it is equal to or greater than max_speed, the class will crash.

wraplimit:int - This is the width in pixels of the dialogue. The text will wrap to the next sentence when a sentence becomes this long.

h:int - The height of the dialogue box

__update__
the update function takes in the arguments screen and dt

screen: the pygame.Surface you want the dialogue to blit itself onto

dt: this is not for ordinary delta time, this should be (ideal_fps/clock.get_fps())

