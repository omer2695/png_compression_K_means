import numpy as np
from PIL import Image
from numpy import asarray
import random


def main():
    image = Image.open("bird_small.png")
    image_as_array = asarray(image)
    num_of_rows = image_as_array.shape[0]
    num_of_cols = image_as_array.shape[1]
    k = 5
    k_means_array = get_k_points(image_as_array, k, num_of_rows, num_of_cols)
    # print(arr)
    k_means(k_means_array, k, image_as_array, num_of_rows, num_of_cols)


def get_k_points(image, k, num_of_rows, num_of_cols):
    array_of_numbers = []
    array_of_points = []
    while len(array_of_numbers) < k:
        row_number = random.randrange(0, num_of_rows)
        col_number = random.randrange(0, num_of_cols)
        if (row_number, col_number) not in array_of_numbers:
            array_of_points.append(image[row_number][col_number])
            array_of_numbers.append((row_number, col_number))
    return array_of_points


def min_distance_from_point_to_mean(x1, y1, z1, x2, y2, z2):
    dist = np.square(x1 - x2) + np.square(y1 - y2) + np.square(z1 - z2)
    dist = np.sqrt(dist)
    return dist


def k_means(k_means_array, k, image_as_array, num_of_rows, num_of_cols):
    number_of_points = (num_of_rows * num_of_cols)
    k_means_index = np.zeros(number_of_points)
    for i in range(0, num_of_rows * num_of_cols):
        potential_short_distance_between_points = min_distance_from_point_to_mean(k_means_array[0][0], k_means_array[0][1],
                                                           k_means_array[0][2],
                                                           image_as_array[int(i / num_of_cols)][i % k - 1][0],
                                                           image_as_array[int(i / num_of_cols)][i % k - 1][1],
                                                           image_as_array[int(i / num_of_cols)][i % k - 1][2])

        for j in range(1, k):
            potential_short_distance_between_points2 = min_distance_from_point_to_mean(k_means_array[j][0], k_means_array[j][1],
                                                                k_means_array[j][2],
                                                                image_as_array[int(i / num_of_cols)][i % k - 1][0],
                                                                image_as_array[int(i / num_of_cols)][i % k - 1][1],
                                                                image_as_array[int(i / num_of_cols)][i % k - 1][2])

            if potential_short_distance_between_points > potential_short_distance_between_points2:
                potential_short_distance_between_points = potential_short_distance_between_points2
                k_means_index[i] = j




if __name__ == "__main__":
    main()
