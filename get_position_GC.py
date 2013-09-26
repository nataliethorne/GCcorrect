def get_position_GC(position_in_genome, sequence, seq_position_in_genome, winsize):
	'''
	This function finds the GC content in a window of sequence.
	The size of the window is given by winsize
	The GC content in this window will be the GC value attributed to the starting position of the window (i.e. the current position in the genome).
	Because we only read in parts of the genome sequence at a time, we need to know the genomic position of the input sequence to determine where the genomic position is within the input sequence.
	'''


	# get position in current sequence
	pos_in_current_sequence= (position_in_genome - seq_position_in_genome) -1
	
	# get the sequence in the window for current position
    # add winsize-1 as indexing positions starts at 0 in python
	dna=sequence[position_in_current_sequence:(position_in_current_sequence+(winsize-1))] 

	# check for any N's in the reference sequence
    countN = dna.count('N')
    dna.replace('N',"")
    numGs = dna.count('G')
    numCs = dna.count('C')
    GC_content = (numGs + numCs)/float(len(dna))
    return GC_content


