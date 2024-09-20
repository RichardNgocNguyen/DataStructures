import random


def left(x):
    return 2 * x + 1


def right(x):
    return 2 * x + 2


def heapify(array, parent, heap_size=None):
    l = left(parent)
    r = right(parent)
    # Only needed for sorting the heap
    if heap_size is None:
        heap_size = len(arr)
    # comparison of heap_size for sorting
    # Checks if the left child of parent is smaller and sets smallest to that child
    if l < heap_size and array[l] < array[parent]:
        smallest = l
    # Else parent is still smaller and sets that as smallest
    else:
        smallest = parent
    # comparison of heap_size for sorting
    # Checks if the right child smaller by checking what set as smallest(parent or left child), and set as smallest
    if r < heap_size and array[r] < array[smallest]:
        smallest = r
    # If the smallest is not the parent, swap for the smallest(left child or right child)
    if smallest != parent:
        array[parent], array[smallest] = array[smallest], array[parent]
        # heapify to see if the smallest child should be pushed up the heap
        heapify(array, smallest, heap_size)


def build_heap(array):
    len_arr = len(array)
    # For loop with backward pointer that travels from the end to mid of list, and heapifies
    for i in range(len_arr // 2):
        x = ((len_arr // 2) - 1) - i
        heapify(array, x)


arr = [random.randint(0,500) for x in range(25)]
build_heap(arr)
print(arr)