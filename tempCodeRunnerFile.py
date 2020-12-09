data = {'skill_names' : skill_names, 'skill_name_ranks' : skill_name_ranks,'skill_name_frequencies':skill_name_frequencies}
df = pd.DataFrame.from_dict(data)
print(df)