
# Takes in a list of tuples of (list_of_adjacent_kingdoms, kingdom)
# list_of_adjacent_kingdoms = an array of indices indicating each kingdom
# num_kingdoms is the number of kingdoms
# adj_matrix = the adjacency matrix of all our kingdoms in our problem
#
# return the most cost-efficient kingdoms (by their indices) to conquer
def min_weight_set_cover_approx_algo(tuple_list, num_kingdoms, adj_matrix)
	# our resulting set of kingdoms (by their indices) to conquer
	result = list([])

	# create and populate an ORIGINAL array of size num_kingdoms, starting from 0 to num_kingdoms-1
	ORIGINAL = Set([])
	for i in range(num_kingdoms):
		ORIGINAL.add(i)

	# initilize an empty NEW set
	NEW = Set([])
	# keep adding set_covers until there is no difference between NEW and ORIGINAL
	while len(NEW.difference(ORIGINAL)) != 0:
		efficient_tuple = ()
		efficient_cost = 0			# this is a float

		# look for the most efficient set to add to NEW
		for t in tuple_list:
			set_cover = t[0]
			kingdom_index = t[1]
			kingdom_efficiency = calc_efficiency(NEW, set_cover, kingdom_index, adj_matrix)

			if kingdom_efficiency > efficient_cost:
				efficient_tuple = t
				efficient_cost = kingdom_efficiency

		# add the most efficient set to the NEW set
		NEW.union(efficient_tuple[0])
		# add the kingdom to the set of kingdoms to conquer
		result.add(efficient_tuple[1])
		# remove the corresponding tuple from the list we're scanning
		tuple_list.remove(efficient_tuple)

	return result

# original_set = the set of all kingdoms in our problem
# candidate_set = the set that we may want to add to our NEW set above
# candidate_index = the candidate kinggdom's index
# adj_matrix = the adjacency matrix of all kingdoms in original_set
#
# returns the cost of conquering the candidate divided by the number of newly-added vertices
#	in decimal form
def calc_efficiency(original_set, candidate_set, candidate_index, adj_matrix)
	# cost is found at c_ii of the adj_matrix
	conquering_cost = adj_matrix[candidate_index][candidate_index]
	# find the length of the number of newly-added vertices
	num_new_vertices = len(original_set.difference(candidate_set))

	# if the candidate does not add any new vertices, return an efficiency of 0
	if num_new_vertices == 0:
		return 0
	return float(conquering_cost)/float(num_new_vertices)


# the original adjacency matrix
matrix = [][]
# visited array
visited = bool[]
# the resulting traversal list
traversal = list()
# length of the matrix
length = 0

# adj_matrix = the original matrix that we run DFS on
# start_index = the index we start DFS on
#
# return the DFS traversal on the corresponding graph
def DFS(adj_matrix, start_index)
	matrix = adj_matrix
	length = len(adj_matrix)

	# initialize the visited array to all false
	for i in range(length):
		visited[i] = false

	# run DFS
	DFS_helper(start_index)

	return traversal

def DFS_helper(i)
	# visit the vertex
	visited[i] = True
	# add the vertex to the traversal list (in order)
	traversal.add(i)

	# for all the adjacent vertices, run DFS
	for j in range(length):
        if !visited[j] && (matrix[i][j] is int):
            DFS(j);