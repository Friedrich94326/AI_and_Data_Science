import codecademylib
import pandas as pd

# Step 1: Analyzing Ad Sources
ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

total_views = ad_clicks.groupby('utm_source').user_id.count()
#print(total_views)

ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()
print(ad_clicks)


clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id').reset_index()
print(clicks_pivot)

sum_rows = clicks_pivot.sum(axis = 0)

#print(sum_rows)
#print(type(sum_rows))
#print(type(clicks_pivot))


clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False]) * 100
print(clicks_pivot)


# Step 2: Analyzing an A/B Test
Different_Ads = ad_clicks.groupby('experimental_group').user_id.count().reset_index()

print(Different_Ads)
Different_Ads.rename(\
  columns = {'user_id': 'number_of_examinees'},\
  inplace = True)

print(Different_Ads)

if ( Different_Ads.number_of_examinees.iloc[0]\
== Different_Ads.number_of_examinees.iloc[1]):
  print("the same!")

experimental = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
print(experimental)
experimental_pivot = experimental.pivot( index = 'experimental_group', columns = 'is_click', values = 'user_id')

experimental_pivot['click_percent'] = experimental_pivot[True] / \
( experimental_pivot[True] + experimental_pivot[False] ) * 100
print(experimental_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
print("a_clicks:")
print(a_clicks.head())
print("b_clicks:")
print(b_clicks.head())


"""
a_clicks_new = a_clicks.groupby('day').user_id.count().reset_index()
print(a_clicks_new)

a_sum_rows = a_clicks_new.sum(axis = 0)
print(a_sum_rows)
"""

# a_clicks
a_clicks = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
print(a_clicks.head())

a_clicks_pivot = a_clicks.pivot(
  columns = 'is_click',\
  index = 'day', \
  values = 'user_id'
)
print(a_clicks_pivot)
a_clicks_pivot['click_percent'] = \
 a_clicks_pivot[True] / \
 (a_clicks_pivot[True] + a_clicks_pivot[False]) * 100
print("/Ad_A_clicks_pivot/")
print(a_clicks_pivot)



# b_clicks
b_clicks = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
#print(b_clicks.head())

b_clicks_pivot = b_clicks.pivot(
  columns = 'is_click',\
  index = 'day', \
  values = 'user_id'
)
#print(b_clicks_pivot)
b_clicks_pivot['click_percent'] = \
 b_clicks_pivot[True] / \
 (b_clicks_pivot[True] + b_clicks_pivot[False]) * 100
print("/Ad_B_clicks_pivot/")
print(b_clicks_pivot)




