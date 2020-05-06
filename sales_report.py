"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []
# combo into one dictionary so you can look up each person and return melons sold

f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')
# parses the text file to loop over each line and split each word into a list

    salesperson = entries[0]
    melons = int(entries[2])
    # assigning variable "salesperson" to value at index 0 and "melons" to value at index 2

    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        # assuming this is looking up the person's name in another file and returning their position.
        # we could add this to values in dictionary (position: position_title)

        melons_sold[position] += melons
        # this is associating the index of one list with the index of another to get a value. We should combine in dictionary.
        # add (melons_sold += Integer)
    else:
        salespeople.append(salesperson)
        # if salesperson doesn't exist, add them to the report
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
#prints a summary for each salesperson. instead we could do this from the dictionary.
