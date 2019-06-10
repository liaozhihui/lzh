# coding=utf-8

final_result=dict()

def sales_sum(pro_name):
    total=0
    nums=[]
    while True:
        x = yield
        print(pro_name+"销量:",x)

        if not x:
            break
        total+=x
        nums.append(x)
    return total,nums

def middle(key):
    while True:
        final_result[key]=yield from sales_sum(key)
        print(key+"销量统计完成")

def main():
    data_sets={
        "bobby牌面膜":[1200,1500,3000],
        "bobby牌手机":[28,55,98,108],
        "bobby牌大衣":[280,560,778,70]
    }
    for key ,data_set in data_sets.items():
        print("start key:",key)
        m = middle(key)
        m.send(None) #预激middle协程
        for value in data_set:
            m.send(value) #给协程传递每一组的值
        m.send(None)
    print("final_result",final_result)

if __name__ == '__main__':
    main()