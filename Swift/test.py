class Program(object):
    #CPU = [Number of CPU, Cores, Clock time]
    def __init__(self, name = 'Program', CPU = [1, 4, 2.0], RAM = 2, harddrive = 100, GPU = True):
        self.name = name
        self.CPU = CPU
        self.RAM = RAM
        self.harddrive = harddrive
        self.GPU = GPU
    def info(self):
        required_specs = {'Number_of_CPUs': self.CPU[0],
                          'Number_of_cores' : self.CPU[1],
                          'RAM' : self.RAM,
                          'harddrive' : self.harddrive,
                          'GPU' : self.GPU
                          }
        return required_specs

class Computer(object):
    #CPU = [Model, Cores, Clock time]
    #PSU = [Model, Watts]
    def get_spec(self):
        specs = {
            'name' : 'Computer',
            '$name': lambda x: specs.update({'name': x}),
            #Model, Cores, Clockrate
            'CPU' : ['Model', 4, 2.0],
            '$CPU': lambda x: specs.update({'CPU': x}),
            'Number_of_CPUs' : 1,
            '$Number_of_CPUs': lambda x: specs.update({'Number_of_CPUs': x}),
            'motherboard' : 'Mobo model',
            '$motherboard': lambda x: specs.update({'motherboard': x}),
            'RAM' : 4,
            '$RAM': lambda x: specs.update({'RAM': x}),
            'harddrive' : 250,
            '$harddrive': lambda x: specs.update({'harddrive': x}),
            'PSU' : ['', 0],
            '$PSU': lambda x: specs.update({'PSU': x})
        }
        def cf(self, data):
            if data in specs:
                print data + ": " + str(specs[data])
                return specs[data]
            else:
                print data + ": Not Found"
                return None
        return cf
    run = get_spec(1)

    def can_it_run(self, Program):
        info = Program.info()
        # for key in info:
        #     self.run(key)
        run = True
        for key in info:
            #if something does not match, then run = False
            print 'program: ' + str(key) + ' ' + str(info[key])
            if key == 'GPU':
                if(info[key] == True):
                    if (self.run("GPU") != True):
                        run = False
                        print 'GPU ' + str(run)
            elif key == 'Number_of_cores':
                if info[key] > self.run('CPU')[1]:
                    run = False
                    print 'cores ' + str(run)
            elif info[key] > self.run(key):
                run = False
                print key + ' ' + str(run)
        if run == False:
            print self.run("name") + " cannot run " + Program.name
        else:
            print self.run("name") + " can run " + Program.name

class SuperComp(Computer):
    def get_spec(self):
        specs = {
            'name' : 'Super Computer',
            '$name': lambda x: specs.update({'name': x}),
            'CPU' : ['Xenon', 18, 3.6],
            '$CPU': lambda x: specs.update({'CPU': x}),
            'Number_of_CPUs' : 2,
            '$Number_of_CPUs': lambda x: specs.update({'Number_of_CPUs': x})
        }
        def cf(self, data):
            if data in specs:
                print data + ": " + str(specs[data])
                return specs[data]
            else:
                return super(SuperComp, self).run(data)
        return cf
    run = get_spec(1)

class Gaming(Computer):
    def get_spec(self):
        specs = {
            'name' : 'Gaming Computer',
            '$name': lambda x: specs.update({'name': x}),
            'GPU' : True,
            '$GPU': lambda x: specs.update({'GPU': x}),
            'motherboard' : 'ASUS',
            '$motherboard': lambda x: specs.update({'motherboard': x}),
            'harddrive' : 750,
            '$harddrive': lambda x: specs.update({'harddrive': x}),
            'PSU' : ['Silver', 500],
            '$PSU': lambda x: specs.update({'PSU': x})
        }
        def cf(self, data):
            if data in specs:
                print data + ": " + str(specs[data])
                return specs[data]
            else:
                return super(Gaming, self).run(data)
        return cf
    run = get_spec(1)

# c1 = Computer()
# print "Printing for Default Computer"
# c1.run("name")
# c1.run("CPU")
# c1.run("motherboard")
# c1.run("RAM")
# c1.run("harddrive")
# c1.run("PSU")
# c1.run("Number_of_CPUs")
# c1.run("GPU")
# print
# s1 = SuperComp()
# print "Printing for Super Computer"
# s1.run("name")
# s1.run("CPU")
# s1.run("motherboard")
# s1.run("RAM")
# s1.run("harddrive")
# s1.run("PSU")
# s1.run("Number_of_CPUs")
# s1.run("GPU")
# g1 = Gaming()
# print
# print "Printing for Gaming Computer"
# g1.run("name")
# g1.run("CPU")
# g1.run("motherboard")
# g1.run("RAM")
# g1.run("harddrive")
# g1.run("PSU")
# g1.run("Number_of_CPUs")
# g1.run("GPU")
# p1 = Program()
# print 
# print "Printing Program"
# print p1.info()
# print
# print
# g1.can_it_run(p1)
# print
# s1.can_it_run(p1)
# print
# c1.can_it_run(p1)

# print
