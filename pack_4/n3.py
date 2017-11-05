from random import randint

MAX_LIFESPAN = 3
NUMBER_OF_STEPS = 8
RIVER_LENGTH = 10
NUMBER_OF_BEARS = 2
AMOUNT_OF_FISH = 3

MAX_LIFESPAN = int(input('Maximum bears\' lifespan: '))
NUMBER_OF_STEPS = int(input('Number of steps: '))
RIVER_LENGTH = int(input('River length: '))
NUMBER_OF_BEARS = int(input('Number of bears: '))
AMOUNT_OF_FISH = int(input('Amount of fish: '))


class River(list):
    def __init__(self, length, bears_n = 0, fish_n = 0):
        self.length = length
        for i in range(length):
            self.append(None)
        self.bears, self.fish = [], []
        self.populate(bears_n, fish_n)

    def populate(self, bears_n, fish_n):
        l = [i for i in range(self.length)]
        a_bear = Bear([None], 0)
        a_fish = Fish([None], 0)

        for i in range(bears_n):
            j = randint(0, len(l)-1)
            a_bear.create(self)
            del l[j]

        for i in range(fish_n):
            j = randint(0, len(l)-1)
            a_fish.create(self)
            del l[j]

    def draw(self, step):
        out = ''
        for cell in river:
            t = type(cell)
            if t == type(None):
                out += '-'
            elif t == Bear:
                out += 'B'
            elif t == Fish:
                out += 'f'
        out += '  ' + str(step)
        print(out)

class Animal:
    def __init__(self, river, position):
        self.position = position
        river[position] = self

    #make static?
    def create(self, river, position = -1):
        a = []
        for i in range(len(river)):
            if river[i] == None:
                a.append(i)
        if len(a) > 0:
            if position == -1:
                pos = randint(0, len(a)-1)
            else:
                pos = position
            if type(self) == Bear:
                river.bears.append(Bear(river, a[pos]))
            elif type(self) == Fish:
                river.fish.append(Fish(river, a[pos]))

    def kill(self, river):
        river[self.position] = None
        if type(self) == Bear:
            del river.bears[river.bears.index(self)]
        elif type(self) == Fish:
            del river.fish[river.fish.index(self)]

    def move(self, river):
        m = randint(0, 2)
        #print(str(self.position) + ',' + str(m), end=' ')
        if m == 0:
            pass
        else:
            if m == 1:
                d = -1 #left
            elif m == 2:
                d = 1 #right
            if self.position+d > -1 and self.position+d < len(river):
                t = type(river[self.position+d])
                #moving to ... (t is the destination)
                if t == type(None):
                    river[self.position], river[self.position+d] = river[self.position+d], river[self.position]
                    self.position += d
                elif t == type(self):
                    self.create(river)
                elif t == Fish:
                    river[self.position+d].kill(river)
                    river[self.position], river[self.position+d] = river[self.position+d], river[self.position]
                    self.position += d
                    river[self.position].lifespan = MAX_LIFESPAN
                elif t == Bear:
                    self.kill(river)
                    river[self.position+d].lifespan = MAX_LIFESPAN

class Bear(Animal):
    def __init__(self, river, position):
        self.position = position
        river[position] = self
        self.lifespan = MAX_LIFESPAN

class Fish(Animal):
    pass

river = River(RIVER_LENGTH, NUMBER_OF_BEARS, AMOUNT_OF_FISH)
river.draw(0)
for i in range(NUMBER_OF_STEPS):
    for animal in river.bears + river.fish:
        if animal in river.bears + river.fish:
            animal.move(river)
    for animal in river.bears:
        animal.lifespan -= 1
        if animal.lifespan < 1:
            animal.kill(river)
    #print()
    river.draw(i+1)
