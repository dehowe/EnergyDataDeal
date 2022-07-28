import os
import pandas as pd


def check_file_integrity(path):
    filenames = os.listdir(path)
    file_name_list=["qy1","fz1","xf1","qy2","fz2","xf2","qy3","fz3","xf3","qy4","fz4","xf4","qy5","fz5","xf5","qy6","fz6","xf6","mvb"]
    file_flag_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in filenames:
        file_name = i[0:3]
        #车厢1
        if(file_name=="qy1"):
            file_flag_list[0]=1
        elif(file_name=="fz1"):
            file_flag_list[1]=1
        elif(file_name=="xf1"):
            file_flag_list[2]=1
        # 车厢2
        elif(file_name=="qy2"):
            file_flag_list[3]=1
        elif(file_name=="fz2"):
            file_flag_list[4]=1
        elif(file_name=="xf2"):
            file_flag_list[5]=1
        # 车厢3
        elif(file_name=="qy3"):
            file_flag_list[6]=1
        elif(file_name=="fz3"):
            file_flag_list[7]=1
        elif(file_name=="xf3"):
            file_flag_list[8]=1
        # 车厢4
        elif(file_name=="qy4"):
            file_flag_list[9]=1
        elif(file_name=="fz4"):
            file_flag_list[10]=1
        elif(file_name=="xf4"):
            file_flag_list[11]=1
        # 车厢5
        elif(file_name=="qy5"):
            file_flag_list[12]=1
        elif(file_name=="fz5"):
            file_flag_list[13]=1
        elif(file_name=="xf5"):
            file_flag_list[14]=1
        # 车厢6
        elif(file_name=="qy6"):
            file_flag_list[15]=1
        elif(file_name=="fz6"):
            file_flag_list[16]=1
        elif(file_name=="xf6"):
            file_flag_list[17]=1
        elif (file_name == "mvb"):
            file_flag_list[18]=1

    for i in range(len(file_flag_list)):
        if file_flag_list[i]==0 and i!=18:
            #缺少除MVB以外文件
           file_flag = i % 3
           for j in range(6):
               if file_flag_list[file_flag+j*3] != 0:
                   copy_file_in=path+file_name_list[file_flag+j*3]+".csv"
                   copy_file_out=path+file_name_list[i]+".csv"
                   with open(copy_file_in) as csvfile:
                       data_csv = pd.read_csv(csvfile, header=None)
                   csvfile.close()
                   data_csv.columns = ['date', 'v', 'a', 'lei', 'zai', 'mileage', 'stop_num', 'accelerate']
                   data_csv['v']=0
                   data_csv['a']=0
                   data_csv['lei']=0
                   data_csv['zai']=0
                   data_csv['mileage']=0
                   data_csv['stop_num']=0
                   data_csv['accelerate']=0
                   data_csv.to_csv(copy_file_out, index=0, header=0)  # 导出解析结果，修改名称或路径
                   file_flag_list[i]=1
                   break
               else:
                   continue
        else:
            continue



path='D:\server\data_deal\缓存\\'
check_file_integrity(path)
