import numpy as np


def get_surrounding_fields(current_entry: dict):
    surrounding_fields_to_consider = []
    if not current_entry.get("row") - 1 < 0:
        surrounding_fields_to_consider.append("top")
    if not current_entry.get("row") + 1 > 99:
        surrounding_fields_to_consider.append("bottom")
    if not current_entry.get("col") - 1 < 0:
        surrounding_fields_to_consider.append("left")
    if not current_entry.get("col") + 1 > 99:
        surrounding_fields_to_consider.append("right")
    return surrounding_fields_to_consider


def get_matrix_indices(current_entry, surrounding_fields_to_consider):
    matrix_indices = []
    if "left" in surrounding_fields_to_consider:
        matrix_indices.append([current_entry.get("row"), current_entry.get("col") - 1])
    if "right" in surrounding_fields_to_consider:
        matrix_indices.append([current_entry.get("row"), current_entry.get("col") + 1])
    if "top" in surrounding_fields_to_consider:
        matrix_indices.append([current_entry.get("row") - 1, current_entry.get("col")])
    if "bottom" in surrounding_fields_to_consider:
        matrix_indices.append([current_entry.get("row") + 1, current_entry.get("col")])
    i = [x[0] for x in matrix_indices]
    j = [x[1] for x in matrix_indices]
    return i, j


def task1():
    matrix = read_input()
    risk_level = 0
    for row_idx in range(matrix.shape[0]):
        for col_idx in range(matrix.shape[1]):
            current_entry = {"row": row_idx, "col": col_idx}
            surrounding_fields = get_surrounding_fields(current_entry)
            i, j = get_matrix_indices(current_entry, surrounding_fields)
            selected_value = matrix[row_idx, col_idx]
            surrounding_values = matrix[i, j]
            if all(selected_value < surrounding_values):
                risk_level += (1 + selected_value)
    print(risk_level)


def task2():
    matrix = read_input()
    bool_matrix = matrix < 9
    components = {}
    already_labeled = []
    queue = []
    curr_label = 1
    for row_idx in range(matrix.shape[0]):
        for col_idx in range(matrix.shape[1]):
            midx = matrix_idx(row_idx, col_idx, bool_matrix.shape[0])
            if bool_matrix[row_idx, col_idx] and not midx in already_labeled:
                already_labeled.append(midx)
                if components.get(curr_label):
                    components[curr_label].append(midx)
                else:
                    components[curr_label] = [midx]
                queue.append(midx)

                if queue:
                    queue = go_deep(queue)


def go_deep(queue):



def matrix_idx(row, col, length):
    return (row * length) + col

def read_input():
    with open("input.txt") as file:
        input = np.array(list(map(lambda x: [int(y) for y in x], [list(line.strip()) for line in file.readlines()])))
        return input


if __name__ == "__main__":
    task1()
    task2()
