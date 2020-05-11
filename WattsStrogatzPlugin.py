import networkx

class WattsStrogatzPlugin:
	def input(self, filename):
                inputfile = open(filename, 'r')
                self.parameters = dict()
                for line in inputfile:
                   contents = line.split('\t')
                   self.parameters[contents[0]] = int(contents[1])


	def run(self):
                self.G = networkx.watts_strogatz_graph(self.parameters['nodes'],
                                                       self.parameters['k'],
                                                       self.parameters['probability'],
                                                       seed=1234)

	def output(self, filename):
		networkx.write_gml(self.G, filename)
