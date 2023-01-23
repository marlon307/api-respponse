def find_probabilities_box(
    nums: list[int],
    target: float,
    current_sum: float,
    current_combo: list[int],
    combos: list[list[int]],
):
    if current_sum >= target:
        combos.append(current_combo)
        return

    if current_sum > target:
        return

    for i in range(len(nums)):
        find_probabilities_box(
            nums[i + 1 :],
            target,
            current_sum + nums[i],
            current_combo + [nums[i]],
            combos,
        )


def cube_volumes(total_volume: float, boxes: list[int]):
    used_boxes = list()
    boxes.sort(reverse=True)

    maneger_volumes = total_volume
    check_update_box: int = boxes[0]
    for index, box in enumerate(boxes):
        if check_update_box != box and boxes[-index] >= maneger_volumes > 0:
            used_boxes.append(boxes[-index])
            maneger_volumes -= boxes[-index]
            break

        while maneger_volumes >= box:
            if check_update_box != box:
                check_update_box = box
                break

            used_boxes.append(box)
            maneger_volumes -= box

    if maneger_volumes > 0:
        boxes.sort()
        combos = []
        find_probabilities_box(boxes, maneger_volumes, 0, [], combos)

        combos.sort(key=lambda x: len(x))
        closest_to_zero = min(combos, key=lambda x: abs(sum(x) - maneger_volumes))

        used_boxes.extend(closest_to_zero)

    return used_boxes
