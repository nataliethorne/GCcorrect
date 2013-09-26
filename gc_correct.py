#Main python script to gc-correct sequence counts aligned to one #chromosome.
#
import sys

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
print seqfile + countsfile + gcfuncfile
print binsize + winsize


#Start initalize reading
reader = open('pg76.txt','r')
outfile = 

# initiate bin_position counter (i.e. where we are in a bin)
# initiate chr_postion in chromosome 

reader = open(seqfile,'r')
#line = reader.readline()

position_bin = 0 #Index of positions within bins
position_seq = 0
print 'Start reading fasta file'
while line != '':  #While there are more positions to do
	
	#Read lines of seqfile and countsfile enough for this position
	res = Readlines()
	...
	
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







