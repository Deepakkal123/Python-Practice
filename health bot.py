
import pygame
import datetime
import time
def myfile(file, stop):

    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


    # clock = pygame.time.Clock()
    # while pygame.mixer.music.get_busy():
    #     print("Playing...")
    #     clock.tick(-1)
    while True:
        input_of_user = input()
        if input_of_user == stop:
            pygame.mixer.music.stop()
            break


timeforwater = time.time()
print("1 ---",time.time())
timeforeyes = time.time()
print("2 ---",time.time())
water = 5
eyes = 10

while True:
    if time.time() - timeforwater > water:
        print("3 ---",time.time())
        print("Its time to drink water : kindly type'drank' for the alarm to stop. ")
        myfile('Alan.mp3', 'drank')
        print("4 ---",time.time())
        timeforwater= time.time()
        print("5 ---",time.time())

    if time.time() - timeforeyes > eyes:
        print("Its time to rotate your eyes : kindly type'done' for the alarm to stop. ")
        myfile('Groove.ogg', 'done')
        timeforeyes= time.time()



