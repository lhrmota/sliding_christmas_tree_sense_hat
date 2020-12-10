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


# alternate between two images to make lanterns
# seem to blink
def alternate_between_two_images(image1,image2,interval,numTimes):
  for i in range(1,numTimes):
    sense.set_pixels(image1)
    sleep(interval)
    sense.set_pixels(image2)
    sleep(interval)

def slide_out_while_alternating_two_images(image1,image2,interval):
  for i in range(8):
    clear_one_column_from_left(image1)
    clear_one_column_from_left(image2)
    if i%2==0:
      sense.set_pixels(image1)
    else:
      sense.set_pixels(image2)
    sleep(interval)

def slide_in_while_alternating_two_images(image1,image2,interval):
  for i in range(1,9):
    partial_tree1=move_image_left(image1,i)
    partial_tree2=move_image_left(image2,i)
    if i%2==0:
      sense.set_pixels(partial_tree1)
    else:
      sense.set_pixels(partial_tree2)
    sleep(interval)
    
# Adjust to display rotation
sense.set_rotation(180)
while True:
	xmas_tree_A= [
	O, O, O, G, G, O, O, O,
	O, O, G, G, Y, G, O, O,
	O, G, Y, G, G, G, G, O,
	O, O, G, G, G, G, O, O,
	O, G, G, G, Y, G, G, O,
	G, G, U, G, G, G, G, G,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]

        xmas_tree_B= [
	O, O, O, G, G, O, O, O,
	O, O, G, G, B, G, O, O,
	O, G, G, G, G, G, G, O,
	O, O, G, Y, G, G, O, O,
	O, G, G, G, G, G, G, O,
	G, G, G, G, G, U, G, G,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]

	slide_in_while_alternating_two_images(xmas_tree_A,xmas_tree_B,.1)

	alternate_between_two_images(xmas_tree_A,xmas_tree_B,.1,5)

        slide_out_while_alternating_two_images(xmas_tree_A,xmas_tree_B,.1)
 
	xmas_tree_A = [
	O, O, O, U, U, O, O, O,
	O, O, Y, U, U, U, O, O,
	O, U, U, U, U, U, U, O,
	O, O, U, U, Y, U, O, O,
	O, U, U, W, U, U, U, O,
	U, U, U, U, U, U, U, U,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]

        xmas_tree_B = [
	O, O, O, U, U, O, O, O,
	O, O, U, W, U, U, O, O,
	O, U, U, U, U, W, U, O,
	O, O, U, U, U, U, O, O,
	O, U, Y, U, U, U, U, O,
	U, U, U, U, U, U, U, U,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]

        
	slide_in_while_alternating_two_images(xmas_tree_A,xmas_tree_B,.1)

	alternate_between_two_images(xmas_tree_A,xmas_tree_B,.1,5)

        slide_out_while_alternating_two_images(xmas_tree_A,xmas_tree_B,.1)

	xmas_tree_A = [
	O, O, O, W, W, O, O, O,
	O, O, W, W, Y, W, O, O,
	O, W, U, W, W, W, W, O,
	O, O, W, W, W, W, O, O,
	O, W, W, Y, W, W, W, O,
	W, W, W, W, W, U, W, W,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]

        xmas_tree_B = [
	O, O, O, W, W, O, O, O,
	O, O, W, W, W, W, O, O,
	O, W, W, Y, W, W, W, O,
	O, O, U, W, W, W, O, O,
	O, W, W, W, W, Y, W, O,
	W, W, W, W, W, U, W, W,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]

        
	slide_in_while_alternating_two_images(xmas_tree_A,xmas_tree_B,.1)

	alternate_between_two_images(xmas_tree_A,xmas_tree_B,.1,5)

        slide_out_while_alternating_two_images(xmas_tree_A,xmas_tree_B,.1)

	xmas_tree_A = [
	O, O, O, R, R, O, O, O,
	O, O, R, U, R, R, O, O,
	O, R, R, R, R, R, R, O,
	O, O, R, R, Y, R, O, O,
	O, R, U, R, R, R, R, O,
	R, R, R, R, Y, R, R, R,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]

        xmas_tree_B = [
	O, O, O, R, R, O, O, O,
	O, O, R, R, Y, R, O, O,
	O, R, W, R, R, R, R, O,
	O, O, R, R, R, R, O, O,
	O, R, R, R, R, R, R, O,
	R, R, R, U, R, R, R, R,
	O, O, O, B, B, O, O, O,
	O, O, O, B, B, O, O, O
	]

        
	slide_in_while_alternating_two_images(xmas_tree_A,xmas_tree_B,.1)

	alternate_between_two_images(xmas_tree_A,xmas_tree_B,.1,5)

        slide_out_while_alternating_two_images(xmas_tree_A,xmas_tree_B,.1)
