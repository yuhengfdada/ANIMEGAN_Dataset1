import os

j = 1
for i in range(1,37885):
    s1 = str(i).zfill(5)
    s2 = str(j).zfill(5)
    try:
        print('i= '+ str(i))
        os.rename('{}.jpg'.format(s1),'{}.jpg'.format(s2))
        j += 1
    except:
        print('skipped')