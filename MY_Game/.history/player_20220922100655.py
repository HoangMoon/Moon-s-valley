import pygame
from settings import*
from support import*
from Time import Timer


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites):
        super().__init__(group)

        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0

        # self.image = pygame.Surface((32, 64))
        # self.image.fill('green')
        # self.rect = self.image.get_rect(center = pos)

	# general setup
        # self.image = self.animations[self.status][self.frame_index]

        # self.rect = self.image.get_rect(center = pos)
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYER['main']

    #movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200


    #collision
        self.hitbox = self.rect.copy().inflate((-126,-70))
        self.collision_sprites = collision_sprites
    #timers
        self.timers = {
            'tool use': Timer(350, self.use_tool),
            'tool switch':Timer(200),
            'seed use': Timer(350, self.use_seed),
            'seed switch':Timer(200)
            
        }

    #tool use
        self.tools = ['hoe', 'axe', 'water']
        self.tool_index = 0
        self.selected_tool = 'water'
    #seed
        self.seeds = ['corn', 'tomato']
        self.seed_index = 0
        self.selected_seed = self.seeds[self.seed_index]
    def use_tool(self):
        # print(self.selected_tool)
        pass

    def use_seed(self):
        pass

    def import_assets(self):
        self.animations = {'up': [],'down': [],'left': [],'right': [],
						   'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
						   'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
						   'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
						   'right_water':[],'left_water':[],'up_water':[],'down_water':[]}

        for animation in self.animations.keys():
            full_path = './graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)
        # print(self.animations)

# làm animate
    def animate(self,dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.timers['tool use'].active:
        #directions
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status= 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status= 'down'
            else:
                self.direction.y = 0
        
            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status= 'left'
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status= 'right'
            else:
                self.direction.x = 0

        #tools use
        if keys[pygame.K_SPACE]:
                #time for tool use
            self.timers['tool use'].activate()
            self.direction = pygame.math.Vector2()
            self.frame_index = 0
 
        # change tool
        if keys[pygame.K_q] and not self.timers['tool switch'].active:
            self.timers['tool switch'].activate()
            self.tool_index += 1
            # print(self.tool_index)
            # if tool index > length of tool => tool index = 0
            self.tool_index = self.tool_index if self.tool_index < len(self.tools) else 0
            self.selected_tool = self.tools[self.tool_index]


        # seed use
        if keys[pygame.K_LCTRL]:
                #time for tool use
            self.timers['seed use'].activate()
            self.direction = pygame.math.Vector2()
            self.frame_index = 0
            # print('use seed')
        #change seed use
        if keys[pygame.K_e] and not self.timers['seed switch'].active:
            self.timers['seed switch'].activate()
            self.seed_index += 1
            # print(self.seed_index)
            # if seed index > length of seed => seed index = 0
            self.seed_index = self.seed_index if self.seed_index < len(self.seeds) else 0
            self.selected_seed = self.seeds[self.seed_index]
            # print(self.selected_seed)
    def get_status(self):
        # nếu player ko di chuyển :
        # add _idle vào status

        #idle
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'
        
        #tool use
        if self.timers['tool use'].active:

            self.status = self.status.split('_')[0] + '_' + self.selected_tool

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    # def collision(self,direction):
    #     for sprite in self.collision_sprites.sprites():
    #         if hasattr(sprite, 'hitbox'):
    #             if sprite.hitbox.colliderect(self.hitbox):
    #                 if direction == 'horizontal':
    #                     if self.direction.x > 0 :#moving right
    #                         self.hitbox.right = sprite.hitbox.left
    #                     if self.direction.x < 0 :#moving left
    #                         self.hitbox.left = sprite.hitbox.right
    #                     self.rect.centerx = self.hitbox.centerx
    #                     self.pos.x = self.hitbox.centerx

    def move(self, dt):


        #normalizing a vector
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        # print(self.direction)

        #horizontal movement
        self.pos.x += self.direction.x *self.speed *dt
        # tạo hộp quanh player
        self.hitbox.centerx = round(self.pos.x) 
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')
        #vertical movement
        self.pos.y += self.direction.y *self.speed *dt
        # tạo hộp quanh player
        self.hitbox.centerx = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision('horizontal')
    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.move(dt)
        self.animate(dt)


