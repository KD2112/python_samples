records = [
    ("alice", "math", 80),
    ("bob", "math", 70),
    ("alice", "science", 90),
     ("alice", "science", 40),
    ("bob", "science", 60),
    ("charlie", "math", 50),
    ("alice", "english", 85),
]

class Gradebook:
    def __init__(self,avg_list):
        self.avg=dict(avg_list)
    def __getitem__(self,name):
        return self.avg.get(name,0)
    def __str__(self):
        sort_item=sorted(self.avg.items(),key=lambda mark_list:mark_list[1],reverse=True)
        lines=[f"{i}:{j}"for i,j in sort_item]
        return "\n".join(lines)




def group_mark(rec):
    mark={}
    for name,subj,marks in rec:
        if name not in mark:
            mark[name]={}
        if subj not in mark[name]:
            mark[name][subj]=[]
            mark[name][subj].append(marks)
    return mark



def compute_avg(mark_list):
    avg_list={}
    # for i,j in mark_list.items():
    #     avg=sum(j)/len(j)
    #     avg_list[i]=avg
    for name,subjects in mark_list.items():
        avg_list[name]={}
        for subj,marks in subjects.items():
            avg=sum(marks)/len(marks)
            avg_list[name][subj]=avg
    return avg_list
        
stud_list=group_mark(records)
print(stud_list)
avg_list=compute_avg(stud_list)
print(avg_list)
# gb=Gradebook(records)
# # print(avg_list)
# print(gb)