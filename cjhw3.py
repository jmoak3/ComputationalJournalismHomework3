from chroniclingamerica import ChronAm
from pprint import pprint

def getStates(fetcher):
	table = {}
	for item in fetcher.fetch():
		if "date" and "state" in item:
			key = item["state"][0] + item["date"][:3]
			if key in table:
				table[key] += 1
			else: 
				table[key] = 1
	return table

search_term = "witch"

fetcher1 = ChronAm(search_term, 1, 500)
statesTable = {}
statesTable.update(getStates(fetcher1))
print(statesTable)
f = open('1860Witches.csv', 'w')
for key, value in statesTable.items():
	f.write('{0},{1}\n'.format(key, value))