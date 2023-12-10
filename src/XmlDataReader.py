# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
from xml.etree import cElementTree


class XmlDataReader(DataReader):

    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = cElementTree.parse(path)
        root = tree.getroot()
        students_list = root.find("students")
        for student in students_list:
            self.students[student.attrib["name"]] = []
            subject_list = student.findall("subject")
            for subject in subject_list:
                subject_name = subject.attrib["name"]
                mark = subject.text
                (self.students[student.attrib["name"]]
                 .append((subject_name, int(mark))))
        return self.students
