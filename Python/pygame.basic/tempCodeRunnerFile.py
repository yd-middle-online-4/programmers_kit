    #충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    #충돌 체크
    if character_rect.collidedict(enemy_dict):
        print("충돌했어요.")
        running = False