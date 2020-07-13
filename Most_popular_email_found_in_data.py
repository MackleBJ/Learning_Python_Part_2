#Extract email addresses from email data & determine who sent the most emails

file_name = input('Enter file name: ')   #Requests file to open
file_handle = open(file_name)            #Opens file entered

emails = dict()                           #var to track number of lines with 'From'

for line in file_handle:
    if line.startswith('From:'):         #We don't want 'From:' lines, just 'From'
        continue
    elif line.startswith('From'):
        line_data = line.split()
        emails[line_data[1]] = emails.get(line_data[1],0) + 1    #Email Histogram

pop_email = None
emails_sent = None

for email,sent in emails.items():        #Pulls info from dict() & and remembers the largest
    if emails_sent is None or sent > emails_sent:
        pop_email = email
        emails_sent = sent

print(pop_email, emails_sent)
