def function(li):
    max_sum = li[0]
    tmp_sum = 0
    start_index = 0
    end_index = 0
    for i in range(len(li)):
        if tmp_sum < 0:
            tmp_sum = li[i]
            start_index = i
        else:
            tmp_sum += li[i]
        if tmp_sum > max_sum:
            end_index = i
            max_sum =  tmp_sum
    print(max_sum)
    print(li[start_index:end_index+1])
    return max_sum


if __name__ == "__main__":
    li = [2, 1, -1, 3, 4, -5]
    function(li)
