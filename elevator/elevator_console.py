class Elevator:
    
    def __init__(self):
        self.elevator = {}
        
    def create(self, n = 1):
        if self.elevator != {}:
            elevator_list = [key for key in self.elevator]
            elevator_list.sort()
            start = elevator_list[-1] + 1
            stop = start + n
        else:
            start = 1
            stop = start + n
        for i in range(start, stop):
            self.elevator[i] = {'move' : False, 'floor': 1}
        return self.elevator
        
    def delete(self, n = 1):
        if self.elevator != {}:
            elevator_list = [key for key in self.elevator]
            elevator_list.sort()
            start = len(elevator_list)
            stop = start - n
            for i in range(start, stop, -1):
                del self.elevator[i]
            return self.elevator
        else:
            print('No elevators')
    
    def show(self):
        return self.elevator
    
    
    
a = Elevator()
b = Elevator()


a.create(5)
a.delete()


b.create(4)
b.delete()

print(a.show())
print(b.show())