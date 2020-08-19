import csv, os, time
# gets files in a list
list = []
all_list = []
dict1 = {}
count_dict1 = {}
avg_dict = {}

# add all the files in a list
for root, dirs, files in os.walk('C:\\myproject'):
    for filename in files:
        list.append(filename)

# get the score number in csv file
for i in range(len(list)):
    with open("C:\\myproject\\" + list[i]) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2 and row[0] == 'Score:':
                score = float(row[1])
                # get time
                m_time = os.path.getmtime("C:\\myproject\\" + list[i])
                local_time = time.ctime(m_time)
                # convert time e.g. Sat Aug 15 2020
                time2 = local_time.split()
                del time2[3]
                
                #
                str1 = ' '.join(time2)
                if str1 not in all_list:
                    all_list.append(str1)
                    
                    # add score in dictionary
                    dict1[str1] = 0
                    sum1 = dict1[str1] + score
                    dict1[str1] = sum1
                    
                    count_dict1[str1] = 1
                else:
                    str1 = ' '.join(time2)
                    sum1 += score
                    dict1[str1] = sum1
                    
                    count = count_dict1[str1]
                    count += 1
                    count_dict1[str1] = count
                #
                break

# loop for average according to dates in all_list
for i in range(len(all_list)):
    avg = dict1[all_list[i]]/count_dict1[all_list[i]]
    avg_dict[all_list[i]] = avg

print(avg_dict)

# create csv file of average
with open(r"C:\Users\ToFoo\OneDrive\Desktop\average dictionary.csv", 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in avg_dict.items():
        writer.writerow([key, value])
   