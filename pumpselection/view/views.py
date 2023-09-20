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
from pumpselection.view.showchart import chart_kdin,chart_kiso,chart_max3




def my_view(request):
    factory = pd.read_sql(f"SELECT fac_number FROM factory_table WHERE model_short = 'KDIN' GROUP by fac_number ", con=mydb)

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
                    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,se_quence,eff_rl FROM factory_table where model_short = "KDIN"', con=mydb)
                factory = pd.read_sql(f"SELECT fac_number FROM factory_table WHERE model_short = 'KDIN' GROUP by fac_number ", con=mydb)
                output = []
                for i in range(len(factory)):
                    output.append(loaddata_kdin(f"{factory.iloc[i]['fac_number']}", fflow, hhead, dfkdin))
                # print(output)

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
            elif model == 'max3':
                dfmax = pd.read_sql(
                    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,se_quence,eff_rl FROM factory_table ', con=mydb)
                factory = pd.read_sql(f"SELECT fac_number FROM factory_table WHERE model_short = 'MAX3' GROUP by fac_number ", con=mydb)
                output = []
                
                for i in range(len(factory)):
                    try:
                        output.append(loaddata_max3(f"{factory.iloc[i]['fac_number']}", fflow, hhead, dfmax))
                    except:
                        pass

                # print(output)
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
    type_chart = factory['model_short'][0]

    if type_chart == "KDIN":
        im_size_lst = (factory.query(f"data_type == 'QH' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())
        eff_size_lst = (factory.query(f"fac_number == '{fac_number}' and eff_rl !=''")["eff_rl"].unique().tolist())
        kw_size_lst = (factory.query(f"data_type == 'KW' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())
        npshr_size_lst = (factory.query(f"data_type == 'NPSHR' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())
        chart = chart_kdin(fac_number,im_size_lst,kw_size_lst,eff_size_lst,npshr_size_lst)

    elif type_chart == "KISO":
        im_size_lst = factory.query(f"data_type == 'QH' and fac_number == '{fac_number}'")['imp_dia'].unique().tolist()
        eff_size_lst = (factory.query(f"data_type == 'EFF' and fac_number == '{fac_number}'")["eff"].unique().tolist())
        kw_size_lst = factory.query(f"data_type == 'KW' and fac_number == '{fac_number}'")['kw'].unique().tolist()
        npshr_size_lst = (factory.query(f"data_type == 'NPSHR' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())

        chart = chart_kiso(fac_number,im_size_lst,kw_size_lst,eff_size_lst,npshr_size_lst)
    elif type_chart == "MAX3":
        im_size_lst = (factory.query(f"data_type == 'QH' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())
        eff_size_lst = (factory.query(f"fac_number == '{fac_number}' and eff_rl !=''")["eff_rl"].unique().tolist())
        kw_size_lst = (factory.query(f"data_type == 'KW' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())
        npshr_size_lst = (factory.query(f"data_type == 'NPSHR' and fac_number == '{fac_number}'")["npshr"].unique().tolist())

        chart = chart_max3(fac_number,im_size_lst,kw_size_lst,eff_size_lst,npshr_size_lst)
    

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
        df_name = pd.read_sql(f"SELECT user_name FROM user_table where user_name = '{name}'" , con=mydb)
        df_name = df_name.to_string(index=False, header=False)
        df_password = pd.read_sql(f"SELECT user_password FROM user_table where user_name = '{name}'" , con=mydb)
        df_password = df_password.to_string(index=False, header=False)
        if name == df_name and password == df_password:
            df = pd.read_sql(f"SELECT status FROM user_table where user_name = '{name}' and user_password = '{password}'" , con=mydb)
            status = df.to_string(index=False, header=False)
            print(status)
            if status == "Admin":
                message = "เข้าสู่ระบบสำเร็จ"
                return render(request, 'register_value.html',{'message': message})
            elif status == "Sales":
                message = "เข้าสู่ระบบสำเร็จ_Sales"
                return render(request, 'register_value.html',{'message': message})
            elif status == "Customer":
                message = "เข้าสู่ระบบสำเร็จ_Customer"
                return render(request, 'register_value.html',{'message': message})
        else:
            message = "เข้าสู่ระบบไม่สำเร็จ"
            return render(request, 'register_value.html', {'message': message})
        

        # ตรวจสอบว่ามีการพบข้อมูลหรือไม่
        # if cursor.fetchone():
        #     message = "เข้าสู่ระบบสำเร็จ"
        #     return render(request, 'register_value.html',{'message': message})
            
        # else:
        #     message = "เข้าสู่ระบบไม่สำเร็จ"
        #     return render(request, 'register_value.html', {'message': message})

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
    try:
        if  request.method == 'POST'and request.FILES['excel_file']:
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
            npshr_dia_list_pre, npshr_x_list, npshr_y_list = update_data_excel(excel_file,fac_number)


            cursor = mydb.cursor()
            del_query = f"DELETE FROM factory_table WHERE fac_number='{fac_number}'"
            cursor.execute(del_query)
            mydb.commit()

            if model_short =="KDIN":
                ###imp
                eff_x_list = [value * 3.6 for value in eff_x_list]
                imp_x_list = [value * 3.6 for value in imp_x_list]
                power_x_list = [value * 3.6 for value in power_x_list]
                npshr_x_list = [value * 3.6 for value in npshr_x_list]
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
            elif model_short =="KISO":
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
                try:
                    for i in range(len(eff_cleaned)):
                        insert_eff_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                            se_quence, eff, flow, head,curve_format,eff_rl,eff_status,tolerance,scale_xy) \
                                VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                                    '{rpm}', 'EFF', '{se_quence_eff_list[i]}', {eff_cleaned[i]}, {eff_x_list[i]}, \
                                        {eff_y_list[i]},'{model_short}','{eff_rl[i]}',1,10,10)"
                        cursor.execute(insert_eff_query)
                except:
                    pass
                ###power
                for i in range(len(power_dia_list_pre)):
                    insert_power_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                        se_quence, kw, flow, head,curve_format,tolerance,scale_xy) \
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
            elif model_short =="MAX3":
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
                        se_quence, npshr, flow, head,curve_format,tolerance,scale_xy) \
                            VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                                '{rpm}', 'NPSHR', '{se_quence_npshr_list[i]}', {npshr_dia_list_pre[i]}, {npshr_x_list[i]}, \
                                    {npshr_y_list[i]},'{model_short}',10,10)"
                    cursor.execute(insert_eff_query)

                mydb.commit()
                cursor.close()

            message = "อัปเดตข้อมูลสำเร็จ"
            return render(request, 'register_value.html', {'message': message})
    except:
        pass
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

            

    return render(request, 'update.html',{'fac_number': fac_number,'factory':factory})



def add_data(request):
    fac_number_table = pd.read_sql('SELECT fac_number FROM factory_table GROUP BY fac_number' , con=mydb)
    if request.method == 'POST'and request.FILES['excel_file']:
        fac_number = request.POST.get('fac_number')
        equipment = request.POST.get('equipment')
        brand = request.POST.get('brand')
        model_short = request.POST.get('model_short')
        size = request.POST.get('size')
        rpm = request.POST.get('rpm')
        excel_file = request.FILES['excel_file']
        if f'{fac_number}' in fac_number_table['fac_number'].values:

            message = "fac_number ซ้ำ"

            return render(request, 'register_value.html', {'message': message,'fac_number':fac_number})

        else:
            model = "{}{} {}".format(model_short, size, rpm)
            se_quence_imp_list, imp_dia_list_pre, imp_x_list, imp_y_list, \
            se_quence_eff_list, eff_cleaned, eff_x_list, eff_y_list, \
            eff_rl, se_quence_power_list, power_dia_list_pre, \
            power_x_list, power_y_list, se_quence_npshr_list, \
            npshr_dia_list_pre, npshr_x_list, npshr_y_list = update_data_excel(excel_file,fac_number)

            if model_short =="KDIN":
                ###imp
                eff_x_list = [value * 3.6 for value in eff_x_list]
                imp_x_list = [value * 3.6 for value in imp_x_list]
                power_x_list = [value * 3.6 for value in power_x_list]
                npshr_x_list = [value * 3.6 for value in npshr_x_list]
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
                
            elif model_short =="KISO":
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
                try:
                    for i in range(len(eff_cleaned)):
                        insert_eff_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                            se_quence, eff, flow, head,curve_format,eff_rl,eff_status,tolerance,scale_xy) \
                                VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                                    '{rpm}', 'EFF', '{se_quence_eff_list[i]}', {eff_cleaned[i]}, {eff_x_list[i]}, \
                                        {eff_y_list[i]},'{model_short}','{eff_rl[i]}',1,10,10)"
                        cursor.execute(insert_eff_query)
                except:
                    pass
                ###power
                for i in range(len(power_dia_list_pre)):
                    insert_power_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                        se_quence, kw, flow, head,curve_format,tolerance,scale_xy) \
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
            elif model_short =="MAX3":
                ###imp
                eff_x_list = [value * 1 for value in eff_x_list]
                imp_x_list = [value * 1 for value in imp_x_list]
                power_x_list = [value * 1 for value in power_x_list]
                npshr_x_list = [value * 1 for value in npshr_x_list]
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
                        se_quence, npshr, flow, head,curve_format,tolerance,scale_xy) \
                            VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                                '{rpm}', 'NPSHR', '{se_quence_npshr_list[i]}', {npshr_dia_list_pre[i]}, {npshr_x_list[i]}, \
                                    {npshr_y_list[i]},'{model_short}',10,10)"
                    cursor.execute(insert_eff_query)

                mydb.commit()
                cursor.close()

            message = "เพิ่มข้อมูลสำเร็จ"
            return render(request, 'register_value.html', {'message': message})
    return render(request,'adddata.html')

########################################################################################################################################
#sales
        

def my_view_sales(request):
    factory = pd.read_sql(f"SELECT fac_number FROM factory_table WHERE model_short = 'KDIN' GROUP by fac_number ", con=mydb)

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
                    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,se_quence,eff_rl FROM factory_table where model_short = "KDIN"', con=mydb)
                factory = pd.read_sql(f"SELECT fac_number FROM factory_table WHERE model_short = 'KDIN' GROUP by fac_number ", con=mydb)
                output = []
                for i in range(len(factory)):
                    output.append(loaddata_kdin(f"{factory.iloc[i]['fac_number']}", fflow, hhead, dfkdin))
                # print(output)

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
            elif model == 'max3':
                dfmax = pd.read_sql(
                    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,se_quence,eff_rl FROM factory_table ', con=mydb)
                factory = pd.read_sql(f"SELECT fac_number FROM factory_table WHERE model_short = 'MAX3' GROUP by fac_number ", con=mydb)
                output = []
                
                for i in range(len(factory)):
                    try:
                        output.append(loaddata_max3(f"{factory.iloc[i]['fac_number']}", fflow, hhead, dfmax))
                    except:
                        pass

                # print(output)
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
            return render(request, 'my_template_sales.html',context)

    else:
        return render(request, 'my_template_sales.html')

def add_data_sales(request):
    fac_number_table = pd.read_sql('SELECT fac_number FROM factory_table GROUP BY fac_number' , con=mydb)
    if request.method == 'POST'and request.FILES['excel_file']:
        fac_number = request.POST.get('fac_number')
        equipment = request.POST.get('equipment')
        brand = request.POST.get('brand')
        model_short = request.POST.get('model_short')
        size = request.POST.get('size')
        rpm = request.POST.get('rpm')
        excel_file = request.FILES['excel_file']
        if f'{fac_number}' in fac_number_table['fac_number'].values:

            message = "fac_number ซ้ำ"

            return render(request, 'register_value.html', {'message': message,'fac_number':fac_number})

        else:
            model = "{}{} {}".format(model_short, size, rpm)

            se_quence_imp_list, imp_dia_list_pre, imp_x_list, imp_y_list, \
            se_quence_eff_list, eff_cleaned, eff_x_list, eff_y_list, \
            eff_rl, se_quence_power_list, power_dia_list_pre, \
            power_x_list, power_y_list, se_quence_npshr_list, \
            npshr_dia_list_pre, npshr_x_list, npshr_y_list = update_data_excel(excel_file,fac_number)
            if model_short =="KDIN":
                ###imp
                eff_x_list = [value * 3.6 for value in eff_x_list]
                imp_x_list = [value * 3.6 for value in imp_x_list]
                power_x_list = [value * 3.6 for value in power_x_list]
                npshr_x_list = [value * 3.6 for value in npshr_x_list]
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
                
            elif model_short =="KISO":
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
                try:
                    for i in range(len(eff_cleaned)):
                        insert_eff_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                            se_quence, eff, flow, head,curve_format,eff_rl,eff_status,tolerance,scale_xy) \
                                VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                                    '{rpm}', 'EFF', '{se_quence_eff_list[i]}', {eff_cleaned[i]}, {eff_x_list[i]}, \
                                        {eff_y_list[i]},'{model_short}','{eff_rl[i]}',1,10,10)"
                        cursor.execute(insert_eff_query)
                except:
                    pass
                ###power
                for i in range(len(power_dia_list_pre)):
                    insert_power_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                        se_quence, kw, flow, head,curve_format,tolerance,scale_xy) \
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
            elif model_short =="MAX3":
                ###imp
                eff_x_list = [value * 1 for value in eff_x_list]
                imp_x_list = [value * 1 for value in imp_x_list]
                power_x_list = [value * 1 for value in power_x_list]
                npshr_x_list = [value * 1 for value in npshr_x_list]
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
                        se_quence, npshr, flow, head,curve_format,tolerance,scale_xy) \
                            VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                                '{rpm}', 'NPSHR', '{se_quence_npshr_list[i]}', {npshr_dia_list_pre[i]}, {npshr_x_list[i]}, \
                                    {npshr_y_list[i]},'{model_short}',10,10)"
                    cursor.execute(insert_eff_query)

                mydb.commit()
                cursor.close()

            message = "เพิ่มข้อมูลสำเร็จ_sales"
            return render(request, 'register_value.html', {'message': message})
    return render(request,'adddata_sales.html')


def read_table_sales(request):
    data_table = pd.read_sql('SELECT fac_number, equipment, brand, model_short, model, rpm FROM factory_table GROUP BY fac_number' , con=mydb)
    
    return render(request, 'table_sales.html', {'data_table': data_table})

def show_details_sales(request, fac_number):
    factory = pd.read_sql(f"SELECT fac_number,model_short,data_type,rpm,imp_dia,flow,head,eff,npshr,kw,model,se_quence,eff_rl FROM factory_table WHERE fac_number = '{fac_number}' ", con=mydb)
    type_chart = factory['model_short'][0]

    if type_chart == "KDIN":
        im_size_lst = (factory.query(f"data_type == 'QH' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())
        eff_size_lst = (factory.query(f"fac_number == '{fac_number}' and eff_rl !=''")["eff_rl"].unique().tolist())
        kw_size_lst = (factory.query(f"data_type == 'KW' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())
        npshr_size_lst = (factory.query(f"data_type == 'NPSHR' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())
        chart = chart_kdin(fac_number,im_size_lst,kw_size_lst,eff_size_lst,npshr_size_lst)

    elif type_chart == "KISO":
        im_size_lst = factory.query(f"data_type == 'QH' and fac_number == '{fac_number}'")['imp_dia'].unique().tolist()
        eff_size_lst = (factory.query(f"data_type == 'EFF' and fac_number == '{fac_number}'")["eff"].unique().tolist())
        kw_size_lst = factory.query(f"data_type == 'KW' and fac_number == '{fac_number}'")['kw'].unique().tolist()
        npshr_size_lst = (factory.query(f"data_type == 'NPSHR' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())

        chart = chart_kiso(fac_number,im_size_lst,kw_size_lst,eff_size_lst,npshr_size_lst)
    elif type_chart == "MAX3":
        im_size_lst = (factory.query(f"data_type == 'QH' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())
        eff_size_lst = (factory.query(f"fac_number == '{fac_number}' and eff_rl !=''")["eff_rl"].unique().tolist())
        kw_size_lst = (factory.query(f"data_type == 'KW' and fac_number == '{fac_number}'")["imp_dia"].unique().tolist())
        npshr_size_lst = (factory.query(f"data_type == 'NPSHR' and fac_number == '{fac_number}'")["npshr"].unique().tolist())

        chart = chart_max3(fac_number,im_size_lst,kw_size_lst,eff_size_lst,npshr_size_lst)
    

    factory.fillna('', inplace=True)
    # หากไม่มีข้อมูล ส่งข้อความแจ้งเตือนกลับไปยังเทมเพลต
    return render(request, 'details_sales.html', {'factory': factory,'chart':chart})

def update_sales(request,fac_number):
    factory = pd.read_sql(f"SELECT equipment,brand,model_short,model,rpm from factory_table WHERE fac_number = '{fac_number}' LIMIT 1", con=mydb)
    try:
        if  request.method == 'POST'and request.FILES['excel_file']:
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
            npshr_dia_list_pre, npshr_x_list, npshr_y_list = update_data_excel(excel_file,fac_number)


            cursor = mydb.cursor()
            del_query = f"DELETE FROM factory_table WHERE fac_number='{fac_number}'"
            cursor.execute(del_query)
            mydb.commit()

            if model_short =="KDIN":
                ###imp
                eff_x_list = [value * 3.6 for value in eff_x_list]
                imp_x_list = [value * 3.6 for value in imp_x_list]
                power_x_list = [value * 3.6 for value in power_x_list]
                npshr_x_list = [value * 3.6 for value in npshr_x_list]
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
            elif model_short =="KISO":
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
                try:
                    for i in range(len(eff_cleaned)):
                        insert_eff_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                            se_quence, eff, flow, head,curve_format,eff_rl,eff_status,tolerance,scale_xy) \
                                VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                                    '{rpm}', 'EFF', '{se_quence_eff_list[i]}', {eff_cleaned[i]}, {eff_x_list[i]}, \
                                        {eff_y_list[i]},'{model_short}','{eff_rl[i]}',1,10,10)"
                        cursor.execute(insert_eff_query)
                except:
                    pass
                ###power
                for i in range(len(power_dia_list_pre)):
                    insert_power_query = f"INSERT INTO factory_table (fac_number,equipment, brand, model_short, model, rpm, data_type, \
                        se_quence, kw, flow, head,curve_format,tolerance,scale_xy) \
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
            elif model_short =="MAX3":
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
                        se_quence, npshr, flow, head,curve_format,tolerance,scale_xy) \
                            VALUES ('{fac_number}','{equipment}', '{brand}', '{model_short}', '{model}', \
                                '{rpm}', 'NPSHR', '{se_quence_npshr_list[i]}', {npshr_dia_list_pre[i]}, {npshr_x_list[i]}, \
                                    {npshr_y_list[i]},'{model_short}',10,10)"
                    cursor.execute(insert_eff_query)

                mydb.commit()
                cursor.close()

            message = "อัปเดตข้อมูลสำเร็จ_sales"
            return render(request, 'register_value.html', {'message': message})
    except:
        pass
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

            message = "อัปเดตข้อมูลสำเร็จ_sales"
            return render(request, 'register_value.html', {'message': message})        

            

    return render(request, 'update_sales.html',{'fac_number': fac_number,'factory':factory})



def delete_sales(request,fac_number):
    cursor = mydb.cursor()
    delete_query = f"DELETE FROM factory_table WHERE fac_number='{fac_number}'"
    print(fac_number)
    cursor.execute(delete_query)
    mydb.commit()
    message = "ลบข้อมูลสำเร็จ_sales"

    return render(request, 'register_value.html', {'message': message})

########################################################################################################################################
#cus




def my_view_cus(request):
    factory = pd.read_sql(f"SELECT fac_number FROM factory_table WHERE model_short = 'KDIN' GROUP by fac_number ", con=mydb)

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
                    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,se_quence,eff_rl FROM factory_table where model_short = "KDIN"', con=mydb)
                factory = pd.read_sql(f"SELECT fac_number FROM factory_table WHERE model_short = 'KDIN' GROUP by fac_number ", con=mydb)
                output = []
                for i in range(len(factory)):
                    output.append(loaddata_kdin(f"{factory.iloc[i]['fac_number']}", fflow, hhead, dfkdin))
                # print(output)

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
            elif model == 'max3':
                dfmax = pd.read_sql(
                    f'SELECT fac_number,flow,head,imp_dia,kw,npshr,data_type,model,eff,se_quence,eff_rl FROM factory_table ', con=mydb)
                factory = pd.read_sql(f"SELECT fac_number FROM factory_table WHERE model_short = 'MAX3' GROUP by fac_number ", con=mydb)
                output = []
                
                for i in range(len(factory)):
                    try:
                        output.append(loaddata_max3(f"{factory.iloc[i]['fac_number']}", fflow, hhead, dfmax))
                    except:
                        pass

                # print(output)
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
            return render(request, 'my_template_cus.html',context)

    else:
        return render(request, 'my_template_cus.html')
















































