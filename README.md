# courier_manage_algo
1. **conditions -> a->b(middle in the road),waiting on loacation b(empty) for next assignment, on the loaction b(unloading) dont knopw about the time.**

<br/>

2. **Trucks/Carrier in the system(unique no,type(v1,v2,v3,v4,v5),rate on carriers{wrt},montly cycle{start date ,end date},minimum km Guranteee , if exceed ->after this 20% increase on algo)**

<br/>

** e.g.
i) After 4000 KM for L1 ( between time period 8th to 7th its price ) the price per KM is 36 INR per KM. During period (8th March to 7th April) lets say by 4th April,
L1 has already run 4000 KM and now on 4th April there is an assignment request of Load where it has to cover 600 KM which means by 7th April the L1 price ideally will be 4000 * 30 + 600 * 36 = 141,600 INR

ii) L2 (period 15th March to 14th April) , its doing unloading at a location and we dont know how much time its going to unload , so that we can assign it the next assignment. It has run 2700KM so far Ideally if it gets picked the price will be 76,000 . This is Low but it has still 10 days left in its cycle. Should you pick or not ?      

iii) Now if we have any other Load Carrier available on a location L5 whose minimum KM run is 3600KM, per KM rate is 22 KM , its cycle is (6th March to 5th April), but it has run 3100 KM so far , ideally this should be picked. why because
total KM run 3100 + 600 = 3700 KM price is 3600 * 22 = 77,000 + extra KM (100 * (22 + 20%22) ) = 81,840 and its cycle is getting ended next day, so utilize it.**