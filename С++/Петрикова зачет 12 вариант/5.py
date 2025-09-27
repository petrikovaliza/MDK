def sort_shella(posled):
    count_element = len(posled)
    step = count_element // 2
    while step > 0:
        for i in range(step,count_element):
            j = i
            while j >= step and posled[j] < posled[j - step]:
                posled[j], posled[j - step] = posled[j - step], posled[j]
                j = j - step
        step = step // 2

spicochek = [5, 0, -2 , 7, 3]
print(spicochek)
sort_shella(spicochek)
print(spicochek)