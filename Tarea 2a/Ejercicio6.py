class Marsupial:
    def __init__(self):
        self.pouch = []
    def put_in_pouch(self, item):
        self.pouch = self.pouch + [item]
    def pouch_contents(self):
        return print(self.pouch)


m = Marsupial()
m.put_in_pouch("doll")
m.put_in_pouch("firetruck")
m.put_in_pouch("kitten")
m.pouch_contents()

class Kangaroo:
    def __str__(self):
        return f"I am a Kangaroo located at coordinates ({self.x_axis},{self.y_axis})"
    def __init__(self,x,y):
        self.pouch = []
        self.x_axis = 0
        self.y_axis = 0
    def put_in_pouch(self, item):
        self.pouch = self.pouch + [item]
    def pouch_contents(self):
        return print(self.pouch)
    def jump(self, dx, dy):
        self.x_axis = self.x_axis + dx
        self.y_axis = self.y_axis + dy

k = Kangaroo(0,0)
print(k)

k.put_in_pouch("doll")
k.put_in_pouch("firetruck")
k.put_in_pouch("kitten")
k.pouch_contents()

k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
print(k)