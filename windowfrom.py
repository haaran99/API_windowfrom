from os import O_SEQUENTIAL, close
from tkinter import *
import tkinter
import os
from json.decoder import JSONDecoder
import requests
import json
from tkinter import messagebox

from requests.models import REDIRECT_STATI

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning) # 경고 지우기

vDCM1 = "https://192.168.123.102:8443/"
vDCM2 = "https://192.168.123.103:8443/"
vDCM3 = "https://192.168.123.104:8443/"
vDCM4 = "https://192.168.123.105:8443/"

if not os.path.exists('C:/utier'): os.makedirs('C:/utier')

#---------------------------------------------------------------------------------------------------------#
# 토큰 장비1번

token_url = vDCM1+"api/authenticate" #토큰 권한 주소

token1 = requests.post(token_url, json={"login": "Administrator","password": "Synamedia12$"}, verify=False) #토큰 받을때 아이디 비밀번호 json 형식으로 입력

token1_jontype = json.loads(token1.text) #제이슨 형식

with open('/utier/token1.json','w') as t: #현재 디렉토리에 w(쓴다.) as f 라는것에
    json.dump(token1_jontype,t)

#---------------------------------------------------------------------------------------------------------#
# 토큰 장비2번

token_url = vDCM2+"api/authenticate" #토큰 권한 주소

token2 = requests.post(token_url, json={"login": "Administrator","password": "Synamedia12$"}, verify=False) #토큰 받을때 아이디 비밀번호 json 형식으로 입력

token2_jontype = json.loads(token2.text) #제이슨 형식

with open('/utier/token2.json','w') as t: #현재 디렉토리에 w(쓴다.) as f 라는것에
    json.dump(token2_jontype,t)

#---------------------------------------------------------------------------------------------------------#
# 토큰 장비3번

token_url = vDCM3+"api/authenticate" #토큰 권한 주소

token3 = requests.post(token_url, json={"login": "Administrator","password": "Synamedia12$"}, verify=False) #토큰 받을때 아이디 비밀번호 json 형식으로 입력

token3_jontype = json.loads(token3.text) #제이슨 형식

with open('/utier/token3.json','w') as t: #현재 디렉토리에 w(쓴다.) as f 라는것에
    json.dump(token3_jontype,t)

#---------------------------------------------------------------------------------------------------------#
# 토큰 장비4번

token_url = vDCM4+"api/authenticate" #토큰 권한 주소

token4 = requests.post(token_url, json={"login": "Administrator","password": "Synamedia12$"}, verify=False) #토큰 받을때 아이디 비밀번호 json 형식으로 입력

token4_jontype = json.loads(token4.text) #제이슨 형식

with open('/utier/token4.json','w') as t: #현재 디렉토리에 w(쓴다.) as f 라는것에
    json.dump(token4_jontype,t)

#---------------------------------------------------------------------------------------------------------#
# 트렌스코더 1번 정보 파싱
transcoder_url = vDCM1+"api/v2/LinearTranscodeServices/"

header1 = {'Authorization': token1_jontype['token']}

transcoder1 = requests.get(transcoder_url, headers=header1, verify=False)

transcoder1_list_jontype = json.loads(transcoder1.text)

with open('/utier/transcoder1_get.json','w') as q: #현재 디렉토리에 w(쓴다.) as b 라는것에
    json.dump(transcoder1_list_jontype,q)

#-----------------------------------------------------------------------------------------#    
# 트렌스코더 2번 정보 파싱
transcoder_url = vDCM2+"api/v2/LinearTranscodeServices/"

header2 = {'Authorization': token2_jontype['token']}

transcoder2 = requests.get(transcoder_url, headers=header2, verify=False)

transcoder2_list_jontype = json.loads(transcoder2.text)

with open('/utier/transcoder2_get.json','w') as q: #현재 디렉토리에 w(쓴다.) as b 라는것에
    json.dump(transcoder2_list_jontype,q)

#---------------------------------------------------------------------------------------------------------#
# 트렌스코더 3번 정보 파싱
transcoder_url = vDCM3+"api/v2/LinearTranscodeServices/"

header3 = {'Authorization': token3_jontype['token']}

transcoder3 = requests.get(transcoder_url, headers=header3, verify=False)

transcoder3_list_jontype = json.loads(transcoder3.text)

with open('/utier/transcoder3_get.json','w') as q: #현재 디렉토리에 w(쓴다.) as b 라는것에
    json.dump(transcoder3_list_jontype,q)

#---------------------------------------------------------------------------------------------------------#
# 트렌스코더 4번 정보 파싱
transcoder_url = vDCM4+"api/v2/LinearTranscodeServices/"

header4 = {'Authorization': token4_jontype['token']}

transcoder4 = requests.get(transcoder_url, headers=header4, verify=False)

transcoder4_list_jontype = json.loads(transcoder4.text)

with open('/utier/transcoder4_get.json','w') as q: #현재 디렉토리에 w(쓴다.) as b 라는것에
    json.dump(transcoder4_list_jontype,q)

#####################################################################################################################
#1 번장비 채널 리스트 불러오기

chanel_count_1 = transcoder1_list_jontype['count']
chanel_list_1 = []

i=0
while i < chanel_count_1:
    ch = (transcoder1_list_jontype['LinearTranscodeServices'][i]['processing']['serviceSettings']['userName'])
    chanel_list_1.append(ch)
    i += 1

###########################################################################################################
#1 번장비 ID 리스트 불러오기

chanel_id_list_1 = []

i=0
while i < chanel_count_1:
    ch_id = (transcoder1_list_jontype['LinearTranscodeServices'][i]['id'])
    chanel_id_list_1.append(ch_id)
    i += 1

#####################################################################################################################
#2 번장비 채널 리스트 불러오기

chanel_count_2 = transcoder2_list_jontype['count']
chanel_list_2 = []

i=0
while i < chanel_count_2:
    ch = (transcoder2_list_jontype['LinearTranscodeServices'][i]['processing']['serviceSettings']['userName'])
    chanel_list_2.append(ch)
    i += 1

###########################################################################################################
#2 번장비 ID 리스트 불러오기

chanel_id_list_2 = []

i=0
while i < chanel_count_2:
    ch_id = (transcoder2_list_jontype['LinearTranscodeServices'][i]['id'])
    chanel_id_list_2.append(ch_id)
    i += 1

#####################################################################################################################
#3 번장비 채널 리스트 불러오기

chanel_count_3 = transcoder3_list_jontype['count']
chanel_list_3 = []

i=0
while i < chanel_count_3:
    ch = (transcoder3_list_jontype['LinearTranscodeServices'][i]['processing']['serviceSettings']['userName'])
    chanel_list_3.append(ch)
    i += 1

#####################################################################################################################
#3 번장비 ID 리스트 불러오기

chanel_id_list_3 = []

i=0
while i < chanel_count_3:
    ch_id = (transcoder3_list_jontype['LinearTranscodeServices'][i]['id'])
    chanel_id_list_3.append(ch_id)
    i += 1

#####################################################################################################################
#4 번장비 채널 리스트 불러오기

chanel_count_4 = transcoder4_list_jontype['count']
chanel_list_4 = []

i=0
while i < chanel_count_4:
    ch = (transcoder4_list_jontype['LinearTranscodeServices'][i]['processing']['serviceSettings']['userName'])
    chanel_list_4.append(ch)
    i += 1

#####################################################################################################################
#4 번장비 ID 리스트 불러오기

chanel_id_list_4 = []

i=0
while i < chanel_count_4:
    ch_id = (transcoder4_list_jontype['LinearTranscodeServices'][i]['id'])
    chanel_id_list_4.append(ch_id)
    i += 1

############################################################################################################
# 트렌스코더 채널 이름 ID 정렬
dictionary1 = dict(zip(chanel_list_1, chanel_id_list_1)) # list 2개를 {채널이름list1 : 채널서비스번호list1}
dictionary1 =sorted(dictionary1.items()) # 채널이름으로 정렬 앞에가 items 뒤에가 keys

dictionary2 = dict(zip(chanel_list_2, chanel_id_list_2)) # list 2개를 {채널이름list1 : 채널서비스번호list1}
dictionary2 =sorted(dictionary2.items()) # 채널이름으로 정렬 앞에가 items 뒤에가 keys

dictionary3 = dict(zip(chanel_list_3, chanel_id_list_3)) # list 2개를 {채널이름list1 : 채널서비스번호list1}
dictionary3 =sorted(dictionary3.items()) # 채널이름으로 정렬 앞에가 items 뒤에가 keys

dictionary4 = dict(zip(chanel_list_4, chanel_id_list_4)) # list 2개를 {채널이름list1 : 채널서비스번호list1}
dictionary4 =sorted(dictionary4.items()) # 채널이름으로 정렬 앞에가 items 뒤에가 keys

chanel_list_1_type_list = list(dictionary1) # 정렬한 dict -> list로
chanel_list_2_type_list = list(dictionary2) # 정렬한 dict -> list로
chanel_list_3_type_list = list(dictionary3) # 정렬한 dict -> list로
chanel_list_4_type_list = list(dictionary4) # 정렬한 dict -> list로

# serivce 저장

for i in range(len(chanel_id_list_1)):
    chanel_id_list_1[i] = (chanel_list_1_type_list[i][1]) # chanel_id_list_1 재배열  
    chanel_list_1[i] = (chanel_list_1_type_list[i][0]) # chanel_list_1 재배열 

for i in range(len(chanel_id_list_2)):
    chanel_id_list_2[i] = (chanel_list_2_type_list[i][1]) # chanel_id_list_4 배열 선공 
    chanel_list_2[i] = (chanel_list_2_type_list[i][0]) # chanel_list_4 배열 선공 

for i in range(len(chanel_id_list_3)):
    chanel_id_list_3[i] = (chanel_list_3_type_list[i][1]) # chanel_id_list_1 배열 선공 
    chanel_list_3[i] = (chanel_list_3_type_list[i][0])    

for i in range(len(chanel_id_list_4)):
    chanel_id_list_4[i] = (chanel_list_4_type_list[i][1]) # chanel_id_list_1 배열 선공 
    chanel_list_4[i] = (chanel_list_4_type_list[i][0])


########################################################################################################################
## UI 시작

root = Tk()

root.title("Emergency transmission")
root.geometry("900x850+170+100")
root.resizable(False, False)

label = Label(root, text='Skylife 비상방송 송출', font=("돋음", 25), pady= 25)
label.place(x=190 , y=90)
#datas = [('utier.ico', './img')]
#root.iconbitmap(datas) # 창 왼쪽맨위 아이콘
label.pack()

#photo = PhotoImage(file="./image/icon.png")
#btn = Button(root, image=photo)
#btn.place(x=1300, y=20, width=40, height=40)


#################################################################################################
# 장비 GUI 이름 표기

device_label1 = tkinter.Label(root, text="Transcoder1\nMain",font=("돋음", 18),borderwidth=4)
device_label1.place(x=240 , y=110)
device_label3 = tkinter.Label(root, text="Transcode2\nMain",font=("돋음", 18),borderwidth=4)
device_label3.place(x=490 , y=110)


#################################################################################################
# 장비 GUI 이름 표기 테두리

#canvas=tkinter.Canvas(root, relief = FLAT, bd=2)
#line = canvas.create_rectangle(0,0,200,800)  #X1,Y1 X2,Y2, window x1 y1 위치
#canvas.pack()



#################################################################################################
# 비상방송 선택 리스트업 

em_CheckVariety_1=tkinter.IntVar()
em_CheckVariety_2=tkinter.IntVar()
em_CheckVariety_3=tkinter.IntVar()
em_CheckVariety_4=tkinter.IntVar()

em_check1=tkinter.Checkbutton(root, text="비상방송1", variable=em_CheckVariety_1, font="굴림 12") 
em_check2=tkinter.Checkbutton(root, text="비상방송2", variable=em_CheckVariety_2, font="굴림 12")
em_check3=tkinter.Checkbutton(root, text="비상방송3", variable=em_CheckVariety_3, font="굴림 12")
em_check4=tkinter.Checkbutton(root, text="비상방송4", variable=em_CheckVariety_4, font="굴림 12")

em_check1.place(x=80, y=350)
em_check2.place(x=80, y=400)
em_check3.place(x=80, y=450)
em_check4.place(x=80, y=500)

#################################################################################################
# 1 번 장비 채널 리스트업 

while chanel_count_1 < 12:
    chanel_count_1 += 1
    chanel_list_1.append(" ")

chanel1_Variety_1=tkinter.IntVar()
chanel1_Variety_2=tkinter.IntVar()
chanel1_Variety_3=tkinter.IntVar()
chanel1_Variety_4=tkinter.IntVar()
chanel1_Variety_5=tkinter.IntVar()
chanel1_Variety_6=tkinter.IntVar()
chanel1_Variety_7=tkinter.IntVar()
chanel1_Variety_8=tkinter.IntVar()
chanel1_Variety_9=tkinter.IntVar()
chanel1_Variety_10=tkinter.IntVar()
chanel1_Variety_11=tkinter.IntVar()
chanel1_Variety_12=tkinter.IntVar()

em_check1_1=tkinter.Checkbutton(root, text=chanel_list_1[0], variable=chanel1_Variety_1, font="굴림 12") 
em_check1_2=tkinter.Checkbutton(root, text=chanel_list_1[1], variable=chanel1_Variety_2, font="굴림 12")
em_check1_3=tkinter.Checkbutton(root, text=chanel_list_1[2], variable=chanel1_Variety_3, font="굴림 12")
em_check1_4=tkinter.Checkbutton(root, text=chanel_list_1[3], variable=chanel1_Variety_4, font="굴림 12")
check1_5=tkinter.Checkbutton(root, text=chanel_list_1[4], variable=chanel1_Variety_5, font="굴림 12")
check1_6=tkinter.Checkbutton(root, text=chanel_list_1[5], variable=chanel1_Variety_6, font="굴림 12")
check1_7=tkinter.Checkbutton(root, text=chanel_list_1[6], variable=chanel1_Variety_7, font="굴림 12")
check1_8=tkinter.Checkbutton(root, text=chanel_list_1[7], variable=chanel1_Variety_8, font="굴림 12")
check1_9=tkinter.Checkbutton(root, text=chanel_list_1[8], variable=chanel1_Variety_9, font="굴림 12")
check1_10=tkinter.Checkbutton(root, text=chanel_list_1[9], variable=chanel1_Variety_10, font="굴림 12")
check1_11=tkinter.Checkbutton(root, text=chanel_list_1[10], variable=chanel1_Variety_11, font="굴림 12")
check1_12=tkinter.Checkbutton(root, text=chanel_list_1[11], variable=chanel1_Variety_12, font="굴림 12")
em_check1_1.place(x=250, y=200)
em_check1_2.place(x=250, y=250)
em_check1_3.place(x=250, y=300)
em_check1_4.place(x=250, y=350)
check1_5.place(x=250, y=400)
check1_6.place(x=250, y=450)
check1_7.place(x=250, y=500)
check1_8.place(x=250, y=550)
check1_9.place(x=250, y=600)
check1_10.place(x=250, y=650)
check1_11.place(x=250, y=700)
check1_12.place(x=250, y=750)

#################################################################################################
# 3 번 장비 채널 리스트업 

while chanel_count_3 < 12:
    chanel_count_3 += 1
    chanel_list_3.append(" ")

chanel3_Variety_1=tkinter.IntVar()
chanel3_Variety_2=tkinter.IntVar()
chanel3_Variety_3=tkinter.IntVar()
chanel3_Variety_4=tkinter.IntVar()
chanel3_Variety_5=tkinter.IntVar()
chanel3_Variety_6=tkinter.IntVar()
chanel3_Variety_7=tkinter.IntVar()
chanel3_Variety_8=tkinter.IntVar()
chanel3_Variety_9=tkinter.IntVar()
chanel3_Variety_10=tkinter.IntVar()
chanel3_Variety_11=tkinter.IntVar()
chanel3_Variety_12=tkinter.IntVar()

check3_1=tkinter.Checkbutton(root, text=chanel_list_3[0], variable=chanel3_Variety_1, font="굴림 12") 
check3_2=tkinter.Checkbutton(root, text=chanel_list_3[1], variable=chanel3_Variety_2, font="굴림 12")
check3_3=tkinter.Checkbutton(root, text=chanel_list_3[2], variable=chanel3_Variety_3, font="굴림 12")
check3_4=tkinter.Checkbutton(root, text=chanel_list_3[3], variable=chanel3_Variety_4, font="굴림 12")
check3_5=tkinter.Checkbutton(root, text=chanel_list_3[4], variable=chanel3_Variety_5, font="굴림 12")
check3_6=tkinter.Checkbutton(root, text=chanel_list_3[5], variable=chanel3_Variety_6, font="굴림 12")
check3_7=tkinter.Checkbutton(root, text=chanel_list_3[6], variable=chanel3_Variety_7, font="굴림 12")
check3_8=tkinter.Checkbutton(root, text=chanel_list_3[7], variable=chanel3_Variety_8, font="굴림 12")
check3_9=tkinter.Checkbutton(root, text=chanel_list_3[8], variable=chanel3_Variety_9, font="굴림 12")
check3_10=tkinter.Checkbutton(root, text=chanel_list_3[9], variable=chanel3_Variety_10, font="굴림 12")
check3_11=tkinter.Checkbutton(root, text=chanel_list_3[10], variable=chanel3_Variety_11, font="굴림 12")
check3_12=tkinter.Checkbutton(root, text=chanel_list_3[11], variable=chanel3_Variety_12, font="굴림 12")

check3_1.place(x=500, y=200)
check3_2.place(x=500, y=250)
check3_3.place(x=500, y=300)
check3_4.place(x=500, y=350)
check3_5.place(x=500, y=400)
check3_6.place(x=500, y=450)
check3_7.place(x=500, y=500)
check3_8.place(x=500, y=550)
check3_9.place(x=500, y=600)
check3_10.place(x=500, y=650)
check3_11.place(x=500, y=700)
check3_12.place(x=500, y=750)

em_status = []    
chanel1_status = []    
chanel2_status = []
chanel3_status = []  
chanel4_status = []   


##################################################################################################
# 지속시간(초)

duration_label = tkinter.Label(root, text="지속시간(초)", font="굴림 11")
duration_label.place(x=85, y=550)

duration_input = tkinter.Entry(root, width=15, borderwidth=3)
duration_input.insert(0, "150")
duration_input.place(x=80, y=570)

#################################################################################################
#비상방송 송출 버튼
banner_puts_stus=['','','','']

def push():
    
    
    #EM list
    em_list = ['em1','em2','em3','em4']
    


    chanel1_status.clear()
    chanel2_status.clear()
    chanel3_status.clear()
    chanel4_status.clear()
    
    em_status.append(em_CheckVariety_1.get())
    em_status.append(em_CheckVariety_2.get())
    em_status.append(em_CheckVariety_3.get())
    em_status.append(em_CheckVariety_4.get())
    
    chanel1_status.append(chanel1_Variety_1.get())
    chanel1_status.append(chanel1_Variety_2.get())
    chanel1_status.append(chanel1_Variety_3.get())
    chanel1_status.append(chanel1_Variety_4.get())
    chanel1_status.append(chanel1_Variety_5.get())
    chanel1_status.append(chanel1_Variety_6.get())
    chanel1_status.append(chanel1_Variety_7.get())
    chanel1_status.append(chanel1_Variety_8.get())
    chanel1_status.append(chanel1_Variety_9.get())
    chanel1_status.append(chanel1_Variety_10.get())
    chanel1_status.append(chanel1_Variety_11.get())
    chanel1_status.append(chanel1_Variety_12.get())

    chanel3_status.append(chanel3_Variety_1.get())
    chanel3_status.append(chanel3_Variety_2.get())
    chanel3_status.append(chanel3_Variety_3.get())
    chanel3_status.append(chanel3_Variety_4.get())
    chanel3_status.append(chanel3_Variety_5.get())
    chanel3_status.append(chanel3_Variety_6.get())
    chanel3_status.append(chanel3_Variety_7.get())
    chanel3_status.append(chanel3_Variety_8.get())
    chanel3_status.append(chanel3_Variety_9.get())
    chanel3_status.append(chanel3_Variety_10.get())
    chanel3_status.append(chanel3_Variety_11.get())
    chanel3_status.append(chanel3_Variety_12.get())


    ###############################################################################################################################################################
    # 지속시간 얻기
    duration = duration_input.get()

    if duration == "":
        messagebox.showinfo("경고","지속시간을 넣어 주세요.")

    duration = int(duration_input.get())
    
    #예외처리
    
    if duration < 15 :
        messagebox.showinfo("경고","지속시간 14초 이하 설정 금지")


    ###############################################################################################################################################################
    # 비상방송 몇번 선택했는지
    em_pick = "null"
    k=0
    for i in em_status:  
        k += 1
        if i == 1:
            em_list[k-1]
            em_pick = em_list[k-1]
            em_list.clear()
            em_status.clear()            
            
    #배열초기화
    ###############################################################################################################################################################
    # 비상방송 몇번 자막 선택
    if em_pick == "null":
        messagebox.showwarning("경고","자막을 선택해주세요")
        em_list.clear()
        em_status.clear()
    
    elif em_pick == "em1":
        payload = {"banners": [{"bannerName": "em1","bannerId": "00000000-0000-0000-0000-000000000000","duration": duration,"infinite": False,"bannerEncoding": "UTF-8","EASAlert": False}]}
    
    elif em_pick == "em2":
        payload = {"banners": [{"bannerName": "em2","bannerId": "00000000-0000-0000-0000-000000000001","duration": duration,"infinite": False,"bannerEncoding": "UTF-8","EASAlert": False}]}
    
    elif em_pick == "em3":
        payload = {"banners": [{"bannerName": "em3","bannerId": "00000000-0000-0000-0000-000000000002","duration": duration,"infinite": False,"bannerEncoding": "UTF-8","EASAlert": False}]}
    
    elif em_pick == "em4":
        payload = {"banners": [{"bannerName": "em4","bannerId": "00000000-0000-0000-0000-000000000003","duration": duration,"infinite": False,"bannerEncoding": "UTF-8","EASAlert": False}]}
    
    ##################################################################################################################################################################
    ## 장비 송출법
    def banner_put1(a):

                token_url = vDCM1+"api/authenticate" #토큰 권한 주소

                token1 = requests.post(token_url, json={"login": "Administrator","password": "Synamedia12$"}, verify=False) #토큰 받을때 아이디 비밀번호 json 형식으로 입력

                token1_jontype = json.loads(token1.text) #제이슨 형식

                with open('/utier/token1.json','w') as t: #현재 디렉토리에 w(쓴다.) as f 라는것에
                    json.dump(token1_jontype,t)

                banner_put_url = vDCM1+"api/v2/LinearTranscodeServices/"+a+"/Banners"
                
                header = {'Authorization': token1_jontype['token']}
                
                banner_puts = requests.put(banner_put_url, headers=header, data=json.dumps(payload), verify=False)

                banner_puts = str(banner_puts)

                

                #if banner_puts == '<Response [202]>':
                #    messagebox.showinfo("1번 장비", chanel_list_1[k] + " 비상방송 송출 성공!!")
                #elif banner_puts == '<Response [409]>':
                #    messagebox.showerror("1번 장비", "1번 장비 송출 실패 ! !")

    def banner_put2(a):

                token_url = vDCM2+"api/authenticate" #토큰 권한 주소

                token2 = requests.post(token_url, json={"login": "Administrator","password": "Synamedia12$"}, verify=False) #토큰 받을때 아이디 비밀번호 json 형식으로 입력

                token2_jontype = json.loads(token2.text) #제이슨 형식

                with open('/utier/token2.json','w') as t: #현재 디렉토리에 w(쓴다.) as f 라는것에
                    json.dump(token2_jontype,t)

                banner_put_url = vDCM2+"api/v2/LinearTranscodeServices/"+a+"/Banners"
                
                header = {'Authorization': token2_jontype['token']}
                
                banner_puts = requests.put(banner_put_url, headers=header, data=json.dumps(payload), verify=False)

                banner_puts = str(banner_puts)

                

                #if banner_puts == '<Response [202]>':
                #    messagebox.showinfo("1번 장비", chanel_list_1[k] + " 비상방송 송출 성공!!")
                #elif banner_puts == '<Response [409]>':
                #    messagebox.showerror("1번 장비", "1번 장비 송출 실패 ! !")

    def banner_put3(a):

                token_url = vDCM3+"api/authenticate" #토큰 권한 주소

                token3 = requests.post(token_url, json={"login": "Administrator","password": "Synamedia12$"}, verify=False) #토큰 받을때 아이디 비밀번호 json 형식으로 입력

                token3_jontype = json.loads(token3.text) #제이슨 형식

                with open('/utier/token3.json','w') as t: #현재 디렉토리에 w(쓴다.) as f 라는것에
                    json.dump(token3_jontype,t)

                banner_put_url = vDCM3+"api/v2/LinearTranscodeServices/"+a+"/Banners"
                
                header = {'Authorization': token3_jontype['token']}
                
                banner_puts = requests.put(banner_put_url, headers=header, data=json.dumps(payload), verify=False)

                banner_puts = str(banner_puts)

                

                #if banner_puts == '<Response [202]>':
                #    messagebox.showinfo("1번 장비", chanel_list_1[k] + " 비상방송 송출 성공!!")
                #elif banner_puts == '<Response [409]>':
                #    messagebox.showerror("1번 장비", "1번 장비 송출 실패 ! !")

    def banner_put4(a):

                token_url = vDCM4+"api/authenticate" #토큰 권한 주소

                token4 = requests.post(token_url, json={"login": "Administrator","password": "Synamedia12$"}, verify=False) #토큰 받을때 아이디 비밀번호 json 형식으로 입력

                token4_jontype = json.loads(token4.text) #제이슨 형식

                with open('/utier/token4.json','w') as t: #현재 디렉토리에 w(쓴다.) as f 라는것에
                    json.dump(token4_jontype,t)

                banner_put_url = vDCM4+"api/v2/LinearTranscodeServices/"+a+"/Banners"
                
                header = {'Authorization': token4_jontype['token']}
                
                banner_puts = requests.put(banner_put_url, headers=header, data=json.dumps(payload), verify=False)

                banner_puts = str(banner_puts)

                

                #if banner_puts == '<Response [202]>':
                #    messagebox.showinfo("1번 장비", chanel_list_1[k] + " 비상방송 송출 성공!!")
                #elif banner_puts == '<Response [409]>':
                #    messagebox.showerror("1번 장비", "1번 장비 송출 실패 ! !")

    ##################################################################################################################################################################
    ## 1 2번 장비 송출 조건

    k=0

    for i in chanel1_status:
        k += 1

        if i == 1:
            k -= 1
            banner_put1(chanel_id_list_1[k])
            banner_put2(chanel_id_list_2[k])
            k += 1
 
    ##################################################################################################################################################################
    ## 3 4번 장비 송출 조건

    k=0

    for i in chanel3_status:
        k += 1

        if i == 1:
            k -= 1
            banner_put3(chanel_id_list_3[k])
            banner_put4(chanel_id_list_4[k])
            k += 1
 

button = tkinter.Button(root, text='방송 송출', font="굴림 20", command=push, bd=10)
button.place(x=720, y=200, width=150, height=500)



root.mainloop()