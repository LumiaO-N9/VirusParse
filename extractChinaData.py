import csv

province = ["河北", "山西", "辽宁", "吉林", "黑龙江", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东",
            "海南", "四川", "贵州", "云南", "陕西", "甘肃", "青海", "台湾", "内蒙古", "广西", "西藏", "宁夏", "新疆", "北京", "天津", "上海", "重庆", "香港",
            "澳门", "台湾"]

source_file = r'C:\Users\zzk10\Documents\Ubuntu\Novel-Coronavirus-Updates\Updates_NC.csv'
new_file = r'C:\Users\zzk10\Documents\Ubuntu\Novel-Coronavirus-Updates\Updates_NC_China.csv'

with open(source_file, encoding='utf8') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(list(headers))
    with open(new_file, 'w', encoding='utf8', newline='') as new_csv:
        writer = csv.writer(new_csv)
        writer.writerow(list(headers))
        for row in f_csv:
            if row[1] in province:
                writer.writerow(row)
