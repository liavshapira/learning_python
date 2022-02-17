bricks_for_pigs=input("Enter three digits (each digit for one pig):")

bricks_per_pig1=int((int(bricks_for_pigs)/100))

bricks_per_pig2=int(( int(bricks_for_pigs) - bricks_per_pig1*100 )/10)

bricks_per_pig3= int(bricks_for_pigs) - bricks_per_pig1*100 - bricks_per_pig2*10

total_bricks=bricks_per_pig1 + bricks_per_pig2 + bricks_per_pig3
print (total_bricks)
print (int(total_bricks/3))
print (total_bricks%3)
print ( (total_bricks%3) == 0 )

