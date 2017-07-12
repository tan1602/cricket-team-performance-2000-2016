import pandas as pd

team = pd.read_csv('teams.csv')

def get_performance(ds):
    print ("\nHere is the LIST of CAPTAINS happened during the period 2000-2016 \n")
    print (ds['CAPTAIN'])
    ch = raw_input("\n\nEnter Captian name to check teams performance:-")

    get = ds.CAPTAIN[ds.CAPTAIN == ch].index.tolist()
    index = get[0]
    curr = ds['PERFORMANCE'].iloc[index]
    pcap = ds['CAPTAIN'].iloc[index-1]
    span = ds['SPAN'].iloc[index]
    prev = 0
    if index > 0:
        prev = ds['PERFORMANCE'].iloc[index-1]

    print ("\nCaptain:-%s" % ch)
    print ("Span:-%s\n" % span)

    if prev == 0:
        print ('\n\nUnder Caption %s ,team performance is satisfactory i,e %d percent' % (ch, curr))

    if curr > prev and prev > 0:
        print ('Under Caption %s ,team performance is good i,e %d percent which is more than that of %s which was %d percent \n' % (ch, curr, pcap, prev))
        print ('That means winning rate is more in %s as compared to %s , So Change in Captaincy has a good impact on team performance' % (ch, pcap))

    if curr < prev and prev > 0:
        print ('Under Caption %s ,team performance is not good i,e %d percent which is less than that of %s which was %d percent \n' % (ch, curr, pcap, prev))
        print ('That means winning rate is less in %s as compared to %s , So Change in Captaincy has a bad impact on team performance' % (ch, pcap))


print(team)
i = pd.read_csv(raw_input("\nEnter team name as given in DATASET above:-") + '.csv')

get_performance(i)
