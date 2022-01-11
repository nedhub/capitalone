def solution(matrix):
    sum_matrix = 0
    
    haunted_room = list()
    for i in range(0, len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                haunted_room.append(j)
        for k in range(len(matrix[0])):

            if k not in haunted_room:
                sum_matrix += matrix[i][k]

    return sum_matrix