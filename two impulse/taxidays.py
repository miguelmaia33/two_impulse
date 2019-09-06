import csv

table = []
#temp = []
with open('taxi-data.csv','r') as tdata, open('taxi_days.csv','w', newline='') as t_days:
    reader=csv.reader(tdata)
    writer=csv.writer(t_days)
    rows=0
    for row in reader:
        table.append(row)
        rows+=1
    
#SubscriptionID -> 2; Quantity -> 7; QuantityDrop -> 28; %Active -> 36;
    #print(table[0])
        
    writer.writerow(['day', 'trips','passenger_count', 'trip_time_in_secs', 'trip_distance', 'fare_amount'])

    line=1
    days=0
    #firstIDPointer=line
    #print(table[line][6])
    while line<(rows):#limite rows-7
      total_fare=0
      passanger=0
      trip_time=0
      trip_distance=0
      trip=0
      while(trip_time<25200):#7h de trabalho em segundos
          total_fare=total_fare+float(table[line][6])
          passanger=passanger+int(table[line][2])
          trip_time=trip_time+int(table[line][3])
          trip_distance=round(trip_distance+float(table[line][4]))#dava casas decimais que nao devia
          trip=trip+1
          line=line+1
          if(line==rows):
              break
      days=days+1
      if(line==rows):
        writer.writerow([days, trip, passanger, trip_time, trip_distance, total_fare])
        break
      #print(trip_distance)
      writer.writerow([days, trip, passanger, trip_time, trip_distance, total_fare])
print('end')          
        
    
        

