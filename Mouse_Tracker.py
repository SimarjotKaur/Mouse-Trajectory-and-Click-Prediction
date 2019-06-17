from pynput.mouse import Listener
import logging

logging.basicConfig(filename="click_logs_5.txt", level=logging.DEBUG, format="%(asctime)s %(message)s")

def on_move(x,y):
	logging.info("Mouse_moved_to ({0}, {1})".format(x,y))
	
def on_click(x,y,button,pressed):
	logging.info("Mouse_clicked_with_{2}_at ({0}, {1})".format(x,y,button))

def on_scroll(x,y,dx,dy):
	logging.info("Mouse_scrolled_at ({0}, {1}) ({2},{3})".format(x,y,dx,dy))
	#listener.stop()

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
	listener.join()