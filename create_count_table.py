# create a tab-delimited file containing two columns "Position" "Count"
def create_count_table(chr_length, number_of_positions, poisson_lam):
	'''Create a count table in tab-delimited format containing two columns "Position" "Count". This script take chromosome length (chr_length) and the number of positions (number_of_positions) to randomly selection the position and generate its correspondent counts in poisson distribution.
	'''
	# import libraries
	from random import randint
	from numpy import random
	
	# Create a list of position
	i = 0
	positions = []
	while i <= number_of_positions:
		positions.append(randint(0, chr_length))
		i += 1
	positions.sort()
	
	# write position and counts to file
	output=open('counts_per_position_chr1.txt', 'w')
	for pos in positions:
		output_string = str(pos) + '\t' + str(random.poisson(poisson_lam)) + '\n'
		output.write(output_string)
	output.close()
	
# call create_count_table function, remember to specify chr_length, number_of_positions, poisson_lam
create_count_table(20000, 15, 5)	

	
