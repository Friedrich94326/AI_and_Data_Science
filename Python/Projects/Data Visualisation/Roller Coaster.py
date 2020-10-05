# Goal: To create several data visualizations that will give you insight into the world of roller coasters


import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
Wood_df = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
Steel_df = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

print("Award Winners Wood:")
print(Wood_df.head())
print("Award Winners Steel:")
print(Steel_df.head())



# write function to plot rankings over time for 1 roller coaster here:

El_Toro_Wood = Wood_df[Wood_df.Name == "El Toro"]
print(El_Toro_Wood[['Rank', 'Year of Rank']])

def Ranks_over_Years(name, park):
  dfWood = Wood_df[(Wood_df['Name'] == name)\
                    & (Wood_df['Park'] == park)]
  plt.plot(dfWood['Year of Rank'], dfWood['Rank'], marker = 'o', linestyle = '--')
  plt.xlabel('year')
  plt.ylabel('rank')
  plt.legend([name], loc = 1)
  plt.title("Roller coasters of the same name at different amusement parks")
  plt.show()

Ranks_over_Years("El Toro", "Six Flags Great Adventure")
# differentiate between roller coasters of the same name at different amusement parks

plt.clf() #  clear the figure only

# write function to plot rankings over time for 2 roller coasters here:

def Ranks_over_Years2(name1, name2, park1, park2):
  dfWood1 = Wood_df[(Wood_df['Name'] == name1)\
                    & (Wood_df['Park'] == park1)]
  plt.plot(dfWood1['Year of Rank'], dfWood1['Rank'], color = 'blue', marker = 'o', linestyle = '--')

  dfWood2 = Wood_df[(Wood_df['Name'] == name2)\
                    & (Wood_df['Park'] == park2)]
  plt.plot(dfWood2['Year of Rank'], dfWood2['Rank'], color = 'red', marker = 's', linestyle = '--')

  plt.xlabel('year')
  plt.ylabel('rank')
  plt.yticks([1, 2, 3, 4])
  plt.legend([name1 + " from " + park1, name2 + " from " + park2], loc = 1)
  plt.title("Roller coasters of 2 kinds at different amusement parks")
  plt.show()

# differentiate between roller coasters of the same name at different amusement parks
Ranks_over_Years2("El Toro", "Boulder Dash", "Six Flags Great Adventure", "Lake Compounce")

plt.clf()




# write function to plot top n rankings over time here:

def Top_N_Rankings(n, df):
  ranking_DF = df[ (df['Rank'] <= n ) ]
  fig, ax = plt.subplots(figsize = (10, 10))
  years = ranking_DF['Year of Rank']
  ranks = ranking_DF['Rank']
  ax.plot(years, ranks, marker = 'o', linestyle = '--')
  ax.set_xlabel('year')
  ax.set_ylabel('rank')
  ax.set_yticks(range(n))
  ax.set_title("Top " + str(n) +" ranked roller coasters")
  plt.show()

Top_N_Rankings(5, Wood_df)


# sample code
def top_ranking(df, n):
  top = df[ df['Rank'] <= n ]
  fig, ax = plt.subplots(figsize=(10,10))

  for coaster in set(top['Name']):
    coaster_rankings = top[top['Name'] == coaster]

  ax.plot(coaster_rankings['Year of Rank'],             coaster_rankings['Rank'], marker = 'o', label = coaster)
  ax.set_yticks([i for i in range(1,6)])
  plt.title("Top " + str(n) + " Rankings")
  plt.xlabel('Year')
  plt.ylabel('Ranking')
  plt.legend(loc = 4)
  plt.show()

top_ranking(Wood_df, 5)


# Unfinished Project
