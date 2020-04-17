class Task:
    id = 0
    name = ''
    description = ''
    time = ''

    def __init__(self, n, d, t):
        self.id = 0
        self.name = n
        self.description = d
        self.time = t

    def __init__(self, id, n, d, t):
        self.id = id
        self.name = n
        self.description = d
        self.time = t

    def __str__(self):
        return ("ID: " + str(self.id) + "\n" + "Task Name: " + self.name + "\n" + "Description: " + self.description +
                "\n" + "Its time is: " + str(self.time))
