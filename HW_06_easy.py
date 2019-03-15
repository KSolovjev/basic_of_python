#Task1
class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = int(speed)
        self.color = color
        self.is_police = bool
        #self.go()
        #self.stop()

    def go(self):
        print('The car is driving')
    def stop(self):
        print('The car is stoping')
    def turn(self,direction):
        if direction == 'l':
            print('The car is turning to the left')
        elif direction == 'r':
            print('The car is turning to the right')
        else:
            print 'Incorrect argument'

class SportCar(Car):
    pass

class PoliceCar(Car):
    def police(self):
        if self.is_police == True:
            print ('Police car')
        else:
            print ('Not police car')

class TownCar(Car):
    pass

class WorkCar(Car):
    pass

a=SportCar('BMW', 150, 'black',False)
b=TownCar('Toyota', 60, 'green', False)
c=PoliceCar('Cadillac', 90, 'white', True)
#print ('{} {} drives at a speed of {} km/h'.format (a.color, a.name, a.speed), a.turn('r'))
print c.police()