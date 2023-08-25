import openpyxl
from openpyxl import load_workbook
import xlrd
import mysql.connector
import pandas as pd
import re
def update_data_excel(excel_file,fac_number):
    workbook = load_workbook(excel_file)
    worksheet = workbook['Sheet1']  # ระบุชื่อแผ่นงานที่ต้องการอ่าน
    fac_number = fac_number
    # ดึงค่าจากเซลล์และเก็บในตัวแปร
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pea_detail_pump"
    )




    start_row = 5
    end_row = 10000

    current_row = start_row


    # print(data_table)

    imp_dia_list = []
    imp_x_list = []
    imp_y_list = []
    se_quence_imp_1 = 4
    se_quence_imp_2 = 4
    se_quence_imp_3 = 4
    se_quence_imp_4 = 4
    se_quence_imp_5 = 4
    se_quence_imp_6 = 4
    se_quence_imp_7 = 4
    se_quence_imp_8 = 3
    se_quence_imp_9 = 4
    se_quence_imp_list = []
    for _ in range(start_row, end_row + 1):


        cell_B = 'B' + str(current_row)
        cell_C = 'C' + str(current_row)
        imp_x_1 = worksheet[cell_B].value
        imp_x_list.append(imp_x_1)
        imp_y_1 = worksheet[cell_C].value
        imp_y_list.append(imp_y_1)
        if imp_x_1 != None:
            imp_dia_1 = worksheet['B3'].value
            imp_dia_list.append(imp_dia_1)
            se_quence_imp_1 += 1
            se_quence_imp_list.append(se_quence_imp_1)
        else:
            pass


        cell_E = 'E' + str(current_row)
        cell_F = 'F' + str(current_row)
        imp_x_2 = worksheet[cell_E].value
        imp_x_list.append(imp_x_2)
        imp_y_2 = worksheet[cell_F].value
        imp_y_list.append(imp_y_2)
        if imp_x_2 != None:
            imp_dia_2 = worksheet['E3'].value
            imp_dia_list.append(imp_dia_2)
            se_quence_imp_2 += 1
            se_quence_imp_list.append(se_quence_imp_2)
        else:
            pass
        
        cell_H = 'H' + str(current_row)
        cell_I = 'I' + str(current_row)
        imp_x_3 = worksheet[cell_H].value
        imp_x_list.append(imp_x_3)
        imp_y_3 = worksheet[cell_I].value
        imp_y_list.append(imp_y_3)
        if imp_x_3 != None:
            imp_dia_3 = worksheet['H3'].value
            imp_dia_list.append(imp_dia_3)
            se_quence_imp_3 += 1
            se_quence_imp_list.append(se_quence_imp_3)
        else:
            pass
        

        cell_K = 'K' + str(current_row)
        cell_L = 'L' + str(current_row)
        imp_x_4 = worksheet[cell_K].value
        imp_x_list.append(imp_x_4)
        imp_y_4 = worksheet[cell_L].value
        imp_y_list.append(imp_y_4)
        if imp_x_4 != None:
            imp_dia_4 = worksheet['K3'].value
            imp_dia_list.append(imp_dia_4)
            se_quence_imp_4 += 1
            se_quence_imp_list.append(se_quence_imp_4)
        else:
            pass


        cell_N = 'N' + str(current_row)
        cell_O = 'O' + str(current_row)
        imp_x_5 = worksheet[cell_N].value
        imp_x_list.append(imp_x_5)
        imp_y_5 = worksheet[cell_O].value
        imp_y_list.append(imp_y_5)
        if imp_x_5 != None:
            imp_dia_5 = worksheet['N3'].value
            imp_dia_list.append(imp_dia_5)
            se_quence_imp_5 += 1
            se_quence_imp_list.append(se_quence_imp_5)
        else:
            pass

        cell_Q = 'Q' + str(current_row)
        cell_R = 'R' + str(current_row)
        imp_x_6 = worksheet[cell_Q].value
        imp_x_list.append(imp_x_6)
        imp_y_6 = worksheet[cell_R].value
        imp_y_list.append(imp_y_6)
        if imp_x_6 != None:
            imp_dia_6 = worksheet['Q3'].value
            imp_dia_list.append(imp_dia_6)
            se_quence_imp_6 += 1
            se_quence_imp_list.append(se_quence_imp_6)
        else:
            pass


        cell_T = 'T' + str(current_row)
        cell_U = 'U' + str(current_row)
        imp_x_7 = worksheet[cell_T].value
        imp_x_list.append(imp_x_7)
        imp_y_7 = worksheet[cell_U].value
        imp_y_list.append(imp_y_7)
        if imp_x_7 != None:
            imp_dia_7 = worksheet['T3'].value
            imp_dia_list.append(imp_dia_7)
            se_quence_imp_7 += 1
            se_quence_imp_list.append(se_quence_imp_7)
        else:
            pass

        cell_W = 'W' + str(current_row)
        cell_X = 'X' + str(current_row)
        imp_x_8 = worksheet[cell_W].value
        imp_x_list.append(imp_x_8)
        imp_y_8 = worksheet[cell_X].value
        imp_y_list.append(imp_y_8)
        if imp_x_8 != None:
            imp_dia_8 = worksheet['W3'].value
            imp_dia_list.append(imp_dia_8)
            se_quence_imp_8 += 1
            se_quence_imp_list.append(se_quence_imp_8)
        else:
            pass

        cell_Z = 'Z' + str(current_row)
        cell_AA = 'AA' + str(current_row)
        imp_x_9 = worksheet[cell_Z].value
        imp_x_list.append(imp_x_9)
        imp_y_9 = worksheet[cell_AA].value
        imp_y_list.append(imp_y_9)
        if imp_x_9 != None:
            imp_dia_9 = worksheet['Z3'].value
            imp_dia_list.append(imp_dia_9)
            se_quence_imp_9 += 1
            se_quence_imp_list.append(se_quence_imp_9)
        else:
            pass
        current_row += 1


    imp_dia_list = [
        float(item.replace('mm', '').replace(' mm', ''))
        for item in imp_dia_list if item is not None
    ]

    # try:
    #     imp_dia_list = [{item.replace('mm', '')} for item in imp_dia_list if item is not None]
    # except ValueError:
    #     imp_dia_list = [{item.replace(' mm', '')} for item in imp_dia_list if item is not None]



    imp_dia_list_pre = []

    for data in imp_dia_list:
        imp_dia_list_pre.append(float(data))
    # id_qh = pd.read_sql('SELECT id FROM `factory_table` WHERE fac_number = "fac-0255"  and data_type = "qh"' , con=mydb).values.tolist()


    # print(type(imp_dia_list))
    # print(imp_dia_list)
    imp_x_list = [item for item in imp_x_list if item is not None]
    imp_x_list = [value * 3.6 for value in imp_x_list]
    imp_y_list = [item for item in imp_y_list if item is not None]

    # print(len(id_qh))
    # print(len(imp_dia_list))
    # print(len(imp_x_list))
    # print(len(imp_y_list))
    se_quence = 4

    # try :
    #     for i in range(len(imp_dia_list_pre)):
    #         print(se_quence_imp_list[i],imp_dia_list_pre[i],imp_x_list[i],imp_y_list[i])
    # except:
    #     pass

    # for i in range(len(imp_dia_list_pre)):
    #     se_quence = se_quence + 1
    #     insert_imp_query = f"INSERT INTO factory_table (equipment, brand, model_short, model, rpm, data_type, se_quence, imp_dia, flow, head) \
    #             VALUES ('equipment', 'brand', 'model_short', 'model', 'rpm', 'qh', '{se_quence_imp_list[i]}', {imp_dia_list_pre[i]}, {imp_x_list[i]}, {imp_y_list[i]})"
    #     cursor.execute(insert_imp_query)
    #     mydb.commit()


        # print("ผ่าน")








    # for i in range(len(id_qh)):
    #     print("ID: {}, Imp_x: {}, Imp_y: {}, Imp_dia: {}".format(id_qh[i], imp_x_list[i], imp_y_list[i], imp_dia_list[i]))
    # print(id_qh[0])
    # print(len(imp_x_list))
    # print(len(imp_y_list))
    # print(len(imp_dia_list))

    # data_table = pd.read_sql(f'factory_table SET flow = "{imp_x_list[0]}", head = "{imp_y_list[0]}" WHERE ID = {id_qh[0]} and imp = {imp_dia_list[0]}"' , con=mydb)

    #############################
    #EFFICIENCY%
    start_row = 5
    end_row = 10000			
 
    current_row = start_row
    eff_dia_list = []
    eff_x_list = []
    eff_y_list = []
    se_quence_eff_1 = 0
    se_quence_eff_2 = 0
    se_quence_eff_3 = 0
    se_quence_eff_4 = 0
    se_quence_eff_5 = 0
    se_quence_eff_6 = 0
    se_quence_eff_7 = 0
    se_quence_eff_8 = 0
    se_quence_eff_9 = 0
    se_quence_eff_10 = 0
    se_quence_eff_11 = 0
    se_quence_eff_12 = 0
    se_quence_eff_13 = 0
    se_quence_eff_14 = 0
    se_quence_eff_15 = 0
    se_quence_eff_list = []
    for _ in range(start_row, end_row + 1):
        cell_AD = 'AD' + str(current_row)
        cell_AE = 'AE' + str(current_row)
        eff_x_1 = worksheet[cell_AD].value
        eff_x_list.append(eff_x_1)
        eff_y_1 = worksheet[cell_AE].value
        eff_y_list.append(eff_y_1)
        # print(eff_x_list)
        if eff_y_1 != None:
            eff_dia_1 = (worksheet['AD3'].value)
            eff_dia_list.append(eff_dia_1)
            se_quence_eff_1 += 1
            se_quence_eff_list.append(se_quence_eff_1)
        else:
            pass


        cell_AG = 'AG' + str(current_row)
        cell_AH = 'AH' + str(current_row)
        eff_x_2 = worksheet[cell_AG].value
        eff_x_list.append(eff_x_2)
        eff_y_2 = worksheet[cell_AH].value
        eff_y_list.append(eff_y_2)
        if eff_x_2 != None:
            eff_dia_2 = worksheet['AG3'].value
            eff_dia_list.append(eff_dia_2)
            se_quence_eff_2 += 1
            se_quence_eff_list.append(se_quence_eff_2)
        else:
            pass
        
        cell_AJ = 'AJ' + str(current_row)
        cell_AK = 'AK' + str(current_row)
        eff_x_3 = worksheet[cell_AJ].value
        eff_x_list.append(eff_x_3)
        eff_y_3 = worksheet[cell_AK].value
        eff_y_list.append(eff_y_3)
        if eff_x_3 != None:
            eff_dia_3 = worksheet['AJ3'].value
            eff_dia_list.append(eff_dia_3)
            se_quence_eff_3 += 1
            se_quence_eff_list.append(se_quence_eff_3)
        else:
            pass
        

        cell_AM = 'AM' + str(current_row)
        cell_AN = 'AN' + str(current_row)
        eff_x_4 = worksheet[cell_AM].value
        eff_x_list.append(eff_x_4)
        eff_y_4 = worksheet[cell_AN].value
        eff_y_list.append(eff_y_4)

        if eff_x_4 != None:
            eff_dia_4 = worksheet['AM3'].value
            eff_dia_list.append(eff_dia_4)
            se_quence_eff_4 += 1
            se_quence_eff_list.append(se_quence_eff_4)
        else:
            pass


        cell_AP = 'AP' + str(current_row)
        cell_AQ = 'AQ' + str(current_row)
        eff_x_5 = worksheet[cell_AP].value
        eff_x_list.append(eff_x_5)
        eff_y_5 = worksheet[cell_AQ].value
        eff_y_list.append(eff_y_5)

        if eff_x_5 != None:
            eff_dia_5 = worksheet['AP3'].value
            eff_dia_list.append(eff_dia_5)
            se_quence_eff_5 += 1
            se_quence_eff_list.append(se_quence_eff_5)
        else:
            pass

        cell_AS = 'AS' + str(current_row)
        cell_AT = 'AT' + str(current_row)
        eff_x_6 = worksheet[cell_AS].value
        eff_x_list.append(eff_x_6)
        eff_y_6 = worksheet[cell_AT].value
        eff_y_list.append(eff_y_6)

        if eff_x_6 != None:
            eff_dia_6 = worksheet['AS3'].value
            eff_dia_list.append(eff_dia_6)
            se_quence_eff_6 += 1
            se_quence_eff_list.append(se_quence_eff_6)
        else:
            pass


        cell_AV = 'AV' + str(current_row)
        cell_AW = 'AW' + str(current_row)
        eff_x_7 = worksheet[cell_AV].value
        eff_x_list.append(eff_x_7)
        eff_y_7 = worksheet[cell_AW].value
        eff_y_list.append(eff_y_7)

        if eff_x_7 != None:
            eff_dia_7 = worksheet['AV3'].value
            eff_dia_list.append(eff_dia_7)
            se_quence_eff_7 += 1
            se_quence_eff_list.append(se_quence_eff_7)
        else:
            pass

        cell_AY = 'AY' + str(current_row)
        cell_AZ = 'AZ' + str(current_row)
        eff_x_8 = worksheet[cell_AY].value
        eff_x_list.append(eff_x_8)
        eff_y_8 = worksheet[cell_AZ].value
        eff_y_list.append(eff_y_8)

        if eff_x_8 != None:
            eff_dia_8 = worksheet['AY3'].value
            eff_dia_list.append(eff_dia_8)
            se_quence_eff_8 += 1
            se_quence_eff_list.append(se_quence_eff_8)
        else:
            pass

        cell_BB = 'BB' + str(current_row)
        cell_BC = 'BC' + str(current_row)
        eff_x_9 = worksheet[cell_BB].value
        eff_x_list.append(eff_x_9)
        eff_y_9 = worksheet[cell_BC].value
        eff_y_list.append(eff_y_9)

        if eff_x_8 != None:
            eff_dia_9 = worksheet['BB3'].value
            eff_dia_list.append(eff_dia_9)
            se_quence_eff_9 += 1
            se_quence_eff_list.append(se_quence_eff_9)
        else:
            pass

        cell_BE = 'BE' + str(current_row)
        cell_BF = 'BF' + str(current_row)
        eff_x_10 = worksheet[cell_BE].value
        eff_x_list.append(eff_x_10)
        eff_y_10 = worksheet[cell_BF].value
        eff_y_list.append(eff_y_10)

        if eff_x_10 != None:
            eff_dia_10 = worksheet['BE3'].value
            eff_dia_list.append(eff_dia_10)
            se_quence_eff_10 += 1
            se_quence_eff_list.append(se_quence_eff_10)
        else:
            pass

        cell_BH = 'BH' + str(current_row)
        cell_BI = 'BI' + str(current_row)
        eff_x_11 = worksheet[cell_BH].value
        eff_x_list.append(eff_x_11)
        eff_y_11 = worksheet[cell_BI].value
        eff_y_list.append(eff_y_11)

        if eff_x_11 != None:
            eff_dia_11 = worksheet['BH3'].value
            eff_dia_list.append(eff_dia_11)
            se_quence_eff_11 += 1
            se_quence_eff_list.append(se_quence_eff_11)
        else:
            pass

        cell_BK = 'BK' + str(current_row)
        cell_BL = 'BL' + str(current_row)
        eff_x_12 = worksheet[cell_BK].value
        eff_x_list.append(eff_x_12)
        eff_y_12 = worksheet[cell_BL].value
        eff_y_list.append(eff_y_12)

        if eff_x_12 != None:
            eff_dia_12 = worksheet['BK3'].value
            eff_dia_list.append(eff_dia_12)
            se_quence_eff_12 += 1
            se_quence_eff_list.append(se_quence_eff_12)
        else:
            pass

        cell_BK = 'BN' + str(current_row)
        cell_BL = 'BO' + str(current_row)
        eff_x_13 = worksheet[cell_BK].value
        eff_x_list.append(eff_x_13)
        eff_y_13 = worksheet[cell_BL].value
        eff_y_list.append(eff_y_13)

        if eff_x_13 != None:
            eff_dia_13 = worksheet['BN3'].value
            eff_dia_list.append(eff_dia_13)
            se_quence_eff_13 += 1
            se_quence_eff_list.append(se_quence_eff_13)
        else:
            pass

        cell_BQ = 'BQ' + str(current_row)
        cell_BR = 'BR' + str(current_row)
        eff_x_14 = worksheet[cell_BQ].value
        eff_x_list.append(eff_x_14)
        eff_y_14 = worksheet[cell_BR].value
        eff_y_list.append(eff_y_14)

        if eff_x_14 != None:
            eff_dia_14 = worksheet['BQ3'].value
            eff_dia_list.append(eff_dia_14)
            se_quence_eff_14 += 1
            se_quence_eff_list.append(se_quence_eff_14)
        else:
            pass

        cell_BT = 'BT' + str(current_row)
        cell_BU = 'BU' + str(current_row)
        eff_x_15 = worksheet[cell_BT].value
        eff_x_list.append(eff_x_15)
        eff_y_15 = worksheet[cell_BU].value
        eff_y_list.append(eff_y_15)

        if eff_x_15 != None:
            eff_dia_15 = worksheet['BT3'].value
            eff_dia_list.append(eff_dia_15)
            se_quence_eff_15 += 1
            se_quence_eff_list.append(se_quence_eff_15)
        else:
            pass




        current_row += 1




    # imp_dia_list = [{item.replace(' mm', '')} for item in imp_dia_list if item is not None]
    eff_dia_list = [item for item in eff_dia_list if item is not None]

    # id_eff = pd.read_sql('SELECT id FROM `factory_table` WHERE fac_number = "fac-0255"  and data_type = "eff"' , con=mydb).values.tolist()
    # print(eff_dia_list)
    eff_rl = []
    # print(eff_dia_list)
    for item in eff_dia_list:
        if isinstance(item, float):
            item = item * 100
            eff_rl.append(item)
        else:
            eff_rl.append(item)
    # print(se_quence_eff_list)
    eff_cleaned = []
    for item in eff_dia_list:
        if isinstance(item, str):
            number = item.replace('%', '').replace('L', '').replace('R', '')
            eff_cleaned.append(float(number))
        else:
            item = item * 100
            eff_cleaned.append(item)





    eff_x_list = [item for item in eff_x_list if item is not None]
    eff_x_list = [value * 3.6 for value in eff_x_list]
    eff_y_list = [item for item in eff_y_list if item is not None]

    # try :
    #     for i in range(len(eff_dia_list)):
    #         print(eff_cleaned[i],eff_x_list[i],eff_y_list[i])
    # except:
    #     pass
    se_quence = 4

    # for i in range(len(eff_cleaned)):
    #     se_quence = se_quence + 1
    #     insert_eff_query = f"INSERT INTO factory_table (equipment, brand, model_short, model, rpm, data_type, se_quence, eff, flow, head,eff_rl) \
    #             VALUES ('equipment', 'brand', 'model_short', 'model', 'rpm', 'eff', '{se_quence_eff_list[i]}', {eff_cleaned[i]}, {eff_x_list[i]}, {eff_y_list[i]},'{eff_rl[i]}')"
    #     cursor.execute(insert_eff_query)
    #     mydb.commit()

    # print(len(eff_cleaned))
    # print(len(eff_x_list))
    # print(len(eff_y_list))

    #############
    #POWER
    start_row = 5
    end_row = 10000			    
    current_row = start_row
    power_dia_list = []
    power_x_list = []
    power_y_list = []
    se_quence_power_1 = 4
    se_quence_power_2 = 4
    se_quence_power_3 = 4
    se_quence_power_4 = 4
    se_quence_power_5 = 4
    se_quence_power_6 = 4
    se_quence_power_7 = 4
    se_quence_power_8 = 4
    se_quence_power_9 = 4
    se_quence_power_list = []
    for _ in range(start_row, end_row + 1):


        cell_BX = 'BX' + str(current_row)
        cell_BY = 'BY' + str(current_row)
        power_x_1 = worksheet[cell_BX].value
        power_x_list.append(power_x_1)
        power_y_1 = worksheet[cell_BY].value
        power_y_list.append(power_y_1)
        if power_x_1 != None:
            power_dia_1 = worksheet['BX3'].value
            power_dia_list.append(power_dia_1)
            se_quence_power_1 += 1
            se_quence_power_list.append(se_quence_power_1)
        else:
            pass


        cell_CA = 'CA' + str(current_row)
        cell_CB = 'CB' + str(current_row)
        power_x_2 = worksheet[cell_CA].value
        power_x_list.append(power_x_2)
        power_y_2 = worksheet[cell_CB].value
        power_y_list.append(power_y_2)
        if power_x_2 != None:
            power_dia_2 = worksheet['CA3'].value
            power_dia_list.append(power_dia_2)
            se_quence_power_2 += 1
            se_quence_power_list.append(se_quence_power_2)
        else:
            pass
        
        cell_CD = 'CD' + str(current_row)
        cell_CE = 'CE' + str(current_row)
        power_x_3 = worksheet[cell_CD].value
        power_x_list.append(power_x_3)
        power_y_3 = worksheet[cell_CE].value
        power_y_list.append(power_y_3)
        if power_x_3 != None:
            power_dia_3 = worksheet['CD3'].value
            power_dia_list.append(power_dia_3)
            se_quence_power_3 += 1
            se_quence_power_list.append(se_quence_power_3)
        else:
            pass
        

        cell_CG = 'CG' + str(current_row)
        cell_CH = 'CH' + str(current_row)
        power_x_4 = worksheet[cell_CG].value
        power_x_list.append(power_x_4)
        power_y_4 = worksheet[cell_CH].value
        power_y_list.append(power_y_4)

        if power_x_4 != None:
            power_dia_4 = worksheet['CG3'].value
            power_dia_list.append(power_dia_4)
            se_quence_power_4 += 1
            se_quence_power_list.append(se_quence_power_4)
        else:
            pass


        cell_CJ = 'CJ' + str(current_row)
        cell_CK = 'CK' + str(current_row)
        power_x_5 = worksheet[cell_CJ].value
        power_x_list.append(power_x_5)
        power_y_5 = worksheet[cell_CK].value
        power_y_list.append(power_y_5)

        if power_x_5 != None:
            power_dia_5 = worksheet['CJ3'].value
            power_dia_list.append(power_dia_5)
            se_quence_power_5 += 1
            se_quence_power_list.append(se_quence_power_5)
        else:
            pass

        cell_CM = 'CM' + str(current_row)
        cell_CN = 'CN' + str(current_row)
        power_x_6 = worksheet[cell_CM].value
        power_x_list.append(power_x_6)
        power_y_6 = worksheet[cell_CN].value
        power_y_list.append(power_y_6)

        if power_x_6 != None:
            power_dia_6 = worksheet['CM3'].value
            power_dia_list.append(power_dia_6)
            se_quence_power_6 += 1
            se_quence_power_list.append(se_quence_power_6)
        else:
            pass

        cell_CP = 'CP' + str(current_row)
        cell_CQ = 'CQ' + str(current_row)
        power_x_7 = worksheet[cell_CP].value
        power_x_list.append(power_x_7)
        power_y_7 = worksheet[cell_CQ].value
        power_y_list.append(power_y_7)

        if power_x_7 != None:
            power_dia_7 = worksheet['CP3'].value
            power_dia_list.append(power_dia_7)
            se_quence_power_7 += 1
            se_quence_power_list.append(se_quence_power_7)
        else:
            pass

        cell_CS = 'CS' + str(current_row)
        cell_CT = 'CT' + str(current_row)
        power_x_8 = worksheet[cell_CS].value
        power_x_list.append(power_x_8)
        power_y_8 = worksheet[cell_CT].value
        power_y_list.append(power_y_8)

        if power_x_8 != None:
            power_dia_8 = worksheet['CS3'].value
            power_dia_list.append(power_dia_8)
            se_quence_power_8 += 1
            se_quence_power_list.append(se_quence_power_8)
        else:
            pass

        cell_CV = 'CV' + str(current_row)
        cell_CW = 'CW' + str(current_row)
        power_x_9 = worksheet[cell_CV].value
        power_x_list.append(power_x_9)
        power_y_9 = worksheet[cell_CW].value
        power_y_list.append(power_y_9)

        if power_x_9 != None:
            power_dia_9 = worksheet['CS3'].value
            power_dia_list.append(power_dia_9)
            se_quence_power_9 += 1
            se_quence_power_list.append(se_quence_power_9)
        else:
            pass

        current_row += 1

    

    # try:
    #     power_dia_list = [{item.replace('kW', '')} for item in power_dia_list if item is not None]
    # except ValueError:
    #     try:
    #         power_dia_list = [{item.replace('kw', '')} for item in power_dia_list if item is not None]
    #     except ValueError:
    #         power_dia_list = [{item.replace(' mm', '')} for item in power_dia_list if item is not None]


    
    power_dia_list = [
        float(item.replace('kW', '').replace('kw', '').replace(' mm', '').replace('mm', ''))
        for item in power_dia_list if item is not None
    ]




    power_dia_list_pre = []

    for data in power_dia_list:
        power_dia_list_pre.append(float(data))
    # print(power_dia_list_pre)

    power_x_list = [item for item in power_x_list if item is not None]
    power_x_list = [value * 3.6 for value in power_x_list]
    power_y_list = [item for item in power_y_list if item is not None]


    se_quence = 4

    # for i in range(len(power_dia_list_pre)):
    #     se_quence = se_quence + 1
    #     insert_power_query = f"INSERT INTO factory_table (equipment, brand, model_short, model, rpm, data_type, se_quence, imp_dia, flow, kw) \
    #             VALUES ('equipment', 'brand', 'model_short', 'model', 'rpm', 'kw', '{se_quence_power_list[i]}', {power_dia_list_pre[i]}, {power_x_list[i]}, {power_y_list[i]})"
    #     cursor.execute(insert_power_query)
    #     mydb.commit()

    # try :
    #     for i in range(len(power_dia_list_pre)):
    #         print(power_dia_list_pre[i],power_x_list[i],power_y_list[i])
    # except:
    #     pass



    # print(power_dia_list)
    # print(len(id_power))
    # print(len(power_dia_list))
    # print(len(power_x_list))
    # print(len(power_y_list))






    ################################
    #NPSHR
    current_row = start_row 
    npshr_dia_list = []
    npshr_x_list = []
    npshr_y_list = []
    se_quence_npshr_1 = 4
    se_quence_npshr_2 = 4
    se_quence_npshr_3 = 4
    se_quence_npshr_4 = 4
    se_quence_npshr_5 = 4
    se_quence_npshr_6 = 4
    se_quence_npshr_list = []
    for _ in range(start_row, end_row + 1):


        cell_CZ = 'CZ' + str(current_row)
        cell_DA = 'DA' + str(current_row)
        npshr_x_1 = worksheet[cell_CZ].value
        npshr_x_list.append(npshr_x_1)
        npshr_y_1 = worksheet[cell_DA].value
        npshr_y_list.append(npshr_y_1)
        if npshr_x_1 != None:
            npshr_dia_1 = worksheet['CZ3'].value
            npshr_dia_list.append(npshr_dia_1)
            se_quence_npshr_1 += 1
            se_quence_npshr_list.append(se_quence_npshr_1)
        else:
            pass


        cell_DC = 'DC' + str(current_row)
        cell_DD = 'DD' + str(current_row)
        npshr_x_2 = worksheet[cell_DC].value
        npshr_x_list.append(npshr_x_2)
        npshr_y_2 = worksheet[cell_DD].value
        npshr_y_list.append(npshr_y_2)
        if npshr_x_2 != None:
            npshr_dia_2 = worksheet['DC3'].value
            npshr_dia_list.append(npshr_dia_2)
            se_quence_npshr_2 += 1
            se_quence_npshr_list.append(se_quence_npshr_2)
        else:
            pass
        
        cell_DF = 'DF' + str(current_row)
        cell_DG = 'DG' + str(current_row)
        npshr_x_3 = worksheet[cell_DF].value
        npshr_x_list.append(npshr_x_3)
        npshr_y_3 = worksheet[cell_DG].value
        npshr_y_list.append(npshr_y_3)
        if npshr_x_3 != None:
            npshr_dia_3 = worksheet['DF3'].value
            npshr_dia_list.append(npshr_dia_3)
            se_quence_npshr_3 += 1
            se_quence_npshr_list.append(se_quence_npshr_3)
        else:
            pass
        

        cell_DI = 'DI' + str(current_row)
        cell_DJ = 'DJ' + str(current_row)
        npshr_x_4 = worksheet[cell_DI].value
        npshr_x_list.append(npshr_x_4)
        npshr_y_4 = worksheet[cell_DJ].value
        npshr_y_list.append(npshr_x_4)

        if npshr_x_4 != None:
            npshr_dia_4 = worksheet['DI3'].value
            npshr_dia_list.append(npshr_dia_4)
            se_quence_npshr_4 += 1
            se_quence_npshr_list.append(se_quence_npshr_4)
        else:
            pass


        cell_DL = 'DL' + str(current_row)
        cell_DM = 'DM' + str(current_row)
        npshr_x_5 = worksheet[cell_DL].value
        npshr_x_list.append(npshr_x_5)
        npshr_y_5 = worksheet[cell_DM].value
        npshr_y_list.append(npshr_y_5)

        if npshr_x_5 != None:
            npshr_dia_5 = worksheet['DL3'].value
            npshr_dia_list.append(npshr_dia_5)
            se_quence_npshr_5 += 1
            se_quence_npshr_list.append(se_quence_npshr_5)
        else:
            pass

        cell_DO = 'DO' + str(current_row)
        cell_DP = 'DP' + str(current_row)
        npshr_x_6 = worksheet[cell_DO].value
        npshr_x_list.append(npshr_x_6)
        npshr_y_6 = worksheet[cell_DP].value
        npshr_y_list.append(npshr_y_6)

        if npshr_x_6 != None:
            npshr_dia_6 = worksheet['DO3'].value
            npshr_dia_list.append(npshr_dia_6)
            se_quence_npshr_6 += 1
            se_quence_npshr_list.append(se_quence_npshr_6)
        else:
            pass
        current_row += 1



    try:
        npshr_dia_list = [{item.replace('m', '')} for item in npshr_dia_list if item is not None]
    except ValueError:
        npshr_dia_list = [{item.replace(' m', '')} for item in npshr_dia_list if item is not None]

    
    # print(npshr_dia_list,".................")
    npshr_dia_list_pre = []

    for data in npshr_dia_list:
        npshr_dia_list_pre.append(float(data.pop()))

    npshr_x_list = [item for item in npshr_x_list if item is not None]
    npshr_x_list = [value * 3.6 for value in npshr_x_list]
    npshr_y_list = [item for item in npshr_y_list if item is not None]



    # print(npshr_x_list)

    # for i in range(len(npshr_dia_list)):
    #     se_quence = se_quence + 1
    #     insert_npshr_query = f"INSERT INTO factory_table (equipment, brand, model_short, model, rpm, data_type, se_quence, npshr, flow, head) \
    #             VALUES ('equipment', 'brand', 'model_short', 'model', 'rpm', 'npshr', '{se_quence_npshr_list[i]}', {npshr_dia_list_pre[i]}, {npshr_x_list[i]}, {npshr_y_list[i]})"
    #     cursor.execute(insert_npshr_query)
    #     mydb.commit()
    # for i in range(len(npshr_dia_list)):
    #     print(npshr_dia_list_pre[i],npshr_x_list[i],npshr_y_list[i])

    # cursor.close()
    
    return se_quence_imp_list, \
       imp_dia_list_pre, \
       imp_x_list, \
       imp_y_list, \
       se_quence_eff_list, \
       eff_cleaned, \
       eff_x_list, \
       eff_y_list, \
       eff_rl, \
       se_quence_power_list, \
       power_dia_list_pre, \
       power_x_list, \
       power_y_list, \
       se_quence_npshr_list,\
       npshr_dia_list_pre, \
       npshr_x_list,\
       npshr_y_list
       

# update_data_excel("FAC-0255-ORG.xlsx")