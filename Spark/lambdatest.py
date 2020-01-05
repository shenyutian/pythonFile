def comp(x):
    return x["age"]


li = [{"age": 20, "name": "def"}, {"age": 25, "name": "abc"},
      {"age": 11, "name": "ghi"}]
# 排序操作
# li = sorted(li, key=comp)
# print(li)

li = sorted(li, key=lambda x: x["age"])
print(li)