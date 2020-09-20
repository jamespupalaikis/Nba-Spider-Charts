import matplotlib.pyplot as plt
import pandas as pd
from math import pi
#import datacalc as dc
#import datasheet as ds
import nbascrape as scraper 
###############################################################################
################################################
##############################################
'''
print(ds.pdict.keys())

##################################
################################################
################################################
################################################

def getminmax(statnum):#//indexes from 1, just cuz
#players = ['LebronJames', 'JamesHarden', "GiannisAntetokounmpo", 
#"LukaDoncic", "PaulGeorge", "JaredHarper"] 
#stat1 =
	#print(statnum, [dc.profile(ds.pdict[name])[statnum-1] for name in ds.pdict.keys()])
	listnow = [(ds.pdict[name])[statnum-1] for name in ds.pdict.keys()]
	return (min(listnow), max(listnow))

#stat2 = [dc.profile(ds.pdict[name])[1] for name in players]
#stat3 = [dc.profile(ds.pdict[name])[2] for name in players]
#stat4 = [dc.profile(ds.pdict[name])[3] for name in players]
#stat5 = [dc.profile(ds.pdict[name])[4] for name in players]


'''

##################################
#['Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%',
# 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
lakers = ['LeBron James', 'Anthony Davis', "JaVale McGee", 
"Danny Green", "Dwight Howard", 'Alex Caruso']
clippers = ["Kawhi Leonard", 'Lou Williams', 'Patrick Beverley', 'Montrezl Harrell', 'Paul George', 'Ivica Zubac']
nuggets = ['Nikola Jokić', 'Jamal Murray', 'Paul Millsap', 'Gary Harris', 'Jerami Grant', 'Will Barton']
rockets = ['James Harden', 'Russell Westbrook', 'P.J. Tucker', 'Danuel House', 'Eric Gordon', 'Austin Rivers']

forplot =  ['Giannis Antetokounmpo', 'Jamal Murray', 'Carmelo Anthony', 'Damian Lillard', 'Bradley Beal', 'James Harden']
Pts, Ass, Reb, Stl, Blk = [],[],[],[],[]

for player in forplot:
	print(player)
	prof = scraper.getPlayerNorm(player, ['PTS', 'AST', 'TRB', 'STL', 'BLK'])
	Pts.append(prof[0])
	Ass.append(prof[1])
	Reb.append(prof[2])
	Stl.append(prof[3])
	Blk.append(prof[4])

'''
Pts = [ds.pdict[name][0] for name in forplot]
Ass = [ds.pdict[name][1] for name in forplot]
Reb = [(ds.pdict[name])[2] for name in forplot]
Stl = [(ds.pdict[name])[3] for name in forplot]
Blk = [(ds.pdict[name])[4] for name in forplot]'''
'''
def normalize(list, st, mx = 0, flooradd =True):

	if(mx != 0):
		norm = mx
	else:
		norm = getminmax(st)[1]
	minval = 0
	if(flooradd):
		minval = getminmax(st)[0]
	if (norm == 0):
		norm = 10**(-7)
	return [(a - minval)/(norm-minval) for a in list]
Pts, Ass, Reb, Stl, stat5a = normalize(Pts, 1), normalize(Ass, 2), normalize(Reb, 3), \
normalize(Stl,4), normalize(Blk,5)

print(Pts, Ass, Reb, Stl, Blk)'''
################################################
################################################
################################################
################################################


#Set data
df = pd.DataFrame({
'group':forplot,
'Points': Pts,
'Assists': Ass,
'Rebounds': Reb,
'Steals': Stl,
'Blocks': Blk,
})
 
def make_spider( row, title, color):
	# number of variable
	categories=list(df)[1:]
	N = len(categories)
	# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
	angles = [n / float(N) * 2 * pi for n in range(N)]
	angles += angles[:1]
	# Initialise the spider plot
	ax = plt.subplot(2,6,2*row + 1, polar=True, )
	# If you want the first axis to be on top:
	ax.set_theta_offset(pi / 2)
	ax.set_theta_direction(-1)
	# Draw one axe per variable + add labels labels yet
	plt.xticks(angles[:-1], categories, color='grey', size=6)
	# Draw ylabels
	ax.set_rlabel_position(0)
	plt.yticks([0,.25,.5,.75], [" "," "," "," "], color="grey", size=7)
	plt.ylim(0,1)
	# Ind1
	values=df.loc[row].drop('group').values.flatten().tolist()
	values += values[:1]
	ax.plot(angles, values, color=color, linewidth=1, linestyle='solid')
	ax.fill(angles, values, color=color, alpha=0.4)
	 
	# Add a title
	plt.title(title, size=11, color=color, y=1.5)
	 
	# ------- PART 2: Apply to all individuals
	# initialize the figure
	my_dpi=96
	#plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
	 
	# Create a color palette:
my_palette = plt.cm.get_cmap("Set2", len(df.index))
 
# Loop to plot
for row in range(0, len(df.index)):
	make_spider( row=row, title=df['group'][row], color=my_palette(row))
plt.show()