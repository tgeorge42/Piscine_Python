def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    
    if (obj_type is type(None)):
        print("Nothing :", object, obj_type)
        return 0
    elif (obj_type is float and object != object):
        print("Cheese :", object, obj_type)
        return 0
    elif (obj_type is int and object == 0):
        print("Zero :", object, obj_type)
        return 0
    elif (obj_type is str and object == ''):
        print("Empty :", object, obj_type)
        return 0
    elif (obj_type is bool and object == False):
        print("Fake :", object, obj_type)
        return 0
    else:
        print("Type not Found")
        return 1
