#Extract email data from file and sort base on hour the email was sent

file_name = input('Enter file name: ')
file_handle = open(file_name)

emails = dict()

for line in file_handle:         #Extracts hours email sent and places in dict()
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        hour_start = line.find(':') - 2
        hour = line[hour_start:(hour_start + 2)]
        emails[hour]= emails.get(hour,0) + 1        #Creates Histogram in dict()

list = []

for k,v in emails.items():                         #Takes k,v and places in list
    k_v = (k,v)
    list.append(k_v)

list.sort()

for k,v in list:
    print(k,v)
