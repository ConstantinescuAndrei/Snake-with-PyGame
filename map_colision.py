from math import sqrt

maps = {
    "first_level": {
        "First wall": {
            "a": {
                "x": 100, 
                "y": 100,
            },
            "b":{
                "x": 100,
                "y": 200,
            },
            "c":{
                "x": 200,
                "y": 100
            },
        },
        "Second_wall": {
            "a": {
                "x": 100,
                "y": 400,
            },
            "b": {
                "x": 100,
                "y": 500,
            },
            "c": {
                "x": 200,
                "y": 500,
            }
        },
        "Third_wall":{
            "a":{
                "x": 700,
                "y": 100,
            },
            "b":{
                "x": 700,
                "y": 200,
            },
            "c":{
                "x": 600,
                "y": 100
            },
        },
        "Fourth_wall":{
            "a":{
                "x": 700,
                "y": 400,
            },
            "b":{
                "x": 700,
                "y": 500,
            },
            "c":{
                "x": 600,
                "y": 500,
            },
        },
    },
}



def distance(a,b):
    return sqrt((a["x"] - b["x"])**2 + (a["y"] - b["y"])**2)

def is_between(a,c,b):
    return distance(a,c) + distance(c,b) == distance(a,b)

def find_level(map_name, x, y):
    for key, value in maps.items():
        if key == map_name:
            return find_walls(maps[key], x, y)

def find_walls(walls, x, y):
    for key in walls.keys():
        if it_collide(walls[key], x, y):
            return True
    return False

def it_collide(points, x, y):
    head_point = {
        "x": x,
        "y": y
    }
    if is_between(points["a"], head_point, points["b"]):
        return True
    if is_between(points["a"], head_point, points["c"]):
        return True
    return False