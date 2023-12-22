def float_and_int_count(nested_list):
    float_count = 0
    int_count = 0
    for l in nested_list:
        for item in l:
            if isinstance(item, int):
                int_count += 1
            elif isinstance(item, float):
                float_count += 1
    return float_count, int_count
if __name__ == '__main__':
    nested_list = [[3,4.0,2,8.4,6],[0,2,0.2,4,6],[9,3.5,0.32,5,4]]
    float_n, int_n = float_and_int_count(nested_list)
    print('Float count: {} \nInteger count: {}'.format(float_n, int_n))
    
    