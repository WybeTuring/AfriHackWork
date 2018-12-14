def sort_array(source_array):
    odd = []
    positions = []
    for i in range(0, len(source_array)):
        if ( source_array[i] % 2 != 0):
            odd.append(source_array[i])
            positions.append(i)
        odd.sort()
    for i in range(0,len(odd)):
        hold = positions[i]
        source_array[hold] = odd[i]
    return source_array
    