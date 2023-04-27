#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    keys = set(boxes[0])  # start with the keys from the first box
    unlocked = {0}  # start with the first box unlocked

    while len(unlocked) < n:
        found_new_box = False
        for i in range(n):
            if i in unlocked:
                # this box is already unlocked, skip it
                continue
            if any(key in unlocked for key in boxes[i]):
                # we have a key for this box, unlock it and add its keys to our keyring
                unlocked.add(i)
                keys.update(boxes[i])
                found_new_box = True
        if not found_new_box:
            # we couldn't find any new boxes to unlock
            return False

    # we have unlocked all the boxes
    return True