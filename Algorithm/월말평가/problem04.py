import json


def turn(temperatures):
    pass
    # 여기에 코드를 작성합니다.
    maximum = []
    minimum = []
    temp_dict = {}
    for temp_list in temperatures:
        maximum.append(temp_list[0])
        minimum.append(temp_list[1])
    temp_dict['maximum'] = maximum
    temp_dict['minimum'] = minimum

    return temp_dict

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperatures = [
        [9, 3],
        [9, 0],
        [11, -3],
        [11, 1],
        [8, -3],
        [7, -3],
        [-4, -12]
    ]
    print(turn(temperatures)) 
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4], 
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }
