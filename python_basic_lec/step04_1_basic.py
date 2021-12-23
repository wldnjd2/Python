# /c/ProgramData/Anaconda3/python
# -*- coding: utf-8 -*-

# immutable or mutable
# immutable: int, float, bool, string, bytes, tuple, etc
# mutable: list, dict, set, bytearray, objects, functions, almost everything else

def list_a(var=[]):
    var.append(1)
    return var

def list_b(var=None):
    if var is None:
        var = []
    var.append(1)
    return var

if __name__ == "__main__":
    print(list_a()) # [1]
    print(list_a()) # [1, 1]
    print(list_a()) # [1, 1, 1]

    print(list_b()) # [1]
    print(list_b()) # [1]
    print(list_b()) # [1]



