from GeneBasic import *
from random import choice
import time

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
	# Get the target message
	print('Type the message you would like the genetic algorithm to spell out.')
	print('Valid characters include the alphabet and space , . ? !')
	target = input('What should the message say? > ')

	# process the target a bit
	if target == '':
		target = 'Hire Me'
	
	# preserve the capital letters while not expanding the genome
	capitals = [0 for i in range(len(target))]
	for i in range(len(target)):
		if target[i].isupper():
			capitals[i] = 1
	target = target.lower()

	# check for invalid characters
	for i in range(len(target)):
		if target[i] not in genome:
			print('Target text contains invalid characters, setting to "Hire Me"')
			target = 'Hire Me'
			time.sleep(5)

	# initialize the genetic algorithm
	pop = Population(target, fit, genIndividual, len(target), 100, genome)

	# evolve the population and report to the user
	i = 0
	lastBest = pop.evolve(1)
	while lastBest[1] != len(target):
		lastBest = pop.evolve(1)

		# re-insert capital letters
		for i in range(len(lastBest[0])):
			if capitals[i] == 1:
				lastBest[0][i] = lastBest[0][i].upper()

		print(''.join(lastBest[0]) + ': ' + str(lastBest[1]))
		i += 1
	print('Finished in ' + str(i) + ' Generations')
