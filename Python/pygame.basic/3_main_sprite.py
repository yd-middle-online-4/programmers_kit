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

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/hallucy/Desktop/Coding/VSC/Python/pygame.basic/LUCID_GAME_Cha_Resize.png")
character_size = character.get_rect().size #이미지의 크기를 구해줌
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화 면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로의 절반 크기에 해당하는 곳에 위치

# 이벤트 루프
running = True # 게임이 진행중인지 확인
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는 지
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생 확인
            running = False #게임 진행중이 아님
    
    screen.blit(background, (0, 0)) #배경 설정
    
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
          
    pygame.display.update() #배경 그리기
# pygame 종료
pygame.quit()