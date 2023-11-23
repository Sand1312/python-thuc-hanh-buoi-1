num_of_store = int(input('Nhap tong so cua hang Mixue: '))
list_of_store = []
sum = 0
for i in range(num_of_store):
    element = int(input(f"Nhap doanh thu cua hang thu {i + 1}: "))
    list_of_store.append(element)
    sum+=element

max_index, max_value = max(enumerate(list_of_store), key=lambda x: x[1])
list_of_store.sort()
sum/=num_of_store

print(list_of_store)
print(f"Doanh thu trung binh cua cac cua hang Mixue: {int(sum)}")
print(f"Cua hang co doanh thu lon nhat la cua hang thu {max_index+1}")
