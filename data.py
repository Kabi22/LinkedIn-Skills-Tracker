import pandas as pd 
import json

df = pd.read_excel('public_use-industry-skills-needs.xlsx', 'Industry Skills Needs')

# print(df.isic_section_name.unique())
def data_collection(): 
    industry_names = df.industry_name.unique()

    sections = {'Mining and quarrying' : 'Mining', 
                'Manufacturing' : 'Manufacturing',
                'Information and communication' : 'Info',
                'Financial and insurance activities' : 'Finacial',
                'Professional scientific and technical activities':'Scientific-Technical',
                'Arts, entertainment and recreation':'Arts'}

    # industry_name_dict = {}
    # count = 0
    # for item in industry_names:
    #     industry_name_dict[item] = count
    #     count += 1 

    # print(industry_name_dict)
    skill_group_names = df['skill_group_name']
    skill_group_names_dict = {}
    for skill in skill_group_names:
        if skill not in skill_group_names_dict:
            skill_group_names_dict[skill] = 1
        else:
            skill_group_names_dict[skill] += 1

    # print(skill_group_names_dict)

    skill_rank = {}
    for ind in df.index: 
        if df['skill_group_name'][ind] not in skill_rank:
            skill_rank[df['skill_group_name'][ind]] = df['skill_group_rank'][ind]
        else:
            skill_rank[df['skill_group_name'][ind]] += df['skill_group_rank'][ind]

    for skill in skill_rank:
        skill_rank[skill] /= skill_group_names_dict[skill]

    # print(skill_rank)

    # with open('skill_name_ranks.json', 'w') as f:
    #     json.dump(skill_rank, f, indent=2)

    # with open('skill_name_frequencies.json', 'w') as f:
    #     json.dump(skill_group_names_dict,f, indent=2)
    with open('skill_name_frequencies.json','r') as f:
        freq = json.load(f)
    with open('skill_name_ranks.json','r') as f:
        ranks = json.load(f)


    print(freq)

def industry_names(): 
    names = df.industry_name.unique()
    industry_name_options = {}
    for name in names:
        industry_name_options[name] = name #creating this dictionary for the dropdown options
    
    options = []
    for k in industry_name_options:
        options.append({'label':k,'value':k})
    
    with open('dropdown_options.json', 'w') as f:
        json.dump(options,f,indent=2)

industry_names()