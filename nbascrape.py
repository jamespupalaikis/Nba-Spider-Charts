from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

# NBA season we will be analyzing
year = 2020# URL page we will scraping (see image above)
url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html)

####
# use findALL() to get the column headers
soup.findAll('tr', limit=2)# use getText()to extract the text we need into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]# exclude the first column as we will not need the ranking order from Basketball Reference for the analysis
headers = headers[1:]
#print(headers)

# avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]

stats = pd.DataFrame(player_stats, columns = headers)
#print(stats.infer_objects)


#

#To select rows whose column value equals a scalar, some_value, use ==:
#stats.loc[df['column_name'] == some_value]
#To select rows whose column value is in an iterable, some_values, use isin:
#stats.loc[df['column_name'].isin(some_values)]

def getPlayer(player, statstoget):
#['Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
	prow = stats.loc[stats['Player'] == player].values.tolist()
	#print('apple', prow)
	pickedstats = []
	def replace(x):
		if ((type(x) == type('s')) and x != ''):
			return float(x)
		else:
			return None

	for stat in statstoget:
		#print(stat, headers.index(stat), len(prow))
		if (stat in ['Player', 'Pos', 'Tm']):
			pickedstats.append(prow[0][headers.index(stat)])
		else:
			#print(stats[stat])
			#print(player)
			#print(prow)
			#print(len(prow[0][headers.index(stat)]))

			pickedstats.append(replace(prow[0][headers.index(stat)]))

		
	return pickedstats

'''for value in stats['FG%']:

	print(type(value), value)
	if((type(value) != type(None))and (value != '')):
		print('a', float(value))'''

def getMinMaxes():
	maxes = []
	for stat in headers:
		#print(stat)
		if (stat in ['Player', 'Pos', 'Tm']):
			maxes.append(None)
		else:
			#print(stats[stat])
			column = stats[stat].apply(lambda x: float(x) if ((type(x) == type('s')) and x != '') else 0)
			#print('|||||')
			#print(type(column[3]))
			max_index = column.max()
			maxes.append(max_index)
	return maxes

def getPlayerNorm(player, statstoget):
	unnorm = getPlayer(player, statstoget)
	#print('ASSSSSSSSSSSSSSSSSSSss')
	#print(unnorm)
	maxes = getMinMaxes()
	new = []
	for stat in statstoget:
		ind = headers.index(stat)
		if (maxes[ind] != None):
			new.append(unnorm[statstoget.index(stat)]/maxes[ind])
		else:
			new.append(unnorm[statstoget.index(stat)])
	return new

#print('a')
#print(getPlayerNorm('Chris Paul', ['Age', 'AST']))
#print(getPlayerNorm('LeBron James', ['Age', 'AST']))
#print(getPlayerNorm('Luka Dončić', ['PTS', 'AST', 'TRB', 'STL', 'BLK']))
#print(getPlayerNorm("Giannis Antetokounmpo", ['PTS', 'AST', 'TRB', 'STL', 'BLK']))
#print(getMinMaxes())
#def getTeam()
