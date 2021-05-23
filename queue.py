class Queue:
    def __init__(self, name = 'unknown'):

        self.list = []
    def add(self, insert):
        print('добавили в очередь')
        if insert < 0:
            raise ValueError('такого не может быть')
        (self.list).append(insert)
        return self.list
    def delete(self):
        print('убради из очереди')
        self.list.pop(0)
        return self.list
    def view(self):
        print('очередь имеет следующий вид')
        return self.list[0]


Q1 = Queue()

Q1.add(1)
Q1.add(5)
Q1.add(2)
Q1.delete()
print(Q1.view())

