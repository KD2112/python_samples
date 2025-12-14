students = {
    "Alice Johnson": 88,
    "Brian Smith": 76,
    "Catherine Lee": 92,
    "David Brown": 67,
    "Emma Wilson": 81,
    "Frank Harris": 73,
    "Grace Martin": 95,
    "Henry Clark": 69,
    "Isabella Lewis": 84,
    "Jack Walker": 78,
    "Karen Young": 91,
    "Liam Hall": 82,
    "Mia Allen": 87,
    "Noah King": 74,
    "Olivia Wright": 89,
    "Paul Scott": 68,
    "Quinn Green": 93,
    "Rachel Adams": 77,
    "Samuel Baker": 85,
    "Tina Nelson": 72,
    "Uma Carter": 94,
    "Victor Mitchell": 79,
    "Wendy Perez": 83,
    "Xavier Roberts": 71,
    "Yara Turner": 90,
    "Zane Phillips": 75,
    "Aaron Campbell": 86,
    "Bella Parker": 80,
    "Caleb Evans": 92,
    "Diana Edwards": 78,
    "Ethan Collins": 88,
    "Fiona Stewart": 67,
    "George Sanchez": 91,
    "Hannah Morris": 84,
    "Ian Rogers": 73,
    "Julia Reed": 89,
    "Kyle Cook": 70,
    "Laura Morgan": 77,
    "Mason Bell": 82,
    "Nina Murphy": 94,
    "Owen Bailey": 69,
    "Piper Rivera": 87,
    "Reid Cooper": 90,
    "Sara Richardson": 76,
    "Tommy Cox": 85,
    "Ursula Howard": 93,
    "Violet Ward": 79,
    "Wyatt Torres": 81,
    "Zoe Peterson": 88
}

print(len(students))

filtered={k:v for k,v in students.items() if  50< v < 70}
print(len(filtered))

print("adding mark")

# add_mark={k+"_stud":v+5 for k,v in students.items()}
# for k,v in students.items():
#     k=k+"_stud"
# print(students)

stud2={"Ursula ": 93,
    "Violet ": 79,
    "Wyatt ": 81,
    "Zoe ": 88}


# for i,j in stud2.items():
#     students[i]=j 
students.update(stud2)
print("after update",len(students))

