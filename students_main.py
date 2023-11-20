import students

def main():
    me = students.Student(23123, 'Yoel')
    class_1 = students.Course('GCIS-123', 4, 'A')
    class_2 = students.Course('UWRT-150', 3, 'B')
    me.print()
    class_1.print()
    class_2.print()

    me.add_course(class_1)
    me.add_course(class_2)

    print(me.get_gpa())

if __name__ == "__main__":
    main()