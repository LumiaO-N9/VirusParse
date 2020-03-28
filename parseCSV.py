import csv
from sqlalchemy.orm import sessionmaker
from db.initDB import VirusStatics, engine
from db.initChinaDB import ChinaVirusStatics

province = ["河北", "山西", "辽宁", "吉林", "黑龙江", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东",
            "海南", "四川", "贵州", "云南", "陕西", "甘肃", "青海", "台湾", "内蒙古", "广西", "西藏", "宁夏", "新疆", "北京", "天津", "上海", "重庆", "香港",
            "澳门", "台湾"]

path = r'C:\Users\zzk10\Documents\Ubuntu\Novel-Coronavirus-Updates\Updates_NC.csv'
DBSession = sessionmaker(bind=engine)
session = DBSession()
with open(path, encoding='utf8') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(list(headers))
    for row in f_csv:
        # print(f_csv.line_num, row)
        if len(row) == 11:
            print(row)
            report_date = row[0]
            region = row[1]
            city = row[2]
            new_confirm = 0
            new_cure = 0
            new_die = 0
            if row[3] != "":
                new_confirm = row[3]
            if row[4] != "":
                new_cure = row[4]
            if row[5] != "":
                new_die = row[5]
            message_source = row[6]
            source_url_one = row[7]
            source_url_two = row[8]
            source_url_three = row[9]
            note = row[10]
            virusStatic = VirusStatics(report_date=report_date,
                                       region=region,
                                       city=city,
                                       new_confirm=new_confirm,
                                       new_cure=new_cure,
                                       new_die=new_die,
                                       message_source=message_source,
                                       source_url_one=source_url_one,
                                       source_url_two=source_url_two,
                                       source_url_three=source_url_three,
                                       note=note
                                       )
            session.add(virusStatic)
            if row[1] in province:
                chinaVirusStatic = ChinaVirusStatics(report_date=report_date,
                                                     region=region,
                                                     city=city,
                                                     new_confirm=new_confirm,
                                                     new_cure=new_cure,
                                                     new_die=new_die,
                                                     message_source=message_source,
                                                     source_url_one=source_url_one,
                                                     source_url_two=source_url_two,
                                                     source_url_three=source_url_three,
                                                     note=note
                                                     )
                session.add(chinaVirusStatic)
    session.commit()
    session.close()
