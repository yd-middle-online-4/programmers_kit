import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("LUCID GAME") # 게임 이름

#배경 이미지 불러오기
background = pygame.image.load("/Users/hallucy/Desktop/Coding/VSC/Python/pygame.basic/LUCID_GAME_BG.jpg")

# 이벤트 루프
running = True # 게임이 진행중인지 확인
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는 지
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생 확인
            running = False #게임 진행중이 아님
    
    # screen.fill((0, 0, 255)) # 배경 채우기
    screen.blit(background, (0, 0)) #배경 설정      
    pygame.display.update() #배경 그리기
# pygame 종료
pygame.quit()