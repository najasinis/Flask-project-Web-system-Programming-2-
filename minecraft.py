from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

Sky(texture='sky_sunset')

selected_block = 'grass'

block_textures = {
    "grass": load_texture("assets/textures/groundEarth.png"),
    "dirt": load_texture("assets/textures/groundMud.png"),
    "stone": load_texture("assets/textures/wallStone.png"),
    "bedrock": load_texture("assets/textures/sone07.png"),
}

put = Audio("assets/bgm/put_block", autoplay=False)
jump = Audio("assets/bgm/jump", autoplay=False)

class Voxel(Entity):
    def __init__(self, position, block_type):
        super().__init__(
            position=position,
            model='assets/models/block_model.obj',
            origin_y=0.5,
            texture=block_textures.get(block_type),
            scale=1.0,
            collider='box'
        )
        self.block_type = block_type

hand = Entity(
    parent=camera,
    model='assets/models/block_model.obj',
    scale=0.2,
    texture=block_textures.get(selected_block),
    position=(0.35, -0.25, 0.5),
    rotation=(-15, -30, -5)
)

def input(key):
    global selected_block

    if key == 'space':
        jump.play()
    
    if key == 'left mouse down':
        put.play()
        hit_info = raycast(camera.world_position, camera.forward, distance=10)  # 괄호 제거

        if hit_info.entity:  # hit_info.entity로 수정
            block = Voxel(hit_info.entity.position + hit_info.normal, selected_block)
        
        elif key == 'right mouse down' and mouse.hovered_entity :
            destroy(mouse.hovered_entity)

# 1, 2, 3번을 통해 다양한 블록 생성 가능

    if key == '1':
        selected_block = 'grass'
    if key == '2':
        selected_block = 'dirt'   
    if key == '3':
        selected_block = 'stone'

def update() :
    hand.texture = block_textures.get(selected_block)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z), block_type="grass")

player = FirstPersonController()

app.run()