debug=0
#-------------------------modules-------------------------
import os, pygame
if debug: print(os.cwd())
for i in os.getcwd().split(chr(92)):
    try: a.append(i)
    except: a=[i]
    try:
        if debug: print("/".join(a)+r"PyGameTemplate.py")
        exec(open("/".join(a)+r"PyGameTemplate.py").read())
        break
    except:
        pass
os.system("cls"); print("pygame 2.6.9 (SDL 2.0.22, Python 3.11.5)")

#-----------------------function(s)-----------------------
def main_loop():
    fps=60
    colour_tuple = 55, 55, 55
    while 1:
        screen.fill(colour_tuple)
        test.place()
        test.rescale(1.001)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        pygame.display.flip()
        pygame.time.delay(int(1000/fps))

#--------------------------setup--------------------------
screen = pygame.display.set_mode(display_size)
test=Element(size_tuple=(75, 120))
#------------------------main line------------------------
main_loop()
input("Press Enter to exit the script...")
