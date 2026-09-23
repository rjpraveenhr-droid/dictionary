D = {
    'I1': {
        'name': 'Arjun',
        'class': 'x',
        'Age': '15',
        'Subjects': ['Math', 'Science', 'English']
    },
    'I2': {
        'name': 'Dima',
        'class': 'x',
        'Age': '14',
        'Subjects': ['Math', 'Science', 'English']
    }
}

for k, v in D.items():
    print("Student Id :", k)
    print("Student details :")
    for k1, v1 in v.items():
        print(k1, ":", v1)