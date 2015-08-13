# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

##############################################################################
# Imports

# Body
def nested_sum(all_the_lists):
    flattened_list = [sum(item) if type(item) is list else item for item in all_the_lists]
    print sum(flattened_list)

##############################################################################
def main():

    pass
    # nested_sum([10,0,[1,0]])

if __name__ == '__main__':
    main()