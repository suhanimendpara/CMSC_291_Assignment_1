""""
File: assignment1.py
Author: Suhani Mendpara
Date: 02/04/2020
Section: 01
Email: mend1@umbc.edu
Description: This program takes in a file of body and brain weights of
various animals and calculates the mean, median, and standard deviation
of the weights.
"""
import math

BODY = 1
BRAIN = 2

def avg_num(data_list):
    """
    A function that will average a list of numbers.
    Preconditions:
    Postconditions:
    :param: data_list, list of data
    :return: integer, average number of list
    """
    # add up all the numbers in the list
    total = 0
    for item in range(0, len(data_list)):
        total = total + data_list[item]

    # divide by length of list to get average
    data_avg = total/len(data_list)
    return data_avg

def median_number (data_list):
    """
    A function that will find the median number in a list of numbers.
    Preconditions:
    Postconditions:
    :param: data_list - list of data
    :return: integer - median number of list
    """
    # if length is an even amount find the two middle index
    # add both middle index values and divide by 2
    length_data = len(data_list)
    if length_data % 2 == 0:
        median_1 = data_list[length_data // 2]
        median_2 = data_list[length_data //2 + 1]
        median_num = (median_1 + median_2) / 2
    # if length is odd, then middle index value is median value
    else:
        median_num = data_list[length_data // 2]
    return median_num

def standard_dev(data_list, avg_num):
    """
    A function that will find the standard deviation of a list of numbers.
    Preconditions:
    Postconditions:
    :param:  list of data either body or brain weights
    :param: float of average number
    :return: integer - standard deviation of list
    """
    # square of each value subtracted by the average number
    variance_list = []
    for item in data_list:
        variance_list.append((item - avg_num) ** 2 )

    # add each value together
    total = 0
    for item in range(0, len(variance_list)):
        total = total + variance_list[item]

    # divide sum by the total number of values and
    # square root that value
    std_num = math.sqrt(total/len(data_list))
    return std_num

def filter_body(data):
    """
    A function that will filter the 2D list for body weight.
    Preconditions:
    Postconditions:
    :param: data_list, 2D list of data
    :return: body_weight, list of body weights
    """
    # create a list of just body weight from 2D list
    index = 0
    body_weight = []
    while len(body_weight) < len(data):
        body_weight.append(float(data[index][BODY]))
        index += 1
    return body_weight

def filter_brain(data):
    """
    A function that will filter the 2D list for brain weight
    Preconditions:
    Postconditions:
    :param data_list, 2D list of data
    :return: brain_weight, list of brain weights
    """
    # create a list of brain weight from 2D list
    index = 0
    brain_weight = []
    while len(brain_weight) < len(data):
        brain_weight.append(float(data[index][BRAIN]))
        index += 1
    return brain_weight

def make_2D_list(filename):
    """
    A function that reads a file of data values and stores them in a list.
    Preconditions:
    Postconditions:
    :param: filename, a string filename
    :return: 2D list, a list of float values
    """

    # read all file values
    file_obj = open(filename)
    data = file_obj.readlines()
    file_obj.close()

    # convert file values to floats and store all in a list
    data_list = []
    index = 0
    while index < len(data):
        data_string = str(data[index])
        split_data = data_string.split(",")
        data_list.append(split_data)
        index += 1
    return data_list

if __name__ == '__main__':
    filename = "Sample-Data-Animal-Weights.csv"
    data_list = make_2D_list(filename)
    data_list.remove(data_list[0])             # removes the title line of the 2D list
    body_weight = filter_body(data_list)
    new_body_weight = body_weight.sort()       # shallow copy of sorted values to original list
    brain_weight = filter_brain(data_list)
    new_brain_weight = brain_weight.sort()     # shallow copy of sorted values to original list


    avg_body_weight = avg_num(body_weight)
    print("The average body weight is:", avg_body_weight)
    median_body = median_number(body_weight)
    print("The median body weight is:", median_body)
    stdev_body = standard_dev(body_weight, avg_body_weight)
    print("The standard deviation body weight is:", stdev_body)
    print()
    avg_brain_weight = avg_num(brain_weight)
    print("The average brain weight is:", avg_brain_weight)
    median_brain = median_number(brain_weight)
    print("The median brain weight is:", median_brain)
    stdev_brain = standard_dev(brain_weight, avg_brain_weight)
    print("The standard deviation brain weight is:", stdev_brain)



