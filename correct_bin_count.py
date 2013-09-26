# calculate correct_bin_count

def correct_bin_count(observed_position_count, predicted_position_count):
	'''Take a list of observed_position_count and predicted_position_count to calculate the observed_bin_count, predicted_bin_count and corrected_bin_count'''
	observed_bin_count = sum(observed_position_count)
	predicted_bin_count = sum(predicted_position_count)
	i = 0
	corrected_position_count = []
	while i < len(observed_position_count):
		corrected_position_count.append(observed_position_count[i]/predicted_position_count[i])
		i +=1
	corrected_bin_count = sum(corrected_position_count)
	return corrected_bin_count, observed_bin_count, predicted_bin_count

corrected_bin_list = correct_bin_count(observed_position_count, predicted_position_count)

write_bin_statistics(bin_position_start, bin_position_end, corrected_bin_list[0], corrected_bin_list[1],corrected_bin_list[2])

