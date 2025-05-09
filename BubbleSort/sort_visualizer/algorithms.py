from time import sleep


def bubble_sort(canvas, array, speed):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if not canvas.sorting:
                return
            canvas.highlight = {j: canvas.RED, j + 1: canvas.RED}
            canvas.repaint()
            sleep(speed)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            canvas.highlight = {}
    canvas.sorting = False