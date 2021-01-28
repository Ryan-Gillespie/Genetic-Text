from wrappers import roundAll, timer
import random
import math

class Population:
	def __init__(self, target, fit, ind, dnaLen, popSize, geneSet = None):
		self.target = target
		self.fit = fit
		self.ind = ind
		self.dnaLen = dnaLen
		self.popSize = popSize
		self.geneSet = geneSet

		self.mutationChance = .05
		
		self.genPopulation()
	
	def genPopulation(self):
		population = []
		for i in range(self.popSize):
			population.append(self.ind(self.dnaLen, self.geneSet))
		self.population = population
	
	def weighted_population(self):
		self.weightedPop = []
		targetFit = self.fit(self.target, self.target)
		for individual in self.population:
			try:
				weight = 1/abs((targetFit - self.fit(individual, self.target)) / targetFit)
			except ZeroDivisionError:
				weight = 100
			self.weightedPop.append([individual, weight])
		return self.weightedPop
	
	def weighted_choice(self, items):
		weight_total = sum((item[1] for item in items))
		n = random.uniform(0, weight_total)
		for item, weight in items:
			if n < weight:
				return item
			n = n - weight
		return item
	
	def createChildren(self, dna1, dna2):
		pos = int(random.random()*self.dnaLen)
		return (dna1[:pos]+dna2[pos:], dna2[:pos]+dna1[pos:])
	
	def randomFromGeneSet(self):
		pos = int(random.random()*len(self.geneSet))
		return self.geneSet[pos]
	
	def mutate(self, individual):
		for i in range(len(individual)):
			if(random.random() < self.mutationChance):
				individual[i] = self.randomFromGeneSet()
		return individual
	
	def avg_ind(self):
		sortedPop = self.getInd()
		halfway = math.ceil(self.popSize / 2)
		return sortedPop[0][halfway][0]
	
	def evolve(self, iterations):
		for i in range(iterations):
			self.wPop = self.weighted_population()
			self.population = []
			for x in range(int(self.popSize/2)):
				ind1 = self.weighted_choice(self.wPop)
				ind2 = self.weighted_choice(self.wPop)
				
				ind1, ind2 = self.createChildren(ind1,ind2)
				
				self.population.append(self.mutate(ind1))
				self.population.append(self.mutate(ind2))
		avg = self.avg_ind()
		return avg, self.fit(avg, self.target)

	def bestInd(self):
		ind = self.getInd()[0][0][0]
		return ind, self.fit(ind, self.target)

	def getInd(self):
		return sorted([self.wPop], key=lambda x: x[1])
	
	def __str__(self):
		best = self.bestInd()
		return ''.join([val for val in best[0]]) + ': '+str(best[1])
