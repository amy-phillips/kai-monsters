import random
f={1:1,
   2:25,
   3:12,
   4:11,
   5:6,
   }
totals = {}
for a in range(1,41) :
    totals[a] = 0
probability={}
for a in range(1,41) :
    probability[a] = 0
probability[1] = 1
moves=100
newprobability={}
for a in range(1,41) :
    newprobability[a] = 0
while moves>0:
    for a in range(1,41):
        for b in range(2,13):
            c=a+b
            if c>40:
                c= c-40
            if c==31:
                c=11
            if c==8 or c==23 or c==37:
                d=random.randint(1,14)
                if d<6:
                    c=f[d]
                elif d==6:
                    if c>13:
                        c=29
                    else:
                        c=13
                elif d==7:
                    if c==8:
                        c=16
                    if c==23:
                        c=26
                    if c==37:
                        c=6
                elif d==8:
                    c=c-3
            if c==18 or c==34 or c==3:
                d=random.randint(1,33)
                if d==1 or d==2:
                    c=1
                if d==3 or d==4:
                    c=11
            newprobability[c]+=probability[a]*(6-(((7-b)**2)**0.5))/36
            totals[c]+=newprobability[c]
    for a in range(1,41):
        probability[a]=newprobability[a]
        newprobability[a]=0
    moves-=1

for a in range(1,41):
    print(f"square {a} = {probability[a]}      {totals[a]}")
print("after 30 moves these are how much each set made")
print("brown properties made £"+str(totals[2]*250+totals[4]*450),"light blue properties made £"+str(totals[7]*550+totals[9]*550+totals[10]*600))
print("pink properties made £"+str(totals[12]*450+totals[14]*450+totals[15]*500)+" orange properties made £"+str(totals[17]*550+totals[19]*550+totals[20]*600))
print("red properties made £"+str(totals[22]*700+totals[24]*700+totals[25]*750)+" yellow properties made £"+str(totals[27]*800+totals[28]*800+totals[30]*850))
print("green properties made £"+str(totals[32]*900+totals[33]*900+totals[35]*1000)+" dark blue properties made £"+str(totals[38]*1100+totals[40]*1400))
