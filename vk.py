from id_from_username import IdFromUsername
from friends import Friends

uclient = IdFromUsername('mary.night')
uid = uclient.execute()
#print(uid)

friends_client = Friends(uid)
friends = friends_client.execute()

for (age, count) in friends:
    print('{} {}'.format(int(age), '#' * count))