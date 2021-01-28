from GeneBasic import *
from random import choice

genome = ['abcdefghijklmnopqrstuvwxyz .,!?'[i] for i in range(31)]

def fit(individual, target):
	score = 0
	for i in range(len(individual)):
		if individual[i] == target[i]:
			score += 1
	
	return score

def genIndividual(length, geneSet):
	ind = []
	for i in range(length):
		ind.append(random.choice(genome))
	
	return ind


if __name__ == '__main__':
	target = input("What should the message say? > ")
	pop = Population(target, fit, genIndividual, len(target), 100, genome)

	lastBest = pop.evolve(1)
	while lastBest[1] != len(target):
		lastBest = pop.evolve(1)
		print(''.join(lastBest[0]) + ': ' + str(lastBest[1]))