import pygame

# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()
##########################################################################################
# 화면 크기 설정
Screen_Width = 1280  # 가로 크기
Screen_Height = 720  # 세로 크기
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
##########################################################################################
# 화면 타이틀 설정
pygame.display.set_caption("방구석 트레이너")  # 게임 
##########################################################################################
# FPS
Clock = pygame.time.Clock()
##########################################################################################
# 이미지 설정

# 배경화면 불러오기

# 배경 왼/오른쪽/가운데 이미지 불러오기
Background_Middle = pygame.image.load("Rhythm/Screen/Smartphone.png").convert_alpha()
Background_Middle = pygame.transform.scale(Background_Middle, (545, 808))

Background_Left = pygame.image.load("Rhythm/Screen/SmartphoneLeftScreen.png").convert_alpha()
Background_Left = pygame.transform.scale(Background_Left, (405, 607))

Background_Right = pygame.image.load("Rhythm/Screen/SmartphoneRightScreen.png").convert_alpha()
Background_Right = pygame.transform.scale(Background_Right, (410, 607))



# 도전과제 이미지 불러오기 

# 시작이 반이다
# 첫 곡을 끝마침
achievement1 = pygame.image.load("Rhythm/achievement/achievement1.png")

achievement1_Size = achievement1.get_rect().size # 이미지의 사이즈
achievement1_Width = achievement1_Size[0] # 이미지의 너비
achievement1_Height = achievement1_Size[1] # 이미지의 높이
achievement1 = pygame.transform.scale(achievement1, (int(achievement1_Width / 1.5), int(achievement1_Height / 1.5)))

achievement1_x_pos = 871
achievement1_y_pos = 100

# 의지박약
# 정확도 0%로 게임을 끝마침
achievement2 = pygame.image.load("Rhythm/achievement/achievement2.png")
achievement2_Size = achievement2.get_rect().size # 이미지의 사이즈
achievement2_Width = achievement2_Size[0] # 이미지의 너비
achievement2_Height = achievement2_Size[1] # 이미지의 높이
achievement2 = pygame.transform.scale(achievement2, (400, 600))

achievement2_x_pos = 871
achievement2_y_pos = 100


# 리듬천재
# 정확도 100%로 게임을 끝마침
achievement3 = pygame.image.load("Rhythm/achievement/achievement3.png")
achievement3_Size = achievement3.get_rect().size # 이미지의 사이즈
achievement3_Width = achievement3_Size[0] # 이미지의 너비
achievement3_Height = achievement3_Size[1] # 이미지의 높이
achievement3 = pygame.transform.scale(achievement3, (482, 600))

achievement3_x_pos = 871
achievement3_y_pos = 100

# 단 한 곡
# 한 곡을 50번 플레이함
achievement4 = pygame.image.load("Rhythm/achievement/achievement4.png")
achievement4_Size = achievement4.get_rect().size # 이미지의 사이즈
achievement4_Width = achievement4_Size[0] # 이미지의 너비
achievement4_Height = achievement4_Size[1] # 이미지의 높이
achievement4 = pygame.transform.scale(achievement4, (463, 600))

achievement4_x_pos = 871
achievement4_y_pos = 100

# 에어로빅 강사
# 게임을 50번 이상 플레이함
achievement5 = pygame.image.load("Rhythm/achievement/achievement5.png")
achievement5_Size = achievement5.get_rect().size # 이미지의 사이즈
achievement5_Width = achievement5_Size[0] # 이미지의 너비
achievement5_Height = achievement5_Size[1] # 이미지의 높이
achievement5 = pygame.transform.scale(achievement5, (495, 600))

achievement5_x_pos = 871
achievement5_y_pos = 100

# 3대 500
# 게임을 500번 이상 플레이함
achievement6 = pygame.image.load("Rhythm/achievement/achievement6.png")
achievement6_Size = achievement6.get_rect().size # 이미지의 사이즈
achievement6_Width = achievement6_Size[0] # 이미지의 너비
achievement6_Height = achievement6_Size[1] # 이미지의 높이
achievement6 = pygame.transform.scale(achievement6, (472, 600))

achievement6_x_pos = 871
achievement6_y_pos = 100

# 헬창
# 1년 동안 하루도 빠짐없이 게임에 접속함
achievement7 = pygame.image.load("Rhythm/achievement/achievement7.png")
achievement7_Size = achievement7.get_rect().size # 이미지의 사이즈
achievement7_Width = achievement7_Size[0] # 이미지의 너비
achievement7_Height = achievement7_Size[1] # 이미지의 높이
achievement7 = pygame.transform.scale(achievement7, (443, 600))

achievement7_x_pos = 871
achievement7_y_pos = 100




list_Achievement = [[achievement1, achievement1_Width, achievement1_x_pos], 
                    [achievement2, achievement2_Width, achievement2_x_pos],
                    [achievement3, achievement3_Width, achievement3_x_pos],
                    [achievement4, achievement4_Width, achievement4_x_pos],
                    [achievement5, achievement5_Width, achievement5_x_pos],
                    [achievement6, achievement6_Width, achievement6_x_pos],
                    [achievement7, achievement7_Width, achievement7_x_pos]]
##########################################################################################
# 배경 음악 및 효과음 설정

# 룰렛이 돌아가는 효과음
pygame.mixer.music.load("Rhythm/BGM/379240__westington__slot-machine.wav")

# 짜쟌 효과음
Tada = pygame.mixer.Sound("Rhythm/BGM/ジャジャーン.mp3")
##########################################################################################
# 전역 변수 설정

count = 1 # 룰렛 돈 횟수
PlayOn = 0 # 배경음악이 켜져있는 확인하는 척도
a = 0 # 룰렛의 가속도

index = 0 
c_index = 2 # 도전과제 달성 인덱스

Crashed = False
##########################################################################################
while not Crashed:
    dt = Clock.tick(30) # 30fps
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            pygame.quit()
    
    Screen.fill((255, 255, 255))
##########################################################################################
    if count < 4:
        if PlayOn == 0:
            pygame.mixer.music.play(-1)
            PlayOn += 1
        if count == 0:
            if a < 50:
                a += 1
        
        elif count == 1:
            if a < 100:
                a += 1
            
        elif count == 2:
            if a > 50:
                a -= 1
        elif count == 3:
            if a > 25:
                a -= 1
                
        if count < 3: 
            if index <= 6:
                Screen.blit(list_Achievement[index][0], (list_Achievement[index][2], 100))
                
                
                if list_Achievement[index][2] > 403 - list_Achievement[index][1]:
                    list_Achievement[index][2] -= a 
                else:
                    list_Achievement[index][2] = 871
                    index += 1
                    if index == 7:
                        index = 0
                        count += 1
        else:
            if index <= c_index:
                Screen.blit(list_Achievement[index][0], (list_Achievement[index][2], 100))
                
                if index < c_index:
             
                    if list_Achievement[index][2] > 403 - list_Achievement[index][1]:
                        list_Achievement[index][2] -= a 
                    else:
                        index += 1
                else:
                    if list_Achievement[index][2] > 403:
                        list_Achievement[index][2] -= a
                    else:
                        if pygame.mixer.music.get_busy(): #like this!
                            pygame.mixer.music.stop()
                        Tada.play()
                        count += 1
##########################################################################################  
    Screen.blit(list_Achievement[c_index][0], (list_Achievement[c_index][2], 100))
    Screen.blit(Background_Left, (0, 112))
    Screen.blit(Background_Right, (870, 112))
    Screen.blit(Background_Middle, (363, 43)) 
    
    pygame.display.update()
    

pygame.quit()













