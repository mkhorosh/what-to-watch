import random
import  json

file_path = 'C:\\Users\\Marina\\rep\\what_to_watch\\list.json'
print("welcome, let's watch some great episode!")
with open(file_path, 'r') as file:
    shows = json.loads(file.read())
# print(shows)
show = random.choice(shows)
# print(show)

print('let it be "', end='')
name = ''.join(show.keys())
print(name, end='')
print('"', end=' ')
# print(show[name])
show_season = random.choice(list(show[name].keys()))
number_of_episodes = show[name][show_season]
# print(number_of_episodes)
show_episode = random.randint(1,number_of_episodes)
print('season ' + str(show_season), end=' ')
print('episode ' + str(show_episode))

print('open?:y/n')
if (name == 'friends'):
    page = 'https://friends-online.me/series/s'+str(show_season)+'e'+str(show_episode)
elif (name == 'how i met your mother'):
    page = 'http://met-mother.com/online/'+str(show_season)+'-season/'+str(show_episode)+'-seria-'+str(show_season)+'-season.html'
elif (name == 'the big bang theory'):
    page = 'https://big-bang-theory.online/episodes/'+str(show_season)+'-season-'+str(show_episode)+'-seriya'
if (input() == 'n'):
    page = '"null"'
page_path = 'C:\\Users\\Marina\\rep\\what_to_watch\\page.txt'
with open(page_path, 'w') as file:
    file.write(page)