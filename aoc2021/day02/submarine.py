from recordclass import recordclass

Position = recordclass("Position", "horizontal depth")

class Submarine:
    def __init__(self, horizontal_start=0, depth_start=0):
        self.position = Position(horizontal=horizontal_start, depth=depth_start)
    
    def navigate(self, directions):
        for direction, value in directions:
            match direction:
                case "forward":
                    self.position.horizontal += int(value)
                case "up":
                    self.position.depth -= int(value)
                case "down":
                    self.position.depth += int(value)


Position2 = recordclass("Position2", "aim horizontal depth")

class Submarine2:
    def __init__(self, aim_start=0, horizontal_start=0, depth_start=0):
        self.position = Position2(aim=aim_start, horizontal=horizontal_start, depth=depth_start)
    
    def navigate(self, directions):
        for direction, value in directions:
            match direction:
                case "forward":
                    self.position.horizontal += int(value)
                    self.position.depth += int(value) * self.position.aim
                case "up":
                    self.position.aim -= int(value)
                case "down":
                    self.position.aim += int(value)
