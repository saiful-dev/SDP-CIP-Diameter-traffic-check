import pandas as pd
file_open=open('PSC-CIPDiameter_8.1_A_1.stat.0','r')

file_read=file_open.read()
file_write=open('last_traffic_value','a');
arr=file_read.split("Detected   Answered    (/s)    Avg    Min    Max")
print(len(arr))
#file_write.write("								Succ    Fail  Timeout  Reject Retransmission  Duplicate")
file_write.write(arr[len(arr)-1])

print('-----------------pandas--------');

file_open.close()
file_write.close()


#df =pd.read_csv('last_traffic_value',names=['date','type','Succ','Fail','Timeout','Reject' ,'Retransmission', 'Duplicate','throuput','RA','RMin','Rmax'])
#df.columns=['date','type','Succ','Fail','Timeout','Reject' ,'Retransmission', 'Duplicate','throuput','RA','RMin','Rmax']

print('-----------------pandas columns--------');









