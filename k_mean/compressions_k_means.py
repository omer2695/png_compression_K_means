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
    # returns an initial array of k random points
    k_means_array = get_k_points(image_as_array, k, num_of_rows, num_of_cols)
    # returns an array that maps each pixel point to a specific k-cluster.
    # each index in the array represents the same index in the image array and the value is the cluster.
    mapping_of_pixels_to_clusters,k_means_array = update_k_means(k_means_array, k, image_as_array, num_of_rows, num_of_cols)
    compressed_image = compress_image(image_as_array,mapping_of_pixels_to_clusters,k_means_array,num_of_rows,num_of_cols) #returns the compressed image


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


def distance_from_point_to_mean(x1, y1, z1, x2, y2, z2):
    dist = np.square(x1 - x2) + np.square(y1 - y2) + np.square(z1 - z2)
    dist = np.sqrt(dist)
    return dist


def update_k_means(k_means_array, k, image_as_array, num_of_rows, num_of_cols):
    number_of_points = (num_of_rows * num_of_cols)
    k_means_index = np.zeros(number_of_points)
    k_means_index = k_means(k_means_array, k, image_as_array, num_of_rows, num_of_cols, k_means_index)
    k_means_index2 = k_means(k_means_array, k, image_as_array, num_of_rows, num_of_cols, k_means_index)
    while k_means_index != k_means_index2:
        k_means_index = k_means_index2
        k_means_index = k_means(k_means_array, k, image_as_array, num_of_rows, num_of_cols, k_means_index)
        k_means_index2 = k_means(k_means_array, k, image_as_array, num_of_rows, num_of_cols, k_means_index)


def cluster_average(k):
    print('ff')


def k_means(k_means_array, k, image_as_array, num_of_rows, num_of_cols, k_means_index):
    for i in range(0, num_of_rows * num_of_cols):
        potential_short_distance_between_points = distance_from_point_to_mean(k_means_array[0][0], k_means_array[0][1],
                                                                              k_means_array[0][2],
                                                                              image_as_array[int(i / num_of_cols)][
                                                                                  i % k - 1][0],
                                                                              image_as_array[int(i / num_of_cols)][
                                                                                  i % k - 1][1],
                                                                              image_as_array[int(i / num_of_cols)][
                                                                                  i % k - 1][2])

        for j in range(1, k):
            potential_short_distance_between_points2 = distance_from_point_to_mean(k_means_array[j][0],
                                                                                   k_means_array[j][1],
                                                                                   k_means_array[j][2],
                                                                                   image_as_array[int(i / num_of_cols)][
                                                                                       i % k - 1][0],
                                                                                   image_as_array[int(i / num_of_cols)][
                                                                                       i % k - 1][1],
                                                                                   image_as_array[int(i / num_of_cols)][
                                                                                       i % k - 1][2])

            if potential_short_distance_between_points > potential_short_distance_between_points2:
                potential_short_distance_between_points = potential_short_distance_between_points2
                k_means_index[i] = j

    return k_means_index


def compress_image(image_as_array, mapping_of_pixels_to_clusters, k_means_array, num_of_rows, num_of_cols):
    image = image_as_array
    for row in range(0, num_of_rows):
        for column in range(0, num_of_cols):
            for rgb_color in range(0, 3):
                image[row][column][rgb_color] = k_means_array[mapping_of_pixels_to_clusters][rgb_color]
    return image


if __name__ == "__main__":
    main()
