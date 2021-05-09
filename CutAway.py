import pygame

pygame.init()
######################################################################
Screen_Width = 1280
Screen_Height = 720
Screen = pygame.display.set_mode((Screen_Width, Screen_Height))
    
# 화면 타이틀 설정
pygame.display.set_caption("방구석 트레이너") # 게임 이름
######################################################################
# FPS
Clock = pygame.time.Clock()
######################################################################
# 배경 이미지 불러오기
Background_Delay = 3000
Background_Time = 0
list_Background = ["Rhythm/ScreenBlue.png", "Rhythm/ScreenGreen.png", "Rhythm/ScreenOrange.png", "Rhythm/ScreenPink.png", "Rhythm/ScreenPurple.png", "Rhythm/ScreenSkyblue.png", "Rhythm/ScreenYellow.png"]
Background_Index = 0

CutAway_Delay = 1500
CutAway_Time = 0
######################################################################
# 시간 계산
Start_Ticks = pygame.time.get_ticks()
######################################################################
Timer_Font = pygame.font.Font("Rhythm/CookieRun Bold.ttf", 50) # 폰트 객체 생성(폰트, 크기)
######################################################################
queue1 = []
OpacityLevel = 255

Crashed = False
######################################################################
pygame.time.delay(1000)

while not Crashed: 
    dt = Clock.tick(30)
    Elapsed_Time = (pygame.time.get_ticks() - Start_Ticks) / 1000
    Screen.fill((255, 255, 255))
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            pygame.quit()
        if event.type == pygame.KEYDOWN: # 키가 눌렸는지 확인
            if event.key == pygame.K_UP: # 위쪽 방향키
                for temp, tempRect in queue1:
                    if tempRect.left >= (1280 / 2) - 100:
                        pass
   
######################################################################                        
    # 타이머 설정

    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시
    Elapsed_Time = (pygame.time.get_ticks() - Start_Ticks) / 1000
    
    
    # 지나간 시간을 분과 초로 분해
    Minutes = int(Elapsed_Time / 60)
    Seconds = int(Elapsed_Time % 60)
    
    
    if Seconds < 10:
        TimerCase = ":0"
    else:
        TimerCase = ":"
    timer = Timer_Font.render(str(Minutes) + TimerCase + str(Seconds), True, (255, 255, 255))                     
######################################################################
    # 배경화면 설정
    
    # 화면 색깔 변환
    Now_Time = pygame.time.get_ticks()
    
    if (Now_Time > Background_Time + Background_Delay):
        Background_Time = Now_Time
        Background_Index += 1
        if (Background_Index >= len(list_Background)):
            Background_Index = 0     
        
    Background = pygame.image.load(list_Background[Background_Index])
######################################################################
    Screen.blit(Background, (0, 0)) 
    Screen.blit(timer, (10, 20))
######################################################################         
 
######################################################################
    pygame.display.update()
    
pygame.time.delay(5000)
pygame.quit()
            