def find_probabilities_box(
    nums: list[dict],
    target: float,
    current_sum: float,
    current_combo: list[dict],
    combos: list[list[dict]],
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
            current_sum + nums[i]["vol"],
            current_combo + [nums[i]],
            combos,
        )


def cube_volumes(total_volume: float, boxes: list[dict], weight: float):
    used_boxes = list()
    boxes.sort(key=lambda x: x["vol"], reverse=True)
    check_update_box: int = boxes[0]["vol"]

    for index, box in enumerate(boxes):
        if check_update_box != box["vol"] and boxes[-index]["vol"] >= total_volume > 0:
            used_boxes.append(boxes[-index])
            total_volume -= boxes[-index]["vol"]
            break

        while total_volume >= box["vol"]:
            if check_update_box != box["vol"]:
                check_update_box = box["vol"]
                break
            used_boxes.append(box)
            total_volume -= box["vol"]

    if total_volume > 0:
        boxes.sort(key=lambda x: x["vol"])
        combos = list()
        find_probabilities_box(boxes, total_volume, 0, [], combos)

        combos.sort(key=lambda x: len(x))
        closest_to_zero = min(
            combos, key=lambda x: abs(sum(map(lambda b: b["vol"], x)) - total_volume)
        )
        used_boxes.extend(closest_to_zero)

    weight_box = weight / len(used_boxes)
    used_boxes = map(lambda b: {**b, "weight": weight_box}, used_boxes)

    return list(used_boxes)
