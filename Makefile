all: $(patsubst %.fa, bin_statistics_%.txt, $(wildcard *.fasta))

# Run's gc_correct.py for a given chromosome and corresponding counts_per_position and gc_prediction txt files for that chromosome
# Outputs bin statistics as tab delimited txt file with columns:
# "bin_position_range", "observed_bin_counts", "predicted_bin_counts","corrected_bin_counts"

# Example inputs:
# where % represents "chr1" 
# %.fa  
# counts_per_position_%.txt
# gc_prediction_%.txt
# B = 500   bin length
# W = 100   window length

# Output:
# bin_statistics_$B_$W_%.txt


# Example useage:
# make clean
# make chr1.fa B=700 W=180
# DOES it need to be make chr1.fa counts_per_position_%.txt  gc_per_position_%.txt ????


# Default values for B and W
B=500
W=200


clean:
	rm -f bin_statistics_*  


bin_statistics_$(B)_$(W)_%.txt: %.fa counts_per_position_%.txt gc_prediction_%.txt
	python gc_correct.py $^ $B $W $@


# $^ means insert all dependencies



