import csv

# Read data from CSV file
def read_csv(filename):
    with open(filename, 'r') as file:
        return [{'name': row['name'], 'age': int(row['age']), 'grade': row['grade']}
                for row in csv.DictReader(file)]

# Main function
def main():
    filename = 'students.csv'
    students = read_csv(filename)

    # Data processing
    total_students = len(students)
    average_age = sum(student['age'] for student in students) / total_students
    oldest = max(students, key=lambda x: x['age'])
    youngest = min(students, key=lambda x: x['age'])

    # Results
    print(f"Total students: {total_students}")
    print(f"Average age: {average_age:.2f}")
    print(f"Oldest: {oldest['name']} (Age: {oldest['age']})")
    print(f"Youngest: {youngest['name']} (Age: {youngest['age']})")

if __name__ == '__main__':
    main()
