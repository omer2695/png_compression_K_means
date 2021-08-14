from builtins import range
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from numpy import asarray
import random


def compress(image, result, k):
    image_as_array = asarray(image)
    x = type(image_as_array)
    num_of_rows = image_as_array.shape[0]
    num_of_cols = image_as_array.shape[1]
    if k is None:
        k = 5
    # returns an initial array of k random points
    k_means_array = get_k_points(image_as_array, k, num_of_rows, num_of_cols)
    # returns an array that maps each pixel point to a specific k-cluster.
    # each index in the array represents the same index in the image array and the value is the cluster.
    mapping_of_pixels_to_clusters, k_means_array = update_k_means(k_means_array, k, image_as_array, num_of_rows,
                                                                  num_of_cols)

    compressed_image = compress_image(mapping_of_pixels_to_clusters, k_means_array, num_of_rows,
                                      num_of_cols)  # returns the compressed image
    # saving the compressed image.
    plt.imsave('compressed_' + str(k) + '_colors.png', np.uint8(compressed_image))
    result[0] = 'compressed_' + str(k) + '_colors.png'


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


def distance_from_point_to_mean(First_point, Second_point):
    dist = 0
    size = len(First_point)
    for i in range(0, size):
        Color_from_first_point = First_point[i]
        Color_from_second_point = Second_point[i]
        temp = Color_from_first_point - Color_from_second_point
        dist += pow(temp,2)
    dist = np.sqrt(dist)
    return dist


def update_k_means(k_means_array, k, image_as_array, num_of_rows, num_of_cols):
    number_of_points = (num_of_rows * num_of_cols)

    k_means_index = np.zeros(number_of_points)

    k_means_index2 = np.zeros(number_of_points)

    k_means_index = k_means(k_means_array, k, image_as_array, num_of_rows, num_of_cols, k_means_index)

    new_k_means_array = cluster_average(k, image_as_array, num_of_rows, num_of_cols, k_means_index)

    k_means_index2 = k_means(new_k_means_array, k, image_as_array, num_of_rows, num_of_cols, k_means_index2)
    i = 0
    while i < 10:
        k_means_index = k_means_index2.copy()
        new_k_means_array = cluster_average(k, image_as_array, num_of_rows, num_of_cols,
                                            k_means_index)
        k_means_index2 = k_means(new_k_means_array, k, image_as_array, num_of_rows, num_of_cols, k_means_index2)

        i += 1
    return k_means_index2, new_k_means_array


def cluster_average(k, image_as_array, num_of_rows, num_of_cols, k_means_index):
    new_k_means_index = [[0 for x in range(3)] for y in range(k)]
    number_points_per_cluster = [0 for y in range(k)]
    for i in range(0, num_of_rows):
        for j in range(0, num_of_cols):
            convert_index_3D_to_2D = (i * num_of_cols) + j
            point_to_cluster_number = int(k_means_index[convert_index_3D_to_2D])
            new_k_means_index[point_to_cluster_number][0] += image_as_array[i][j][0]
            new_k_means_index[point_to_cluster_number][1] += image_as_array[i][j][1]
            new_k_means_index[point_to_cluster_number][2] += image_as_array[i][j][2]
            number_points_per_cluster[point_to_cluster_number] += 1

    for i in range(0, k):
        if number_points_per_cluster[i] != 0:
            new_k_means_index[i][0] = int(new_k_means_index[i][0] / number_points_per_cluster[i])
            new_k_means_index[i][1] = int(new_k_means_index[i][1] / number_points_per_cluster[i])
            new_k_means_index[i][2] = int(new_k_means_index[i][2] / number_points_per_cluster[i])
        else:
            new_k_means_index[i][0] = random.randrange(0, 255)
            new_k_means_index[i][1] = random.randrange(0, 255)
            new_k_means_index[i][2] = random.randrange(0, 255)
    return new_k_means_index


def k_means(k_means_array, k, image_as_array, num_of_rows, num_of_cols, k_means_index):
    for i in range(0, num_of_rows * num_of_cols):
        potential_short_distance_between_points = distance_from_point_to_mean(k_means_array[0],
                                                                              image_as_array[int(i / num_of_cols)][
                                                                                  (i % num_of_cols) - 1])

        for j in range(1, k):
            potential_short_distance_between_points2 = distance_from_point_to_mean(k_means_array[j],
                                                                                   image_as_array[int(i / num_of_cols)][
                                                                                       (i % num_of_cols) - 1])

            if potential_short_distance_between_points > potential_short_distance_between_points2:
                potential_short_distance_between_points = potential_short_distance_between_points2
                k_means_index[i] = j

    return k_means_index


def compress_image(mapping_of_pixels_to_clusters, k_means_array, num_of_rows, num_of_cols):
    image = [[[0 for x in range(3)] for y in range(num_of_cols)] for z in range(num_of_rows)]
    for row in range(0, num_of_rows):
        for column in range(0, num_of_cols):
            for rgb_color in range(0, 3):
                mapping_of_pixels_to_clusters = np.array(mapping_of_pixels_to_clusters, dtype=np.int)
                image[row][column][rgb_color] = \
                    k_means_array[mapping_of_pixels_to_clusters[row * num_of_cols + column]][rgb_color]

    return np.array(image)
