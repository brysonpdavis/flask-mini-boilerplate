#!C:\Python37\python.exe
import sys
import operator
import requests
import json
import twitter
import heapq
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

class Person(object):
  """
  Person's instance variables:
  :self.handle
  :self.pi_result
  :self.flat_data
  :self.top_5_traits
  """

  def __init__(self, handle):

    self.handle = handle

    twitter_consumer_key = 'DJNYG9zMErdfOu6pEuyP6G42l'
    twitter_consumer_secret = 'goURqOB0vN5BQvVQvcKTLkrIge9mjJkBV32pVeKK4zNgNAbRZw'
    twitter_access_token = '947704874409578498-FJAbBVEoqTd3Q2Wal0HpUaJCw2CIzDO'
    twitter_access_secret = 'pOxfJ8gecYnNldX9Thq2ydERYEnBuqr0zvWvgFGTemZnQ'
    
    pi_username = '522d0709-1460-412e-a024-44bf4fad8c29'
    pi_password = 'L73jQNdAwvR8'

    twitter_api = twitter.Api(consumer_key=twitter_consumer_key, 
                              consumer_secret=twitter_consumer_secret, 
                              access_token_key=twitter_access_token, 
                              access_token_secret=twitter_access_secret)

    statuses = twitter_api.GetUserTimeline(screen_name=self.handle,
                                          count=200,
                                          include_rts=False)
    text = ""
    for status in statuses:
      if (status.lang == 'en'):
        text += status.text#.encode('utf-8')
        #py3 does not need the encode

    #creating instace of Watson API
    personality_insights = PersonalityInsights(username=pi_username,password=pi_password)
    #anaylze the body of text retrieved from Twitter

    self.pi_result = personality_insights.profile(text)

  #flattens the tree structure data obtained from the analyze()
  #stores the traits in a dictionary
  def get_flat_data(self):
      self.flat_data = {}
      for c in self.pi_result['tree']['children']:
          if 'children' in c:
            for c2 in c['children']:
                  if 'children' in c2:
                      for c3 in c2['children']:
                          if 'children' in c3:
                              for c4 in c3['children']:
                                  if (c4['category'] == 'personality'):
                                      self.flat_data[c4['id']] = c4['percentage']
                                      if 'children' not in c3:
                                          if (c3['category'] == 'personality'):
                                                  self.flat_data[c3['id']] = c3['percentage']
      return self.flat_data
      #flat_data returned as {Trait:Value}
      #{u'Dutifulness': 0.8791187812473007, u'Cooperation': 0.5236241021826932}
      #need to find a way to extract the most evident traits from flat_data

  def get_top_5(self):
    self.top_5_traits = heapq.nlargest(5, self.flat_data, key=self.flat_data.get)
    return(self.top_5_traits)


#testing testing
'''
barry=Person('@BarackObama')
print('BARRY\'S PI_RESULTS')
print(barry.pi_result)
print('BARRY\'S FLATTENED DATA')
print(barry.get_flat_data())
print('BARRY\'S TOP 5 TRAITS')
print(barry.get_top_5())
'''


#compare function belongs outside class
#compares two dictionaries, returns the trait and distance
def get_similarities(dict1,dict2):
  #dict1, dict2 would be the flat_data variable for two separate Person objects
  compared_data = {}
  for keys in dict1:
    if dict1[keys] != dict2[keys]:
      compared_data[keys]=abs(dict1[keys] - dict2[keys])

  sorted_result = sorted(compared_data.items(),key=operator.itemgetter(1))

  return sorted_result[:5]

barry = Person('@BarackObama')
barry_flat_data = barry.get_flat_data()
barry_top_5 = barry.get_top_5()

don = Person('@realDonaldTrump')
don_flat_data = don.get_flat_data()
don_top_5 = don.get_top_5()

top_5_sim = get_similarities(barry_flat_data,don_flat_data)

print("BARRY'S FLATTENED PI_RESULTS")
print(barry_flat_data)
print("BARRY'S TOP 5")
print(barry_top_5)
print("DON'S TOP 5")
print(don_top_5)
print("TOP 5 SIMILARITIES")
print(top_5_sim)

#Prints the data in readable format
i = 1
for keys,value in top_5_sim:
  print("{})".format(i))
  print(keys)
  print(barry.handle)
  print(barry_flat_data[keys])
  print(don.handle)
  print(don_flat_data[keys])
  print('->')
  print(value)
  i += 1