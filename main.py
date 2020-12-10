from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

G = [0, 100, 0] # Green
O = [0, 0, 0] # Black
W = [255, 255, 255]  # White
B = [139, 69, 19] # Brown
U = [0, 0, 128] # Blue
R = [255, 0, 0] # Red
Y = [255,255,0] # Yellow

def clear_one_column_from_left(xmas_tree):
  for i in range(8):
    for j in range(7):
      xmas_tree[i*8+j]=xmas_tree[i*8+j+1]
    xmas_tree[i*8+7]=O

def move_image_left(xmas_tree,i):
  return_image=[]
  for line in range(8):
    for j in range(8-i):
      return_image.append(O)
    for j in range(i):
      return_image.append(xmas_tree[line*8+j])

  return return_image

# Adjust to display rotation
sense.set_rotation(180)
while True:
	xmas_tree= [
	O, O, O, G, G, O, O, O,
	O, O, G, G, Y, G, O, O,
	O, G, Y, G, G, G, G, O,
	O, O, G, G, G, G, O, O,
	O, G, G, G, Y, G, G, O,
	G, G, U, G, G, G, G, G,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]

	for i in range(1,9):
	  partial_tree=move_image_left(xmas_tree,i)
	  sense.set_pixels(partial_tree)
	  sleep(.2)

	sleep(2)

	for i in range(8):
	  clear_one_column_from_left(xmas_tree)
	  sense.set_pixels(xmas_tree)
	  sleep(.2)
 
	xmas_tree = [
	O, O, O, U, U, O, O, O,
	O, O, Y, U, U, U, O, O,
	O, U, U, U, U, U, U, O,
	O, O, U, U, Y, U, O, O,
	O, U, U, W, U, U, U, O,
	U, U, U, U, U, U, U, U,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]

	for i in range(1,9):
	  partial_tree=move_image_left(xmas_tree,i)
	  sense.set_pixels(partial_tree)
	  sleep(.2)

	sleep(2)

	for i in range(8):
	  clear_one_column_from_left(xmas_tree)
	  sense.set_pixels(xmas_tree)
	  sleep(.2)

	xmas_tree = [
	O, O, O, W, W, O, O, O,
	O, O, W, W, Y, W, O, O,
	O, W, U, W, W, W, W, O,
	O, O, W, W, W, W, O, O,
	O, W, W, Y, W, W, W, O,
	W, W, W, W, W, U, W, W,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]

	for i in range(1,9):
	  partial_tree=move_image_left(xmas_tree,i)
	  sense.set_pixels(partial_tree)
	  sleep(.2)

	sleep(2)

	for i in range(8):
	  clear_one_column_from_left(xmas_tree)
	  sense.set_pixels(xmas_tree)
	  sleep(.2)

	xmas_tree = [
	O, O, O, R, R, O, O, O,
	O, O, R, U, R, R, O, O,
	O, R, R, R, R, R, R, O,
	O, O, R, R, Y, R, O, O,
	O, R, U, R, R, R, R, O,
	R, R, R, R, Y, R, R, R,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]

	for i in range(1,9):
	  partial_tree=move_image_left(xmas_tree,i)
	  sense.set_pixels(partial_tree)
	  sleep(.2)

	sleep(2)

	for i in range(8):
	  clear_one_column_from_left(xmas_tree)
	  sense.set_pixels(xmas_tree)
	  sleep(.2)
