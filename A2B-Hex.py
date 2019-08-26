from tkinter import *
from math import *

master = Tk()

canvas_width = 1400
canvas_height = 900

w = Canvas(master, width=canvas_width, height=canvas_height)

w.pack()

w.configure(background="dark orange")

hex_side = 50


def create_hex(a, b):
    w.create_line(a - (hex_side * cos(1.0472)), b - (hex_side * sin(1.0472)), a + (hex_side * cos(1.0472)),
                  b - (hex_side * sin(1.0472)), fill="white")
    w.create_line(a + (hex_side * cos(1.0472)), b - (hex_side * sin(1.0472)), a + hex_side, b, fill="black")
    w.create_line(a + hex_side, b, a + (hex_side * cos(1.0472)), b + (hex_side * sin(1.0472)), fill="white")
    w.create_line(a - (hex_side * cos(1.0472)), b + (hex_side * sin(1.0472)), a + (hex_side * cos(1.0472)),
                  b + (hex_side * sin(1.0472)), fill="black")
    w.create_line(a - hex_side, b, a - (hex_side * cos(1.0472)), b + (hex_side * sin(1.0472)), fill="white")
    w.create_line(a - hex_side, b, a - (hex_side * cos(1.0472)), b - (hex_side * sin(1.0472)), fill="black")


x = 170
y = 140


class Coord:
    pass


coords = []


def append_in_coords(cnqrd, vstd, pno, sno, a, b):
    coord_obj = Coord()
    
    coord_obj.c = cnqrd
    coord_obj.v = vstd
    coord_obj.pn = pno
    coord_obj.sn = sno
    coord_obj.i = a
    coord_obj.j = b

    coords.append(coord_obj)


for count in range(0, 7):
    create_hex(x, y + ((2 * count) * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + hex_side + (hex_side * cos(1.0472)),
               y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + (3 * hex_side), y + ((2 * count) * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + (4 * hex_side) + (hex_side * cos(1.0472)),
               y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + (6 * hex_side), y + ((2 * count) * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + (7 * hex_side) + (hex_side * cos(1.0472)),
               y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + (9 * hex_side), y + ((2 * count) * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + (10 * hex_side) + (hex_side * cos(1.0472)),
               y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + (12 * hex_side), y + ((2 * count) * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + (13 * hex_side) + (hex_side * cos(1.0472)),
               y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + (15 * hex_side), y + ((2 * count) * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + (16 * hex_side) + (hex_side * cos(1.0472)),
               y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + (18 * hex_side), y + ((2 * count) * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + (19 * hex_side) + (hex_side * cos(1.0472)),
               y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    create_hex(x + (21 * hex_side), y + ((2 * count) * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 1, x, y + (2 * count * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 8, x + hex_side + (hex_side * cos(1.0472)),
                     y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 15, x + (3 * hex_side), y + (2 * count * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 22, x + (4 * hex_side) + (hex_side * cos(1.0472)),
                     y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 29, x + (6 * hex_side), y + (2 * count * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 36, x + (7 * hex_side) + (hex_side * cos(1.0472)),
                     y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 43, x + (9 * hex_side), y + (2 * count * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 50, x + (10 * hex_side) + (hex_side * cos(1.0472)),
                     y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 57, x + (12 * hex_side), y + (2 * count * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 64, x + (13 * hex_side) + (hex_side * cos(1.0472)),
                     y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 71, x + (15 * hex_side), y + (2 * count * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 78, x + (16 * hex_side) + (hex_side * cos(1.0472)),
                     y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 85, x + (18 * hex_side), y + (2 * count * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 92, x + (19 * hex_side) + (hex_side * cos(1.0472)),
                     y - (hex_side * sin(1.0472)) + (count * 2 * hex_side * sin(1.0472)))

for count in range(0, 7):
    append_in_coords(0, 0, 0, count + 99, x + (21 * hex_side), y + (2 * count * hex_side * sin(1.0472)))


def is_adjacent_true(hex_num, coordinates, pl):
    global chance_text
    if coordinates[hex_num - 1].pn == pl:
        coordinates[hex_num - 1].v = 1
        if hex_num > 98:
            if pl == 1:
                w.delete(chance_text)
                w.create_text(700, 25, fill="black", font="times 20 bold", text="PLAYER 1 WINS")
                w.unbind("<Button-1>", click)
            if pl == 2:
                w.delete(chance_text)
                w.create_text(700, 25, fill="white", font="times 20 bold", text="PLAYER 2 WINS")
                w.unbind("<Button-1>", click)
        if hex_num % 14 == 0:
            if (hex_num + 5) < 105:
                if coordinates[hex_num + 5].v != 1:
                    is_adjacent_true(hex_num + 6, coordinates, pl)
            if (hex_num + 6) < 105:
                if coordinates[hex_num + 6].v != 1:
                    is_adjacent_true(hex_num + 7, coordinates, pl)
            if (hex_num - 2) < 105:
                if coordinates[hex_num - 2].v != 1:
                    is_adjacent_true(hex_num - 1, coordinates, pl)
        else:
            if hex_num % 7 == 0 and hex_num % 14 != 0:
                if (hex_num + 6) < 105:
                    if coordinates[hex_num + 6].v != 1:
                        is_adjacent_true(hex_num + 7, coordinates, pl)
                if (hex_num - 2) < 105:
                    if coordinates[hex_num - 2].v != 1:
                        is_adjacent_true(hex_num - 1, coordinates, pl)
            else:
                if hex_num % 14 == 1:
                    if (hex_num + 6) < 105:
                        if coordinates[hex_num + 6].v != 1:
                            is_adjacent_true(hex_num + 7, coordinates, pl)
                    if (hex_num + 7) < 105:
                        if coordinates[hex_num + 7].v != 1:
                            is_adjacent_true(hex_num + 8, coordinates, pl)
                    if (hex_num) < 105:
                        if coordinates[hex_num].v != 1:
                            is_adjacent_true(hex_num + 1, coordinates, pl)
                else:
                    if hex_num % 7 == 1 and hex_num % 14 != 1:
                        if (hex_num + 6) < 105:
                            if coordinates[hex_num + 6].v != 1:
                                is_adjacent_true(hex_num + 7, coordinates, pl)
                        if (hex_num) < 105:
                            if coordinates[hex_num].v != 1:
                                is_adjacent_true(hex_num + 1, coordinates, pl)
                    else:
                        if hex_num % 14 in range(9, 14):
                            if (hex_num + 5) < 105:
                                if coordinates[hex_num + 5].v != 1:
                                    is_adjacent_true(hex_num + 6, coordinates, pl)
                            if (hex_num + 6) < 105:
                                if coordinates[hex_num + 6].v != 1:
                                    is_adjacent_true(hex_num + 7, coordinates, pl)
                            if (hex_num - 2) < 105:
                                if coordinates[hex_num - 2].v != 1:
                                    is_adjacent_true(hex_num - 1, coordinates, pl)
                            if (hex_num) < 105:
                                if coordinates[hex_num].v != 1:
                                    is_adjacent_true(hex_num + 1, coordinates, pl)
                        else:
                            if hex_num % 14 in range(2, 7):
                                if (hex_num + 6) < 105:
                                    if coordinates[hex_num + 6].v != 1:
                                        is_adjacent_true(hex_num + 7, coordinates, pl)
                                if (hex_num + 7) < 105:
                                    if coordinates[hex_num + 7].v != 1:
                                        is_adjacent_true(hex_num + 8, coordinates, pl)
                                if (hex_num - 2) < 105:
                                    if coordinates[hex_num - 2].v != 1:
                                        is_adjacent_true(hex_num - 1, coordinates, pl)
                                if (hex_num) < 105:
                                    if coordinates[hex_num].v != 1:
                                        is_adjacent_true(hex_num + 1, coordinates, pl)


def is_player_winner(coordinates, pl):
    for first_row in range(0, 7):
        if coordinates[first_row].pn == pl:
            coordinates[first_row].v = 1
            if coordinates[first_row].sn == 1:
                if coordinates[coordinates[first_row].sn + 6].v != 1:
                    is_adjacent_true(coordinates[first_row].sn + 7, coordinates, pl)
                if coordinates[coordinates[first_row].sn + 7].v != 1:
                    is_adjacent_true(coordinates[first_row].sn + 8, coordinates, pl)
                if coordinates[coordinates[first_row].sn].v != 1:
                    is_adjacent_true(coordinates[first_row].sn + 1, coordinates, pl)
            else:
                if coordinates[first_row].sn == 7:
                    if coordinates[coordinates[first_row].sn + 6].v != 1:
                        is_adjacent_true(coordinates[first_row].sn + 7, coordinates, pl)
                    if coordinates[coordinates[first_row].sn - 2].v != 1:
                        is_adjacent_true(coordinates[first_row].sn - 1, coordinates, pl)
                else:
                    if coordinates[coordinates[first_row].sn + 6].v != 1:
                        is_adjacent_true(coordinates[first_row].sn + 7, coordinates, pl)
                    if coordinates[coordinates[first_row].sn + 7].v != 1:
                        is_adjacent_true(coordinates[first_row].sn + 8, coordinates, pl)
                    if coordinates[coordinates[first_row].sn - 2].v != 1:
                        is_adjacent_true(coordinates[first_row].sn - 1, coordinates, pl)
                    if coordinates[coordinates[first_row].sn].v != 1:
                        is_adjacent_true(coordinates[first_row].sn + 1, coordinates, pl)


chance = 0

w.create_text(500,735,fill="black",font="times 20 bold",text="PLAYER 1 : BLACK")
w.create_text(900,735,fill="white",font="times 20 bold",text="PLAYER 2 : WHITE")

w.create_text(65,400,fill="gray40",font="times 100 bold",text="A")
w.create_text(1330,400,fill="gray40",font="times 100 bold",text="B")

chance_text = w.create_text(700,25,fill="black",font="times 20 bold",text="PLAYER 1's CHANCE")

def click(event):
    global chance
    smallest = 10000
    for obj in coords:
        distance = sqrt(((event.y - obj.j) ** 2) + ((event.x - obj.i) ** 2))
        if distance < smallest:
            smallest = distance
            closest = obj.sn

    closest_i = coords[closest - 1].i
    closest_j = coords[closest - 1].j

    if coords[closest-1].c == 0:

        global chance_text
        coords[closest-1].c = 1
        chance = chance + 1

        if (chance % 2) == 1:
            coords[closest - 1].pn = 1
            w.create_oval(closest_i - 25, closest_j - 25, closest_i + 25, closest_j + 25, fill="black")
            w.delete(chance_text)
            chance_text = w.create_text(700, 25, fill="white", font="times 20 bold", text="PLAYER 2's CHANCE")
        else:
            coords[closest - 1].pn = 2
            w.create_oval(closest_i - 25, closest_j - 25, closest_i + 25, closest_j + 25, outline="white", fill="white")
            w.delete(chance_text)
            chance_text = w.create_text(700, 25, fill="black", font="times 20 bold", text="PLAYER 1's CHANCE")

        is_player_winner(coords, 1)
        is_player_winner(coords, 2)

    for obj in coords:
        obj.v = 0


w.bind("<Button-1>", click)

mainloop()
