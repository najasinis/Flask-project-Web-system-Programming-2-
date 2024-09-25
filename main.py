from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

Entity(
    parent=scene,
    model='sphere',
    texture=load_texture('위한.png'),
    scale=100,
    double_sided=True
)

hand = Entity(
    parent=camera.ui,
    model='cube',
    texture='brick',
    scale=0.3,
    rotation=Vec3(-10, -10, 10),
    position=Vec2(0.5, -0.5)
)

def update() :
    if held_keys['left mouse'] or held_keys['right mouse'] :
        hand.position = Vec2(0.4, -0.5)
    else :
        hand.position = Vec2(0.5, -0.5)

class Voxel(Button) :
    def __init__(self, position=(0, 0, 0), texture='brick') :
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=1.0
        )
    
    def input(self, key) :
        if self.hovered :
            if 'left mouse down' == key :
                Voxel(position=self.position + mouse.normal)
            elif 'right mouse down' == key :
                destroy(self)

for z in range(20) :
    for x in range(20) :
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()

app.run()