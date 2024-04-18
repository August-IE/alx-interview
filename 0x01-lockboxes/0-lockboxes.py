#!/usr/bin/python3
'''A function that unlocks lockboxes.
'''


def canUnlockAll(boxes):
    '''A method that determines if all boxes can be unlocked
    '''
    n = len(boxes)
    seen_boxes = {0}
    unseen_boxes = set(boxes[0]) - {0}
    while unseen_boxes:
        boxIdx = unseen_boxes.pop()
        if boxIdx not in range(n):
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes |= set(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return len(seen_boxes) == n
