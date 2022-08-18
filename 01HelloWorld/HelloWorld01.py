import carla


try: 
    client = carla.Client("localhost", 2000)
    client.set_timeout(10)
    world = client.get_world()
    maps = client.get_available_maps()
    print(maps)
    world = client.load_world('Town05')
    world = client.load_world('Town04')
    
finally:
    print("all cleaned up.")