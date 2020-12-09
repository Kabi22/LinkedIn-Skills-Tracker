import pandas as pd 
import json 

with open('skill_name_frequencies.json', 'r') as f:
    freq = json.load(f)
with open('skill_name_ranks.json', 'r') as f:
    ranks = json.load(f)

skill_names = []
skill_name_frequencies = []
skill_name_ranks = []
for name in ranks:
    skill_names.append(name)
    skill_name_ranks.append(ranks[name])

for name in freq:
    skill_name_frequencies.append(freq[name])

print(len(skill_names))
print(len(skill_name_ranks))
print(len(skill_name_frequencies))

data = {'skill_names' : skill_names, 'skill_name_ranks' : skill_name_ranks,'skill_name_frequencies':skill_name_frequencies}
df = pd.DataFrame.from_dict(data)
print(df)