# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

# Imports

# Body
def capitalize_nested(nested_lists):
	"""function flattens the nested list into a singled list, then joins the lists into a string
	then returns the string with all uppercase then splits the string back into a list. but shoot
	I just realized I'm supposed to return a new nested list and I don't know how to do that."""
	flattened = [' '.join(item) if type(item) is list else item for item in nested_lists]
	joined = ' '.join(flattened)
	capitalized = joined.upper()
	new_list = capitalized.split()
	print new_list


##############################################################################
def main():

    pass
    # capitalize_nested(['apple', ['bear'], 'cat'])
    # capitalize_nested(['reading', ['literacy', 'Literacy'], 'Reading'])

if __name__ == '__main__':
    main()