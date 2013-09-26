# write bin statistics to file


# let chr_number be an integer: chr_number = 1
# write to a file bin_statistics_chr'chr_number'.txt

chr_number = 1
filename = 'bin_statistics_chr' + str(chr_number) + '.txt'
one_line_bin_statistics = open(filename,'w')

def write_bin_statistics(bin_position_start, bin_position_end, corrected_bin_count, observed_bin_count, predicted_bin_count)
	'''Write bin statistics to file in tab delimited format.
	The column order is: "Bin" "corrected_bin_count" "observed_bin_count" "predicted_bin_count"'''
	one_line_bin_statistics.write(str(bin_position_start) + '-' + str(bin_position_end) + '\t' + str(corrected_bin_count) + '\t' + str(observed_bin_count) + '\t' + str(predicted_bin_count) + '\n')
	

one_line_bin_statistics.close()

