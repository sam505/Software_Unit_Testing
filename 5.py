height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # height list

left, right = 0, len(height) - 1  # left and right pointer
left_max, right_max = 0, 0
capacity = 0

# t_max: to store the maximum amount of water that can be trap between any two peaks.
t_max = 0
# to store from which side are we coming, f=0: for left side
# f=1: for right side
f = -1
while left < right:
    if height[left] < height[right]:
        if height[left] >= left_max:
            left_max = height[left]
        else:
            capacity += left_max - height[left]
        # checking if we are coming from right side
        if f == 1:
            # updating t_max if less than capacity
            if t_max < capacity:
                t_max = capacity
            capacity = 0
        f = 0
        left += 1

    else:
        if height[right] >= right_max:
            right_max = height[right]
        else:
            capacity += right_max - height[right]
        # checking if we are coming from left side
        if f == 0:
            # updating t_max if less than capacity
            if t_max < capacity:
                t_max = capacity
            capacity = 0
        f = 1
        right -= 1
if t_max < capacity:
    t_max = capacity
print(t_max)
