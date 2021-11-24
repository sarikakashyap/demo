import requests
import pandas as pd

personal_token = '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'
HEADER = {'Authorization': f'{personal_token}'}

df = pd.DataFrame()
since_date = '2020-08-01'
until_date = '2021-08-10'
repo_name = 'Hashicorp/consul'
date_range_parameter = f'{since_date} to {until_date}'
org_dict = {'Misc': {'total_contributions': 0, 'unique_contributors': 0, "id": [], 'date_range_parameter': f'{date_range_parameter}'}}
n = 1
total_commits = 0
while True:
    info_url = f'https://api.github.com/repos/{repo_name}/commits?page={n}&per_page=100&since={since_date}&until={until_date}'
    commit_info = requests.get(info_url, HEADER).json()
    if commit_info:
        no_of_items = len(commit_info)
        #print(no_of_items)
        total_commits = total_commits + no_of_items
        #print("Total commits ", total_commits)
        #df=pd.DataFrame([commit_info])
        df = pd.concat([df,pd.DataFrame([commit_info])], ignore_index=True)
        n = n + 1
        #print(df.shape)
    else:
        print("Completed")
        break

data = df


for commit in data['commit']:
    email = commit['author']['email']
    email_end = email.split('@')
    company_name = email_end[1].rsplit('.', 1)  # Split into 2 from right to remove '.com'
    company = company_name[0].capitalize()  # Capitalize the company name

    # If the organization is users.noreply.github.com e.x. mikemorris@users.noreply.github.com, johncowen@users.noreply.github.com, gmail, yahoo id to Misc
    # For Total contributions, increase the count
    # For unique contributors, if email-id is in list, we will skip his commit i.e. multiple commits

    if company == 'Users.noreply.github' or company == 'Gmail' or company == 'Yahoo':
        org_dict['Misc']['total_contributions'] = org_dict['Misc']['total_contributions'] + 1
        if email not in org_dict['Misc']['id']:
            org_dict['Misc']['id'].append(email)  # org id List
            org_dict['Misc']['unique_contributors'] = org_dict['Misc']['unique_contributors'] + 1
            print(org_dict)
    # If organization is not users.noreply.github.com, make a new key as company name.
    else:
        if company in org_dict.keys():
            org_dict[company]['total_contributions'] = org_dict[company]['total_contributions'] + 1
        else:
            org_dict[company] = {'total_contributions': 1, 'unique_contributors': 0, 'id': [], 'date_range_parameter': f'{date_range_parameter}'}
        if email not in org_dict[company]['id']:
            org_dict[company]['id'].append(email)  # org id List
            org_dict[company]['unique_contributors'] = org_dict[company]['unique_contributors'] + 1
        print(org_dict)    

print("Output dictionary:")
print(org_dict)  # output dictionary