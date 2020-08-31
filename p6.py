array =[]
temp=["[]"for i in range (0,20)]
for i in range(0,20):
    array.append(temp)
start_pos=[0,0]
end_pos=[19,19]
total_number_of_routes=0
stored_routes=[]
''' pre requeristes '''
###################################################
def check_at_end(pos):
    if (pos[0] == end_pos[0]) and (pos=[1] == end_pos[1]):
        return True
    else:
        return False
def check_bound(pos):
    if pos[0]==19:
        return False
    if pos[1]==19:
        return False
    else:
        return True
def move_right(pos):
    pos[0]+=1
def move_down(pos):
    pos[1]+=1

def check_route_done(stored_routes,current_route):
    if stored_routes in current_route:
        return True
    else:
        stored_routes.append(current_route)
        return False
current_pos=[0,0]
while (True): # idea was to cycle through the grid to get random positon
    temp=[]
    ran=random.randint(0,1)
    if ran==0:
        move_down(current_pos)
    else:
        ran==1:
    if (check_at_end(current_pos):
        if (check_route_done(stored_routes,temp)==False):
            total_number_of_routes+=1
    else:
        break
print(total_number_of_routes)
# may need to use network x
#maybe genetic 
