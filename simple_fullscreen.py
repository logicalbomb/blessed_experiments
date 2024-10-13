import blessed

term = blessed.Terminal()

PIXEL_WIDTH = 64
PIXEL_HEIGHT = 32
PIXEL_STRING = u'\u2830\u2806'
#PIXEL_STRING = u'\u28FF\u28FF'

pixel_colors = [['' for _ in range(PIXEL_WIDTH)] for _ in range(PIXEL_HEIGHT)]

def print_screen():
    #TODO: Pull out styles into something more manageable
    print(f'{term.home}{term.on_black}{term.clear}', end='')
    print(f'{term.color(75, 185, 22)}', end='')
    y = 0
    while y < len(pixel_colors):
        x = 0
        while x < len(pixel_colors[y]):
            if (y == 15 and x == 31) or (y == 15 and x == 32) or (y == 16 and x == 31) or (y == 16 and x == 32):
                print(f'{term.color(130, 205, 230)}', end='') 
            elif (y == 15 and x == 33) or (y == 16 and x == 33):
                print(f'{term.color(75, 185, 22)}', end='')
            print(PIXEL_STRING, end='')
            x += 1
        print()
        y += 1

with term.fullscreen():
    print_screen()

    with term.cbreak():
        val = ''
        while val.lower() != 'q':
            val = term.inkey(timeout=3)
            if not val:
                pass
            elif val.is_sequence and val.code == 260:
                print_screen()
                print('Left')
            elif val.is_sequence and val.code == 261:
                print_screen()
                print('Right')
            elif val.is_sequence:
                print_screen()
                print('Sequence: {0}'.format((str(val), val.name, val.code)))
            elif val == ' ':
                print_screen()
                print('Space')
            elif val:
                print_screen()
                print(val)
    
        print('No longer looking for keyboard')

    print('Leaving fullscreen')
    
print('The end')
    
