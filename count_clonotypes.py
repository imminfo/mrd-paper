import sys


def count_clonotypes_in_files(link_path):

	def get_sequence(words):
		tmp = 0
		res = ''

		try:
			tmp = float(words[2])
			res = words[3]
		except Exception:
			res = words[2]

		if not res: print("Empty string in NUC!!!")
		return res

	global_sequences = {}
	local_sequences = set()

	sample_list = []
	with open(link_path) as infile:
		sample = ''
		for line in infile:
			line = line.strip()

			if line[0] == '#':
				sample = line[1:]
				if sample:
					for seq in local_sequences:
						global_sequences[seq] = global_sequences.get(seq, 0) + 1
					local_sequences = set()

			elif line:
				target_file = line
				print("Searching in", target_file)

				for target_line in target_file:
					local_sequences.add(get_sequence(target_line.strip().split()))
					
        for seq in local_sequences:   
                global_sequences[seq] = global_sequences.get(seq, 0) + 1

	return global_sequences

if __name__ == '__main__':
	seq_dict = count_clonotypes_in_files(sys.argv[1])

	print("# Unique clonotypes: ", sum(filter(lambda x: x == 1, seq_dict.values())))
	print("# Public clonotypes: ", sum([1 for x in filter(lambda x: x > 1, seq_dict.values())]))
