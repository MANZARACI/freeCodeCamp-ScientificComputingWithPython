import random
import copy

class Hat:
    def __init__(self,**colors):
        self.contents=list()
        for a,b in colors.items():
            for i in range(b):
                self.contents.append(a)

    def draw(self,number):
        self.drBalls=list()

        if(number>len(self.contents)):
            return self.contents

        for i in range(number):
            a=self.contents.pop(random.randrange(len(self.contents)))
            self.drBalls.append(a)
        return self.drBalls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter=0
    for i in range(num_experiments):
        hat_copy=copy.deepcopy(hat)
        check=True
        x=hat_copy.draw(num_balls_drawn)
        for a,b in expected_balls.items():
            for m in range(b):
                if(a in x):
                    x.pop(x.index(a))
                else:
                    check=False
        if check:
            counter+=1
    
    return counter/num_experiments