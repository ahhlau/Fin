class Program(object):
	#CPU = [Number of CPU, Cores, Clock time]
	def __init__(self, name = 'Program', CPU = [0, 0, 0], RAM = 'RAM requirement', harddrive = 'harddrive memory requirement', GPU = True):
		self.name = name
		self.CPU = CPU
		self.RAM = RAM
		self.harddrive = harddrive
		self.GPU = GPU
	def info(self):
		required_specs = {'Number_of_CPUs': self.CPU[0],
							'Number_of_cores' : self.CPU[1],
							'Max_Clock_rate' : self.CPU[2],
							'RAM' : self.RAM,
							'harddrive' : self.harddrive,
							'GPU' : self.GPU
		}
		return required_specs

class Computer(object):
	#CPU = [Model, Cores, Clock time]
	#PSU = [Model, Watts]
	def __init__(self, name = 'Computer', CPU = [['', 0, 0]], motherboard = 'Mobo model', RAM = 'RAM', harddrive = 'harddrive memory', PSU = ['', 0], computer_type = "computer", GPU = False):
		self.name = name
		self.CPU = CPU
		self.motherboard = motherboard
		self.RAM = RAM
		self.harddrive = harddrive
		self.PSU = PSU
		self.computer_type = computer_type
		self.GPU = GPU

	def get_spec(self):
		specs = {
			'name' : 'hi',
			'$name': lambda x: specs.update({'name': x})
			# 'CPU' : self.CPU,
			# 'Number_of_CPUs' : len(self.CPU),
			# 'Max_Clock_rate' : self.find_maxclock(),
			# 'motherboard' : self.motherboard,
			# 'RAM' : self.RAM,
			# 'harddrive' : self.harddrive,
			# 'PSU' : self.PSU
		}
		def get(self, data):
			if data in specs:
				print data + ": " + specs[data]
				return specs[data]
			else:
				return None
		return get
	run = get_spec(1)

	# def get_specs(self):
	# 	specs = {
	# 		'name' : self.name,
	# 		'CPU' : self.CPU,
	# 		'Number_of_CPUs' : len(self.CPU),
	# 		'Max_Clock_rate' : self.find_maxclock(),
	# 		'motherboard' : self.motherboard,
	# 		'RAM' : self.RAM,
	# 		'harddrive' : self.harddrive,
	# 		'PSU' : self.PSU
	# 	}
	# 	print "Specs: "
	# 	print specs
	# 	return specs


	def find_maxclock(self):
		maxclock = self.CPU
		maxclock.sort(reverse = True, key = lambda x: x[2])
		return maxclock[0][2]

	def get_type(self):
		print "Type: " + self.computer_type

	def can_it_run(self, Program):
		info = Program.info
		specs = Computer.get_specs
		run = True
		for key in info:
			#if something does not match, then run = False
			if key == 'GPU':
				if(info[key] == True):
					if (computer.GPU == False): 
						run = False

			elif info[key] >= specs[key]:
				run = False
		if run == False:
			print self.name + "cannot  run " + Program.name
		else:
			print self.name + "can run " + Program.name
			

class Gaming(Computer):
	def __init__(self, GPU = True):
		self.computer_type = 'Gaming'

class SuperComp(Computer):
	def __init__(self, computer_type = 'Super', GPU = 'GPU'):
		self.computer_type = computer_type
		self.GPU = GPU

c1 = Computer()
c1.run('name')
p1 = Program()
