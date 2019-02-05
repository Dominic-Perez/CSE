world_map = {
    'R19A':

}


# Controller
current_node = world_map
directions = {"North", "South", "East", "West", "Up", "Down"}
playing = True

while playing:
   print(current_node["Name"])
    command = input(">_")
    if command in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
    room_name= current_node ['Paths'][command.upper]
    world_map[room_name]
   print("Command Not Recognized")