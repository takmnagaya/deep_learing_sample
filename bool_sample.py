hungry = True # お腹が減っているか
sleepy = False # 眠いか

print(type(hungry))
# >> <class 'bool'>

print(not hungry)
# >> False # hungryの否定

print(hungry and sleepy)
# >> False # 腹が減っているかつ眠い

print(hungry or sleepy)
# >> True # 腹が減っているまたは眠い

# if文
if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")


if sleepy:
    print("I'm sleepy")
else:
    print("I'm not sleepy")
