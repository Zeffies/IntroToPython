def dataset(data):
	number_of_a = data.count('A')
	number_of_g = data.count('G')
	number_of_c = data.count('C')
	number_of_t = data.count('T')
	print(number_of_a, number_of_c, number_of_g, number_of_t)


dataset('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
