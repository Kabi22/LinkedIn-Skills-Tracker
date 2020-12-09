import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import json

df = pd.read_excel('public_use-industry-skills-needs.xlsx',
                   'Industry Skills Needs')
with open('json\skill_name_frequencies.json', 'r') as f:
    freq = json.load(f)
with open('json\skill_name_ranks.json', 'r') as f:
    ranks = json.load(f)
with open('json\dropdown_options.json', 'r') as f:
    option_array = json.load(f)

skill_names = []
skill_name_frequencies = []
skill_name_ranks = []
for name in ranks:
    skill_names.append(name)
    ranks[name] = 11-ranks[name]
    skill_name_ranks.append(ranks[name])

for name in freq:
    skill_name_frequencies.append(freq[name])


data = {'skill_name': skill_names, 'skill_name_rank': skill_name_ranks,
        'skill_name_frequency': skill_name_frequencies}
df = pd.DataFrame.from_dict(data)
df2 = pd.read_excel('public_use-industry-skills-needs.xlsx', 'Industry Skills Needs')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, title="LinkedIn Skills Tracker")
fig = px.scatter(df, x="skill_name_frequency", y="skill_name_rank",
                 color="skill_name", size="skill_name_frequency")


app.layout = html.Div([
    html.H4("LinkedIn Skills Tracker"),
    html.H6("Industry Name"),
    html.Div(dcc.Dropdown(id='my-input',
                          options=option_array,
                          placeholder="Select a section"
                          )),
    html.Br(),
    html.Div(id='my-output'),
    dcc.Graph(id='scatter-plot', figure=fig),


])


@app.callback(
    Output(component_id='scatter-plot', component_property='figure'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    dff = df2
    skill_names = {}
    skill_name_ranks = {}
    count = 0
    if input_value == 'All':
        return px.scatter(df, x="skill_name_frequency", y="skill_name_rank",
                          color="skill_name", size="skill_name_frequency")
    for industry in dff['industry_name']:
        if industry == input_value:
            if dff['skill_group_name'][count] not in skill_names:
                skill_names[dff['skill_group_name'][count]] = 1
            else:
                skill_names[dff['skill_group_name'][count]] += 1
            if dff['skill_group_name'][count] not in skill_name_ranks:
                skill_name_ranks[dff['skill_group_name'][count]] = dff['skill_group_rank'][count]
            else:
                skill_name_ranks[dff['skill_group_name'][count]] += dff['skill_group_rank'][count]
        count += 1
    ranks = [] 
    for rank in skill_name_ranks:
        ranks.append(11 - skill_name_ranks[rank] / skill_names[rank])
    skills =list(skill_names.keys())
    data = {'skill_name': skills, 'skill_name_rank': ranks}
    print(skill_name_ranks)
    graphdf = pd.DataFrame.from_dict(data)
    return px.bar(graphdf, x="skill_name", y="skill_name_rank", color="skill_name")


if __name__ == '__main__':
    app.run_server(debug=True)

