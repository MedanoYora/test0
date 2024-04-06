count_buildings=4
time=24
building_time=10
farm= 3
k=0
while time==0:
    resours_result=count_buildings*farm
    resours=resours+resours_result
    time=-1
    k=+1
    if k==10:
        k=0
        count_buildings=+1
print(resours)