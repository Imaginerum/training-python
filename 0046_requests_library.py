import requests
import json
import pprint
from collections import defaultdict

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_task_frequency(tasks):
    completedTasksFrequenciesByUser = defaultdict(int)
    for entry in tasks:
        if entry['completed'] == True:
            completedTasksFrequenciesByUser[entry["userId"]] += 1
    return completedTasksFrequenciesByUser

def get_keys_with_top_values(my_dict):
    return [
        key
        for key, value in my_dict.items()
        if value == max(my_dict.values())
    ]

def get_users_with_top_completed_tasks(completedTasksFrequenciesByUser):
    userIdWithMaxCompletedTasks = []
    maxAmountOfCompletedTask = max(completedTasksFrequenciesByUser.values())
    for userId, numberOfCompletedTask in completedTasksFrequenciesByUser.items():
        if numberOfCompletedTask == maxAmountOfCompletedTask:
            userIdWithMaxCompletedTasks.append(userId)
    return userIdWithMaxCompletedTasks
try:
    #tasks = json.loads(r.text)
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("niepoprawny format")
else:
    completedTasksFrequenciesByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = get_users_with_top_completed_tasks(completedTasksFrequenciesByUser)

# SPOSÓB 1
"""
r = requests.get("https://jsonplaceholder.typicode.com/users")

users = r.json()

for user in users:
    if user["id"] in usersWithTopCompletedTasks
        print("Wręczamy ciasteczko mistrzunia dyscypliny do użytkownika o nazwie: ", user["name"])
"""
# SPOSÓB 2
"""
for userId in usersWithTopCompletedTasks:
    r = requests.get("https://jsonplaceholder.typicode.com/users/"+str(userId))
    user = r.json()
    print("Wręczamy ciasteczko mistrzunia dyscypliny użytkownikowi o imieniu: ", user["name"])
"""
#SPOSÓB 3

def change_list_into_conj_of_param(my_list):
    conj_param = 'id='
    lastIterationNumber = len(my_list)
    i = 0
    for item in  my_list:
        i += 1
        if i == lastIterationNumber:
            conj_param += str(item)
        else:
            conj_param += str(item) + '&id='

conj_param = change_list_into_conj_of_param(usersWithTopCompletedTasks)
r = requests.get("https://jsonplaceholder.typicode.com/users", params = conj_param)
pprint.pprint(completedTasksFrequenciesByUser)