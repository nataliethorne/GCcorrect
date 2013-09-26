
def Readlines(position_in_genome, sequence, seq_position_in_genome, seqreader, countslist, position_in_bin, countsreader)

	# This hasn't bee implemented yet.

	#########
	# Remove unneccessary sequence in current memory
	#########
	# remove positions in sequence that are less than position
	# if removed above; update sequence_position_in_genome


	#########
	# Read more sequence to do GC window calculation for the current position_in_genome
	#########
	# if  seq_position+len(sequence) < position_in_genome+winsize
	# read next line from reader and append to sequence
	# update len(sequence)
	# repeat this block while seq_position+len(sequence) < position_in_genome+winsize

	
	#########
	# Read from countsreader to get all counts within the bin
	#########
	# if position_in_bin ==0; get counts for the next bin (position_in_genome + binsize)

	#last line read from countsreader
	#if position in this last line is > than position_in_genome
	#keep current line in current_bin_counts list

	#if position in current line from counts reader is < position_in_genome+binsize
	# read next line in countsreader and append to current_bin_counts list
	# repeat this block until position in counts reader is >= position_in_genome+binsize

	# sum counts in bin store as counts object

	return sequence seq_position_in_genome counts
