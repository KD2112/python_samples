
sales = [
    ("apple", 1),
    ("banana", 5),
    ("apple", 6),
    ("orange", 3),
    ("banana", 4),
    ("apple", 1),
]

class Inven:
    def __init__(self,item_dict):
        self.item=dict(item_dict)
    def __getitem__(self,item):
        return self.item.get(item,0)
    def __len__(self):
        return len(self.item)
    def __iter__(self):
        return iter(self.item)
    def __str__(self):
        sorted_item=sorted(self.item.items(),key=lambda x:x[1],reverse=True)
        lines=[f"{i}:{j}"for i,j in sorted_item]
        return "\n".join(lines)
    def __repr__(self):
        return f"Inventory({self.item})"


def summarize_sales(sale):
    sale_sum = {}

    for i,j in sale:
        sale_sum[i]=sale_sum.get(i,0)+j
   
    return list(sale_sum.items())

def sort(items):
    items=items[:]
    n=len(items)
    for i in range(n):
        for j in range(n - 1 -i):
            if items[j][1]<items[j+1][1]:
                  items[j], items[j + 1] = items[j + 1], items[j]

    return items

def main():
    sum_items=summarize_sales(sales)
    # print(sum_items)
    # items=sort(sum_items)
    # print(items)
    inv=Inven(sum_items)

    print(inv)
    print("\nAccess single item:")
    print("banana sold:", inv["banana"])

if __name__=="__main__":
    main()

