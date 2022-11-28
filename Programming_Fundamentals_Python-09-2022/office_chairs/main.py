total_chairs = 0
total_visitors = 0
enough_chairs = True

number_of_rooms = int(input())
rooms = [input().split(' ') for _ in range(number_of_rooms)]
for i in range(len(rooms)):
    room = rooms[i]
    chairs = len(room[0])
    total_chairs += chairs
    visitors = int(room[1])
    total_visitors += visitors
    if visitors > chairs:
        enough_chairs = False
        print(f"{visitors - chairs} more chairs needed in room {i + 1}")

if enough_chairs:
    print(f"Game On, {total_chairs - total_visitors} free chairs left")
