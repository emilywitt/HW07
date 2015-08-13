# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

# Imports

# Body
def is_sorted(various_lists):
	""" compares the list to the sorted version of the list. should this work if there are nested lists?
	it doesn't. how would I make it do that???"""
	sorted_list = sorted(various_lists)
	if sorted_list == various_lists:
		return True
	else:
		return False




##############################################################################
def main():

    pass
    # print is_sorted(['a', 'b', ['c','d']])
    # print is_sorted(['c','d'])
    # print is_sorted([[1], [2], [4,3], 9, 10])
    # print is_sorted([[1],2,3,[4,5]])

if __name__ == '__main__':
    main()