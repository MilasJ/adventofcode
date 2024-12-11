from math import prod
class intcode():
    def __init__(self, program):
        # self.program = [program[i:i+4] for i in range(0,len(program),4)]
        self.program = program
        self.identifier = {
            1:sum,
            2:prod
        }
    def assign(self,chunk,func):
        args = self.program[chunk[1]],self.program[chunk[2]]
        self.program[chunk[3]] = func(args)
    def run(self):
        for i in range(0,len(self.program),4):
            if self.program[i] ==99:
                break
            chunk= self.program[i:i+4]
            func = self.identifier[chunk[0]]
            self.assign(chunk,func)