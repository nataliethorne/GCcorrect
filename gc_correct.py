#Main python script to gc-correct sequence counts aligned to one #chromosome. This script steps through each position in the genome,
#calculates GC content in a window, estimates GC bias from gc bias
#function, corrects for the GC bias and then outputs sums of counts
#and corrected counts in a bin table file.

import sys
#Mytestrow
# args = ['chr1.fa','counts_per_position_chr1.txt',
#'gc_prediction_chr1.txt',1000, 249	]

#Input arguments
#B = binsize
#W = windowsize
#sequence = fasta file (genome sequence for this chromosome)
args = sys.argv
args = args[1:]
seqfile = args[0]
countsfile = args[1]
gcfuncfile = args[2]
binsize = int(args[3])
winsize = int(args[4])
print 'Sequence file: ' +seqfile
print 'Counts file: ' +countsfile
print 'GC bias function file: ' +gcfuncfile
print 'Binsize: ' + str(binsize)
print 'Window size: ' + str(winsize)

#Init reading and writing files
print 'Reading gc prediction function.'
gcreader = open(gcfuncfile,'r')
line = gcreader.readline()
while line != '':  #Read all lines of this file
				  #They are our prediction values
    line = gcreader.readline()

print 'Start reading fasta file.'
seqreader = open(seqfile,'r')
dummy = seqreader.readline()
print 'Start reading counts file.'
countsreader = open(countsfile,'r')
countline = reader.readline()

# initiate bin_position counter (i.e. where we are in a bin)
# initiate chr_postion in chromosome 
position_bin = 1 #Index of new position within bins (max binsize)
position_seq = 1 #Index of new position in sequence
seq_position_in_genome = 0
sequence = []
countlist = []
while seqline != '':  #While there are more positions to do
	
	#Read lines of seqfile and countsfile enough for this position
	sequence,position_in_genome = Readlines(position_in_genome=position_seq, sequence, seq_position_in_genome)
	
	
 	# get GC for that position 
	gc = get_position_GC(position, sequence, seqpositions, winsize)
	predlist = [predlinst,get_predicted_position_count()]

	# if bin_position>=B (yes, bin_position=0 and output bin statistics, no increment bin_position)
	if (position_bin>=binsize):
		correct_bin_count()
		write_bin_statistics()
		
	#Increment for next loop round
	position_bin += 1
	position_seq += 1		

close read and write file







