# -*- coding: utf-8 -*-
import argparse
import sys

from CalcBStudents import CalcBStudents
from CalcRating import CalcRating
from XmlDataReader import XmlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = XmlDataReader()
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    b_student_count = CalcBStudents(students).calc()
    print("B Students (all marks >= 76): ", b_student_count)


if __name__ == "__main__":
    main()
