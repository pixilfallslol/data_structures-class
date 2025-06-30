class Robot:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print("My name is "+self.name)
        
robot = Robot("kurt")
robot.introduce()