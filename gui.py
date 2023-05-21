import tkinter as tk
from tkinter import *



def draw_board():
    canvas.create_line(100, 0, 100, 300)
    canvas.create_line(200, 0, 200, 300)
    canvas.create_line(0, 100, 300, 100)
    canvas.create_line(0, 200, 300, 200)

root = tk.Tk() # creates a tkinter window  -- main window represented buy "root"
canvas = tk.Canvas(root, width=300, height=300) # creates a canvas to display in tkinter window ("root)-- canvas is a rectangular widget 
canvas.pack() # .pack() displays widget on screen (in this case, the widget is a canvas)
draw_board()

#create empty lists with the positions of x, o, and entangled pairs

is_full = [0, 0, 0, 0, 0, 0, 0, 0, 0]
played_buttons = []

entangled = []
turnCounter = 1

players = ["X", "Y"]




#def entangle():
#def run_game():
    #code for collapsing quantum states

thirty_button_x = Button(root, text="30X", command=lambda: place_val(30, "X"))
forty_button_x = Button(root, text="40X", command=lambda: place_val(40, "X"))
fifty_button_x = Button(root, text="50X", command=lambda: place_val(50, "X"))
sixty_button_x = Button(root, text="60X", command=lambda: place_val(60, "X"))
seventy_button_x = Button(root, text="70X", command=lambda: place_val(70, "X"))
hundred_button_x = Button(root, text="100X", command=lambda: place_val(100, "X"))


thirty_button_y = Button(root, text="30Y", command=lambda: place_val(30, "Y"))
forty_button_y = Button(root, text="40Y", command=lambda: place_val(40, "Y"))
fifty_button_y = Button(root, text="50Y", command=lambda: place_val(50, "Y"))
sixty_button_y = Button(root, text="60Y", command=lambda: place_val(60, "Y"))
seventy_button_y = Button(root, text="70Y", command=lambda: place_val(70, "Y"))

all_buttons = [thirty_button_x, forty_button_x, fifty_button_x, sixty_button_x, seventy_button_x, thirty_button_y, forty_button_y, fifty_button_y, sixty_button_y, seventy_button_y]




def place_val(number, player):
    def on_click(event):
        x = event.x
        y = event.y
        global turnCounter
        turnCounter = turnCounter+1
        row = y // 100
        col = x // 100 
        pos = coord_to_num(row, col)
        val = str(number)+player
        

        
        if is_full[pos] == 0 and is_valid_move(val, player): # checking to make sure cell is empty before placing o
            draw_number(row, col, number, player)
            is_full[pos] = 1
            add_to_entangled(row, col, number, player)
            currentButton = get_button(number, player)
            played_buttons.append([number, player])

            # change player
            newPlayer = changeplayer(player)
            if(turnCounter == 9):
                disable_buttons_except_hundred()
            elif is_comp_turn(turnCounter):
                #complementary_number = get_complementary_number(number)
                complementary_button = get_complementary_button(number, player)
                disable_buttons_except_complementary(complementary_button, currentButton)

            elif not is_comp_turn(turnCounter):
                enable_except_played(played_buttons)
            
            
            
            # now want to disable all buttons except for the complementary button

            
            
    canvas.bind('<Button-1>', on_click)


def add_to_entangled(row, col, number, player):
    entangled.append([coord_to_num(row, col), number, player])


def print_vals():
    print(entangled)
    print(turnCounter)
    print(played_buttons)

    

print_button = Button(root, text="print", command=print_vals) ## for debugging purposes 

#rungame = Button(root, text = "Run Game", command = run_game)

thirty_button_x.pack()
forty_button_x.pack()
fifty_button_x.pack()
sixty_button_x.pack()
seventy_button_x.pack()
hundred_button_x.pack()


thirty_button_y.pack()
forty_button_y.pack()
fifty_button_y.pack()
sixty_button_y.pack()
seventy_button_y.pack()


print_button.pack()

#run_game = Button(root, text="Run Game", command=lambda: runGame)



# functions for drawing numbers 30-100  
def draw_number(row, col, number, player):
    x1, y1 = col * 100 + 10, row * 100 + 10
    x2, y2 = (col + 1) * 100 - 10, (row + 1) * 100 - 10
    x_center, y_center = (x1 + x2) // 2, (y1 + y2) // 2
    canvas.create_text(x_center, y_center, text=str(number)+player, font=("Arial", 36))

# ... 30



   

def coord_to_num(row, col):
    num = row * 3 + col 
    # 0-8 going across first, then down 
    return num 

def is_valid_move(number, player):
    if (player == "X" and str(number)[-1] == "X") or (player == "Y" and str(number)[-1] == "Y"):
        return True
    return False



def get_button(number, player):
    if player == "X":
        if number == 30:
            return thirty_button_x
        elif number == 40:
            return forty_button_x
        elif number == 50:
            return fifty_button_x
        elif number == 60:
            return sixty_button_x
        elif number == 70:
            return seventy_button_x
    else:
        if number == 30:
            return thirty_button_y
        elif number == 40:
            return forty_button_y
        elif number == 50:
            return fifty_button_y
        elif number == 60:
            return sixty_button_y
        elif number == 70:
            return seventy_button_y
        
def get_complementary_button(number, player):
    if player == "X":
        if number == 30:
            return seventy_button_y
        elif number == 40:
            return sixty_button_y
        elif number == 50:
            return fifty_button_y
        elif number == 60:
            return forty_button_y
        elif number == 70:
            return thirty_button_y
    else:
        if number == 30:
            return seventy_button_x
        elif number == 40:
            return sixty_button_x
        elif number == 50:
            return fifty_button_x
        elif number == 60:
            return forty_button_x
        elif number == 70:
            return thirty_button_x

def enable_button(button):
    button.config(state=NORMAL)

def disable_button(button):
    button.config(state=DISABLED)


def disable_buttons_except_complementary(comp_button, current_button):
    for player in players:
        for i in range (30, 80, 10):
            button = get_button(i, player)
            if button!=comp_button:
                disable_button(button)
    disable_button(current_button)
    disable_button(hundred_button_x)
    enable_button(get_complementary_button(comp_button))




def enable_except_played(played_buttons_list):
    for button in all_buttons:
        enable_button(button)
    for val in played_buttons_list:
        disable = get_button(val[0], val[1])
        disable_button(disable)
    disable_button(hundred_button_x)
    
    




def changeplayer(current_player):
    if current_player == "X":
        return "Y"
    else:
        return "X"
    
def is_comp_turn(counter):
    if counter%2 == 0:
        return True
    else:
        return False

def disable_buttons_except_hundred():
    for button in all_buttons:
        disable_button(button)
    enable_button(hundred_button_x)
    



root.mainloop() # starts the main event and displays the gui