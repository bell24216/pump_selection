from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse,JsonResponse
import pandas as pd
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
import mysql.connector
import numpy as np
import io
from pumpselection.view.kdin import loaddata_kdin
from pumpselection.view.kiso1 import loaddata_kiso
from pumpselection.view.kiso2 import loaddata_kiso_two
from pumpselection.view.kop import loaddata_kop9196
from pumpselection.view.max import loaddata_max3
from pumpselection.view.load_excel import update_data_excel
import xlrd
from django.db.models import Q
import requests
from database.forms import SQLFileSearchForm
from database.models import SQLFile
import openpyxl
from django.contrib import messages
import matplotlib.pyplot as plt
from pumpselection.view.connectDB import mydb
from pumpselection.view.showchart import chart_kdin




def my_view(request):
    if request.method == 'POST':
            model = request.POST.get('model')
            fflow = request.POST.get('fflow')
            hhead = request.POST.get('hhead')
            fflow = float(fflow)
            hhead = float(hhead)
            # print(model, type(model))
            # print(fflow, type(fflow))
            # print(hhead, type(hhead))
            if model == 'kdin':
                dfkdin = pd.read_sql(
                    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,se_quence,eff_rl FROM factory_table_off where model_short = "KDIN"', con=mydb)
                output = [
                     loaddata_kdin('FAC-0001', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0002', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0003', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0004', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0005', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0006', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0007', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0008', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0009', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0010', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0011', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0012', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0013', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0014', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0015', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0016', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0017', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0018', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0019', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0020', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0021', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0022', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0023', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0024', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0025', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0026', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0027', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0028', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0029', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0030', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0068', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0069', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0070', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0071', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0072', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0073', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0074', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0075', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0076', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0077', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0078', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0079', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0080', fflow, hhead,dfkdin),
                # loaddata_kdin('FAC-0081', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0082', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0083', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0084', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0085', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0086', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0087', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0088', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0089', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0090', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0091', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0092', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0093', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0094', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0095', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0096', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0097', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0098', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0099', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0100', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0101', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0102', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0103', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0104', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0105', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0106', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0107', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0108', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0109', fflow, hhead,dfkdin),

                loaddata_kdin('FAC-0158', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0160', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0161', fflow, hhead,dfkdin),

                loaddata_kdin('FAC-0164', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0170', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0172', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0174', fflow, hhead,dfkdin),
                loaddata_kdin('FAC-0256', fflow, hhead,dfkdin),
                ]

                names = [output_val[0][0]for output_val in output if output_val is not None ]
                im_size = [output_val[1] for output_val in output if output_val is not None ]
                eff = [output_val[2] for output_val in output if output_val is not None ]
                power = [output_val[3] for output_val in output if output_val is not None ]
                yt = [output_val[4] for output_val in output if output_val is not None ]
                chart = [output_val[5] for output_val in output if output_val is not None ]

                context = {
                    'model': model,
                    'fflow': fflow,
                    'hhead': hhead,
                    'names': names,
                    'im_size': im_size,
                    'eff': eff,
                    'power': power,
                    'yt': yt,
                    'chart': chart,                    
                    'model':model,
                    'fflow':fflow,
                    'hhead':hhead,
                }   
            elif model =='kiso':
                dfkiso = pd.read_sql(
                    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,se_quence,eff_rl FROM factory_table_off where model_short = "KISO"', con=mydb)
                output = [
                loaddata_kiso('FAC-0031', fflow, hhead,dfkiso),
                loaddata_kiso('FAC-0032', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0033', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0034', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0035', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0036', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0037', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0038', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0039', fflow,hhead,dfkiso),

                loaddata_kiso_two('FAC-0040', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0041', fflow,hhead,dfkiso),
                # loaddata_kiso_two('FAC-0042', fflow,hhead,55,56,30,dfkiso), กราฟ eff ไม่มี
                loaddata_kiso_two('FAC-0043', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0044', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0045', fflow,hhead,dfkiso),
                # loaddata_kiso_two('FAC-0046', fflow,hhead,55,56,30,dfkiso), flow ไม่มี
                loaddata_kiso_two('FAC-0047', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0048', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0049', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0050', fflow,hhead,dfkiso),

                loaddata_kiso_two('FAC-0051', fflow,hhead,dfkiso),
                loaddata_kiso_two("FAC-0052", fflow, hhead, dfkiso),
                loaddata_kiso_two('FAC-0053', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0054', fflow,hhead,dfkiso),

                loaddata_kiso_two('FAC-0055', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0056', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0057', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0058', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0059', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0060', fflow,hhead,dfkiso),
                loaddata_kiso_two('FAC-0061', fflow,hhead,dfkiso),
                # loaddata_kiso('FAC-0062', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0063', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0064', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0065', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0066', fflow,hhead,dfkiso),
                loaddata_kiso('FAC-0067', fflow,hhead,dfkiso),


                ]
                names = [output_val[0][0]for output_val in output if output_val is not None ]
                im_size = [output_val[1] for output_val in output if output_val is not None ]
                eff = [output_val[2] for output_val in output if output_val is not None ]
                power = [output_val[3] for output_val in output if output_val is not None ]
                yt = [output_val[4] for output_val in output if output_val is not None ]
                chart = [output_val[5] for output_val in output if output_val is not None ]


                context = {
                    'model': model,
                    'fflow': fflow,
                    'hhead': hhead,
                    'names': names,
                    'im_size': im_size,
                    'eff': eff,
                    'power': power,
                    'yt': yt,
                    'chart': chart,
                    'model':model,
                    'fflow':fflow,
                    'hhead':hhead
                }   
            elif model == 'kop9196':
                dfkop9196 = pd.read_sql(f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,se_quence,eff_rl FROM factory_table_off where model_short = "KOP9196"', con=mydb)
                output = [ 
                    loaddata_kop9196('FAC-0110',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0111',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0112',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0114',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0115',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0116',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0117',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0118',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0119',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0120',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0121',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0122',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0123',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0124',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0125',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0126',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0127',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0128',fflow,hhead,dfkop9196),
                    # loaddata_kop9196('FAC-0129',16,16,dfkop9196), เส้น nhspr ไกลเกิน
                    loaddata_kop9196('FAC-0130',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0131',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0132',fflow,hhead,dfkop9196),  
                    loaddata_kop9196('FAC-0133',fflow,hhead,dfkop9196),
                    # loaddata_kop9196('FAC-0134',fflow,hhead,dfkop9196), 
                    loaddata_kop9196('FAC-0135',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0136',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0137',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0138',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0139',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0140',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0141',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0142',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0143',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0144',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0145',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0146',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0147',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0148',fflow,hhead,dfkop9196),
                    # loaddata_kop9196('FAC-0149',fflow,hhead,dfkop9196),
                    # loaddata_kop9196('FAC-0150',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0151',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0152',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0153',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0154',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0155',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0156',fflow,hhead,dfkop9196),
                    loaddata_kop9196('FAC-0157',fflow,hhead,dfkop9196),
                ]
                names = [output_val[0][0]for output_val in output if output_val is not None ]
                im_size = [output_val[1] for output_val in output if output_val is not None ]
                eff = [output_val[2] for output_val in output if output_val is not None ]
                power = [output_val[3] for output_val in output if output_val is not None ]
                yt = [output_val[4] for output_val in output if output_val is not None ]
                chart = [output_val[5] for output_val in output if output_val is not None ]


                context = {
                    'model': model,
                    'fflow': fflow,
                    'hhead': hhead,
                    'names': names,
                    'im_size': im_size,
                    'eff': eff,
                    'power': power,
                    'yt': yt,
                    'chart': chart,
                    'model':model,
                    'fflow':fflow,
                    'hhead':hhead
                }   
            elif model == 'max3':
                dfmax = pd.read_sql(
                    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,se_quence,eff_rl FROM factory_table_off ', con=mydb)
                output = [ 
                    loaddata_max3('FAC-0159',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0166',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0167',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0175',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0176',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0178',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0179',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0180',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0181',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0182',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0183',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0184',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0185',fflow,hhead,dfmax),

                    loaddata_max3('FAC-0230',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0231',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0232',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0233',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0234',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0235',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0236',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0237',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0238',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0239',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0240',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0241',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0242',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0243',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0244',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0245',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0246',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0247',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0248',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0249',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0250',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0251',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0252',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0253',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0254',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0255',fflow,hhead,dfmax),
                    loaddata_max3('FAC-0229',fflow,hhead,dfmax),
                ]
                names = [output_val[0][0]for output_val in output if output_val is not None ]
                im_size = [output_val[1] for output_val in output if output_val is not None ]
                eff = [output_val[2] for output_val in output if output_val is not None ]
                power = [output_val[3] for output_val in output if output_val is not None ]
                yt = [output_val[4] for output_val in output if output_val is not None ]
                chart = [output_val[5] for output_val in output if output_val is not None ]


                context = {
                    'model': model,
                    'fflow': fflow,
                    'hhead': hhead,
                    'names': names,
                    'im_size': im_size,
                    'eff': eff,
                    'power': power,
                    'yt': yt,
                    'chart': chart,
                    'model':model,
                    'fflow':fflow,
                    'hhead':hhead
                }   
            return render(request, 'my_template.html',context)

    else:
        return render(request, 'my_template.html')


def read_table(request):
    data_table = pd.read_sql('SELECT fac_number, equipment, brand, model_short, model, rpm FROM factory_table GROUP BY fac_number' , con=mydb)
    
    return render(request, 'table.html', {'data_table': data_table})

def show_details(request, fac_number):

    factory = pd.read_sql(f"SELECT fac_number,model_short,data_type,rpm,imp_dia,flow,head,eff,npshr,kw,model,se_quence,eff_rl FROM factory_table WHERE fac_number = '{fac_number}' ", con=mydb)

    try:
        im_size_lst = (factory.query(f"data_type == 'QH' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())
        eff_size_lst = (factory.query(f"fac_number == '{fac_number}' and eff_rl !=''")["eff_rl"].unique().tolist())
        kw_size_lst = (factory.query(f"data_type == 'KW' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())
        npshr_size_lst = (factory.query(f"data_type == 'NPSHR' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())
        chart = chart_kdin(fac_number,im_size_lst,kw_size_lst,eff_size_lst,npshr_size_lst)
    except:
        chart = None
    

    factory.fillna('', inplace=True)
    # หากไม่มีข้อมูล ส่งข้อความแจ้งเตือนกลับไปยังเทมเพลต
    return render(request, 'details.html', {'factory': factory,'chart':chart})

def read_user(request):
    user_table = pd.read_sql('SELECT user_name,user_password,status,fname,lname,company_name FROM user_table' , con=mydb)

    return render(request, 'user_table.html', {'user_table': user_table})

def show_details_user(request, user_name):

    user_table = pd.read_sql(f"SELECT user_name,user_password,status,fname,lname,company_name FROM user_table where user_name ='{user_name}' ", con=mydb)

    if request.method == 'POST':
        user_name_new = request.POST.get('user_name')
        user_password = request.POST.get('user_password')
        status = request.POST.get('status')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        compamy = request.POST.get('company')
        cursor = mydb.cursor()
        update_query = f"UPDATE user_table SET user_name = '{user_name_new}', user_password = '{user_password}', \
        status = '{status}',fname = '{fname}',lname = '{lname},company_name={compamy}'WHERE user_name = '{user_name}'"
        cursor.execute(update_query)
        mydb.commit()


        message = "อัปเดตข้อมูลผู้ใช้สำเร็จ"
        return render(request, 'register_value.html', {'message': message})
    
    return render(request, 'user_details.html', {'user_table': user_table})






def user_delete(request,user_name):

    cursor = mydb.cursor()
    delete_query = f"DELETE FROM user_table WHERE user_name='{user_name}'"
    cursor.execute(delete_query)
    mydb.commit()
    
    message = "ลบข้อมูลผู้ใช้สำเร็จ"
    print(message)
    return render(request, 'register_value.html',{'message':message})








def index(request):
    return render(request, 'index.html')

mydb_user = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pea_detail_pump"
)


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        status = request.POST.get('status')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        company = request.POST.get('company')
        cursor = mydb_user.cursor()
        sql = "SELECT * FROM user_table WHERE user_name = %s"
        data = (name,)

        # execute คำสั่ง SQL
        cursor.execute(sql, data)

        # ตรวจสอบว่ามีการพบข้อมูลหรือไม่
        if cursor.fetchone():
            message = "ชื่อผู้ใช้มีอยู่ในฐานข้อมูล"
            print(message)
            return render(request, 'register_value.html', {'message': message})
        else:
            cursor = mydb.cursor()
            update_query = f"INSERT INTO user_table (user_name, user_password,status,fname,lname,company_name) \
                VALUES ('{name}', '{password}', '{status}','{fname}','{lname}','{company}')"
            cursor.execute(update_query)
            mydb.commit()

            
            message = "เพิ่มข้อมูลผู้ใช้สำเร็จ"
            return render(request, 'register_value.html',{'message': message})
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        cursor = mydb_user.cursor()
        sql = "SELECT * FROM user_table WHERE user_name = %s and user_password = %s"
        data = (name,password)

        # execute คำสั่ง SQL
        cursor.execute(sql, data)

        # ตรวจสอบว่ามีการพบข้อมูลหรือไม่
        if cursor.fetchone():
            message = "เข้าสู่ระบบสำเร็จ"
            return render(request, 'register_value.html',{'message': message})
            
        else:
            message = "เข้าสู่ระบบไม่สำเร็จ"
            return render(request, 'register_value.html', {'message': message})

    else:
        return render(request, 'login.html')

def search_sql_files(request):
    form = SQLFileSearchForm()
    results = []

    if request.method == 'POST':
        form = SQLFileSearchForm(request.POST, request.FILES)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            sql_file = form.cleaned_data['sql_file']

            # ตรวจสอบว่ามีไฟล์ SQL ที่มีชื่อเดียวกับไฟล์ที่ผู้ใช้เลือกหรือไม่
            existing_file = SQLFile.objects.filter(file_name=sql_file.name).first()
            if existing_file:
                # ลบไฟล์ SQL ที่มีชื่อเดียวกันก่อนหน้านี้ (ถ้ามี)
                existing_file.delete()

            # บันทึกไฟล์ SQL ใหม่
            new_file = SQLFile(file_name=sql_file.name, file_path='path/to/save')  # ปรับเส้นทางไปยังตำแหน่งที่คุณต้องการบันทึก
            new_file.save()

            # ทำสิ่งที่คุณต้องการกับไฟล์ SQL ในตำแหน่งที่คุณบันทึก

            results = SQLFile.objects.filter(file_name__icontains=search_query)

    return render(request, 'search.html', {'form': form, 'results': results})

def delete(request,fac_number):
    cursor = mydb.cursor()
    delete_query = f"DELETE FROM factory_table WHERE fac_number='{fac_number}'"
    cursor.execute(delete_query)
    mydb.commit()
    message = "ลบข้อมูลสำเร็จ"

    return render(request, 'register_value.html', {'message': message})


def update(request,fac_number):
    factory = pd.read_sql(f"SELECT equipment,brand,model_short,model,rpm from factory_table WHERE fac_number = '{fac_number}' LIMIT 1", con=mydb)

    if request.method == 'POST':
        fac_number = request.POST.get('fac_number')
        equipment = request.POST.get('equipment')
        brand = request.POST.get('brand')
        model_short = request.POST.get('model_short')
        model = request.POST.get('model')
        rpm = request.POST.get('rpm')

        cursor = mydb.cursor()
        update_query = f"UPDATE factory_table SET equipment = '{equipment}', brand = '{brand}', \
        model_short = '{model_short}', model = '{model}', rpm = '{rpm}' WHERE fac_number = '{fac_number}'"
        cursor.execute(update_query)
        mydb.commit()

        message = "อัปเดตข้อมูลสำเร็จ"
        return render(request, 'register_value.html', {'message': message})
    
    elif  request.method == 'POST'and request.FILES['excel_file']:
        fac_number = request.POST.get('fac_number')
        equipment = request.POST.get('equipment')
        brand = request.POST.get('brand')
        model_short = request.POST.get('model_short')
        model = request.POST.get('model')
        rpm = request.POST.get('rpm')
        excel_file = request.FILES['excel_file']

        cursor = mydb.cursor()
        del_query = f"DELETE FROM factory_table where fac_number = '{fac_number}'"
        cursor.execute(del_query)
        mydb.commit()

        se_quence_imp_list, imp_dia_list_pre, imp_x_list, imp_y_list, \
        se_quence_eff_list, eff_cleaned, eff_x_list, eff_y_list, \
        eff_rl, se_quence_power_list, power_dia_list_pre, \
        power_x_list, power_y_list, se_quence_npshr_list, \
        npshr_dia_list_pre, npshr_x_list, npshr_y_list = update_data_excel(excel_file)


        cursor = mydb.cursor()
        del_query = f"DELETE FROM factory_table WHERE fac_number='{fac_number}'"
        cursor.execute(del_query)
        mydb.commit()


        ###imp
        for i in range(len(imp_dia_list_pre)):
            insert_imp_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                se_quence, imp_dia, flow, head,curve_format) \
                    VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                        '{rpm}', 'QH', '{se_quence_imp_list[i]}', {imp_dia_list_pre[i]}, {imp_x_list[i]}, \
                            {imp_y_list[i]},'{model_short}')"
            cursor.execute(insert_imp_query)

        ###eff
        for i in range(len(eff_cleaned)):
            insert_eff_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                se_quence, eff, flow, head,curve_format,eff_rl,eff_status,tolerance,scale_xy) \
                    VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                        '{rpm}', 'EFF', '{se_quence_eff_list[i]}', {eff_cleaned[i]}, {eff_x_list[i]}, \
                            {eff_y_list[i]},'{model_short}','{eff_rl[i]}',1,10,10)"
            cursor.execute(insert_eff_query)

        ###power
        for i in range(len(power_dia_list_pre)):
            insert_power_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                se_quence, npshr, flow, head,curve_format,tolerance,scale_xy) \
                    VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                        '{rpm}', 'KW', '{se_quence_power_list[i]}', {power_dia_list_pre[i]}, {power_x_list[i]}, \
                            {power_y_list[i]},'{model_short}',10,10)"
            cursor.execute(insert_power_query)

        ###npshr
        for i in range(len(npshr_dia_list_pre)):
            insert_eff_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                se_quence, npshr, flow, head,curve_format,tolerance,scale_xy) \
                    VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                        '{rpm}', 'NPSHR', '{se_quence_npshr_list[i]}', {npshr_dia_list_pre[i]}, {npshr_x_list[i]}, \
                            {npshr_y_list[i]},'{model_short}',10,10)"
            cursor.execute(insert_eff_query)
            
        mydb.commit()
        cursor.close()

        message = "อัปเดตข้อมูลสำเร็จ"
        return render(request, 'register_value.html', {'message': message})
        

        

    return render(request, 'update.html',{'fac_number': fac_number,'factory':factory})

def add_data(request):
    if request.method == 'POST'and request.FILES['excel_file']:
        fac_number = request.POST.get('fac_number')
        equipment = request.POST.get('equipment')
        brand = request.POST.get('brand')
        model_short = request.POST.get('model_short')
        size = request.POST.get('size')
        rpm = request.POST.get('rpm')
        excel_file = request.FILES['excel_file']



        model = "{}{} {}".format(model_short, size, rpm)
        # print(model)
        se_quence_imp_list, imp_dia_list_pre, imp_x_list, imp_y_list, \
        se_quence_eff_list, eff_cleaned, eff_x_list, eff_y_list, \
        eff_rl, se_quence_power_list, power_dia_list_pre, \
        power_x_list, power_y_list, se_quence_npshr_list, \
        npshr_dia_list_pre, npshr_x_list, npshr_y_list = update_data_excel(excel_file,fac_number)
         ###imp
        cursor = mydb.cursor()
        for i in range(len(imp_dia_list_pre)):
            insert_imp_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                se_quence, imp_dia, flow, head,curve_format) \
                    VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                        '{rpm}', 'QH', '{se_quence_imp_list[i]}', {imp_dia_list_pre[i]}, {imp_x_list[i]}, \
                            {imp_y_list[i]},'{model_short}')"
            cursor.execute(insert_imp_query)

        ###eff
        for i in range(len(eff_cleaned)):
            insert_eff_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                se_quence, eff, flow, head,curve_format,eff_rl,eff_status,tolerance,scale_xy) \
                    VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                        '{rpm}', 'EFF', '{se_quence_eff_list[i]}', {eff_cleaned[i]}, {eff_x_list[i]}, \
                            {eff_y_list[i]},'{model_short}','{eff_rl[i]}',1,10,10)"
            cursor.execute(insert_eff_query)
            
        ###power
        for i in range(len(power_dia_list_pre)):
            insert_power_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                se_quence, imp_dia, flow, kw,curve_format,tolerance,scale_xy) \
                    VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                        '{rpm}', 'KW', '{se_quence_power_list[i]}', {power_dia_list_pre[i]}, {power_x_list[i]}, \
                            {power_y_list[i]},'{model_short}',10,10)"
            cursor.execute(insert_power_query)

        ###npshr
        for i in range(len(npshr_dia_list_pre)):
            insert_eff_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                se_quence, imp_dia, flow, npshr,curve_format,tolerance,scale_xy) \
                    VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                        '{rpm}', 'NPSHR', '{se_quence_npshr_list[i]}', {npshr_dia_list_pre[i]}, {npshr_x_list[i]}, \
                            {npshr_y_list[i]},'{model_short}',10,10)"
            cursor.execute(insert_eff_query)

        mydb.commit()
        cursor.close()

        message = "เพิ่มข้อมูลสำเร็จ"
        return render(request, 'register_value.html', {'message': message})
    return render(request,'adddata.html')



        



































































