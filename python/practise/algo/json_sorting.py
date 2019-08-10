json = [{id: '2','tags':[{'Key': 'Name','Value': 'Tag2'},{'Key': 'Role','Value': 'Publisher'},{'Key': 'Foo',        'Value': 'Bar'}]},
        {id: '1','tags':[{'Key': 'Name','Value': 'Tag1'},{'Key': 'Role','Value': 'Subscriber'},{'Key': 'Tao',
            'Value': 'Ching'}]}
        ]


'''Given the input JSON above, the output should look like this:

ID, NAME, ROLE

1, Tag1, Subscriber

2, Tag2, Publisher'''

#print(json[0])
# print(json[0][id])
# print(json[0]['tags'][0]['Value'])
# print(json[0]['tags'][1]['Value'])
# print('')
# print(json[1][id])
# print(json[1]['tags'][0]['Value'])
# print(json[1]['tags'][1]['Value'])


json_sorted = sorted(json,key=lambda x:x[id],reverse=False)

for element in json_sorted:
    print(element[id])

    for tags in element['tags']:

        if tags['Key'] =='Name':
            print(tags['Value'])

        elif tags['Key']=='Role':
            print(tags['Value'])


#time complexity = 0(n**2)  :/
