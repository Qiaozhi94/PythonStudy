import csv


def write_csv_demo():
    headers = {
        'username', 'age', 'height'
    }
    values = {
        ('张三', '19', '190'),
        ('李四', '26', '170'),
        ('王五', '50', '150')
    }
    with open('classroom.csv', 'w', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)

# <---------------分隔符----------------->

def write_csv_demo2():
    headers = [
        'username', 'age', 'height'
    ]
    values = [
        {'username':'张三','age':'19','height':'190'},
        {'username':'李四','age':'26','height':'170'},
        {'username':'王五','age':'50','height':'150'}
    ]
    with open('classroom2.csv','w',encoding='utf-8',newline='') as fp:
        writer = csv.DictWriter(fp,headers)
        # 写入表头数据的时候，需要调用writeheader方法
        writer.writeheader()
        writer.writerows(values)

if __name__ == '__main__':
    write_csv_demo()
if __name__ == '__main__':
    write_csv_demo2()