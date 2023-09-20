import base64
from io import BytesIO
import matplotlib.pyplot as plt
import math
import pandas as pd
from pumpselection.view.connectDB import mydb,mySQL
from pumpselection.view.showchart import sort_eff

def loaddata_kdin(fac_number, fflow, hhead, dfkdin):
    import numpy as np

    ###imp
    imp_x_list = []
    imp_y_list = []
    im_size_lst = (
        dfkdin.query(f"data_type == 'QH' and fac_number == '{fac_number}'")[
            "imp_dia"
        ]
        .unique()
        .tolist()
    )
    name = dfkdin.query(f"fac_number == '{fac_number}'")["model"].unique()
    if name:
        print("name_id",name)
        for imp_dia in im_size_lst:
            
            flows = dfkdin.query(
                f"data_type == 'QH' and imp_dia == {str(int(imp_dia))} and fac_number == '{fac_number}'"
            )["flow"].tolist()
            imp_x_list.append(flows)
            

            heads = dfkdin.query(
                f"data_type == 'QH' and imp_dia == {str(int(imp_dia))} and fac_number == '{fac_number}'"
            )["head"].tolist()
            imp_y_list.append(heads)

        # print(name,im_size_lst,'\n')

        # -------- Poly Method ----------
        max_lmpeller = np.max(im_size_lst)
        min_lmpeller = np.min(im_size_lst)

        imp_x_top = dfkdin.query(
            f"data_type == 'QH' and imp_dia == {str(int(max_lmpeller))} and fac_number == '{fac_number}'"
        )["flow"].tolist()
        imp_y_top =  dfkdin.query(
            f"data_type == 'QH' and imp_dia == {str(int(max_lmpeller))} and fac_number == '{fac_number}'"
        )["head"].tolist()
        imp_x_botton = dfkdin.query(
            f"data_type == 'QH' and imp_dia == {str(int(min_lmpeller))} and fac_number == '{fac_number}'"
        )["flow"].tolist()
        imp_y_botton = dfkdin.query(
            f"data_type == 'QH' and imp_dia == {str(int(min_lmpeller))} and fac_number == '{fac_number}'"
        )["head"].tolist()

        # print("flow",imp_x_top)
        # print("head",imp_y_top)

        imp_x_center_top = np.max(imp_x_top)
        imp_y_center_top = np.min(imp_y_top)

        imp_x_center_botton = np.max(imp_x_botton)
        imp_y_center_botton = np.min(imp_y_botton)

        center_data_x = ([imp_x_center_top,imp_x_center_botton])
        # print('x',center_data_x)
        center_data_y = ([imp_y_center_top,imp_y_center_botton])
        # print('y',center_data_y)
        degree = 2  # Specify the degree of the polynomial
        # print(len(imp_x_top))
        # print(len(imp_y_top))
        coefficients_top = np.polyfit(imp_x_top, imp_y_top, degree)
        coefficients_botton = np.polyfit(imp_x_botton, imp_y_botton, degree)
        coefficients_center = np.polyfit(center_data_x, center_data_y,1)


        # Calculate the y-coordinate for x = 5
        equation_top_func = np.poly1d(coefficients_top)
        equation_botton_func = np.poly1d(coefficients_botton)
        equation_center_func = np.poly1d(coefficients_center)

        # inputsection
        flow_input = float(fflow)  # รอรับจากลูกค้า
        Head_input = float(hhead)  # รอรับจากลูกค้า

        x_value = flow_input
        y_value_top = float(format(equation_top_func(x_value),'.2f'))
        y_value_botton = float(format(equation_botton_func(x_value),'.2f'))
        y_value_center = float(format(equation_center_func(x_value),'.2f'))

        # print(f"TOP For x = {x_value}, y = {y_value_top}")
        # print(f"BOT For x = {x_value}, y = {y_value_botton}")
        # print(f"CEN For x = {x_value}, y = {y_value_center}")

        (
            imp_x_1,
            imp_x_2,
            imp_x_3,
            imp_x_4,
            imp_x_5,
            imp_x_6,
            imp_x_7,
            imp_x_8,
            imp_x_9,
        ) = imp_x_list + [[0]] * (9 - len(im_size_lst))
        # print(flow_list)
        (
            imp_y_1,
            imp_y_2,
            imp_y_3,
            imp_y_4,
            imp_y_5,
            imp_y_6,
            imp_y_7,
            imp_y_8,
            imp_y_9,
        ) = imp_y_list + [[0]] * (9 - len(im_size_lst))
        # Impeller
        imp_data_x = [
            imp_x_1,
            imp_x_2,
            imp_x_3,
            imp_x_4,
            imp_x_5,
            imp_x_6,
            imp_x_7,
            imp_x_8,
            imp_x_9,
        ]
        # print(imp_data_x)
        imp_data_y = [
            imp_y_1,
            imp_y_2,
            imp_y_3,
            imp_y_4,
            imp_y_5,
            imp_y_6,
            imp_y_7,
            imp_y_8,
            imp_y_9,
        ]
        # print(imp_data_y)
        ###########################################
        ### kw
        power_x_list = []
        power_y_list = []

        kw_size_lst = (
            dfkdin.query(f"data_type == 'KW' and fac_number == '{fac_number}'")[
                "imp_dia"
            ]
            .unique()
            .tolist()
        )
        for kw_dia in kw_size_lst:
            flows = dfkdin.query(
                f"data_type == 'KW' and imp_dia == {kw_dia}and fac_number == '{fac_number}'"
            )["flow"].tolist()
            power_x_list.append(flows)

            heads = dfkdin.query(
                f"data_type == 'KW' and imp_dia == {kw_dia}and fac_number == '{fac_number}'"
            )["kw"].tolist()
            power_y_list.append(heads)

        (
            power_x_1,
            power_x_2,
            power_x_3,
            power_x_4,
            power_x_5,
            power_x_6,
            power_x_7,
            power_x_8,
            power_x_9,
        ) = power_x_list + [[0]] * (9 - len(kw_size_lst))
        # print(power_1)
        (
            power_y_1,
            power_y_2,
            power_y_3,
            power_y_4,
            power_y_5,
            power_y_6,
            power_y_7,
            power_y_8,
            power_y_9,
        ) = power_y_list + [[0]] * (9 - len(kw_size_lst))
        # print(flow_p_1)

        ###power
        power_data_x = [
            power_x_1,
            power_x_2,
            power_x_3,
            power_x_4,
            power_x_5,
            power_x_6,
            power_x_7,
            power_x_8,
            power_x_9,
        ]
        power_data_y = [
            power_y_1,
            power_y_2,
            power_y_3,
            power_y_4,
            power_y_5,
            power_y_6,
            power_y_7,
            power_y_8,
            power_y_9,
        ]
        #####################################
        ###npshr
        npshr_x_list = []
        npshr_y_list = []

        npshr_size_lst = (
            dfkdin.query(f"data_type == 'NPSHR' and fac_number == '{fac_number}'")[
                "imp_dia"
            ]
            .unique()
            .tolist()
        )
        # print(npshr_size_lst)
        for im_size in npshr_size_lst:
            flow_n = dfkdin.query(
                f"data_type =='NPSHR'and fac_number == '{fac_number}'and imp_dia =={im_size}"
            )["flow"].tolist()
            npshr_x_list.append(flow_n)

            head_n = dfkdin.query(
                f"data_type =='NPSHR' and fac_number == '{fac_number}'and imp_dia =={im_size}"
            )["npshr"].tolist()
            npshr_y_list.append(head_n)

        (
                npshr_x_1,
                npshr_x_2,
                npshr_x_3,
                npshr_x_4,
                npshr_x_5,
                npshr_x_6,
                npshr_x_7,
                npshr_x_8,
                npshr_x_9,
        ) = npshr_x_list + [[0]] * (9 - len(npshr_size_lst))

        (
            npshr_y_1,
            npshr_y_2,
            npshr_y_3,
            npshr_y_4,
            npshr_y_5,
            npshr_y_6,
            npshr_y_7,
            npshr_y_8,
            npshr_y_9,
        ) = npshr_y_list + [[0]] * (9 - len(npshr_size_lst))

        ##npshr
        npshr_data_x = [
            npshr_x_1,
            npshr_x_2,
            npshr_x_3,
            npshr_x_4,
            npshr_x_5,
            npshr_x_6,
            npshr_x_7,
            npshr_x_8,
            npshr_x_9,
        ]
        npshr_data_y = [
            npshr_y_1,
            npshr_y_2,
            npshr_y_3,
            npshr_y_4,
            npshr_y_5,
            npshr_y_6,
            npshr_y_7,
            npshr_y_8,
            npshr_y_9,
        ]

        ##################################
        # effS
        eff_x_list = []
        eff_y_list = []
        eff_size_lst = (
            dfkdin.query(f"data_type == 'EFF' and fac_number == '{fac_number}'")["eff"]
            .unique()
            .tolist()
        )

        for eff_size in eff_size_lst:
            eff_flow = (
                dfkdin.query(
                    f"data_type =='EFF' and eff =={eff_size}and fac_number == '{fac_number}'"
                )
                .sort_values("se_quence", ascending=True)["flow"]
                .tolist()
            )

            eff_x_list.append(eff_flow)

            # eff_flow_list.sort()
            eff_head = (
                dfkdin.query(
                    f"data_type =='EFF' and eff =={eff_size}and fac_number == '{fac_number}'"
                )
                .sort_values("se_quence", ascending=True)["head"]
                .tolist()
            )
            eff_y_list.append(eff_head)

        (
            eff_x_1,
            eff_x_2,
            eff_x_3,
            eff_x_4,
            eff_x_5,
            eff_x_6,
            eff_x_7,
            eff_x_8,
            eff_x_9,
        ) = eff_x_list + [[0]] * (9 - len(eff_size_lst))

        (
            eff_y_1,
            eff_y_2,
            eff_y_3,
            eff_y_4,
            eff_y_5,
            eff_y_6,
            eff_y_7,
            eff_y_8,
            eff_y_9,
        ) = eff_y_list + [[0]] * (9 - len(eff_size_lst))

        ###eff
        eff_data_x = [
            eff_x_1,
            eff_x_2,
            eff_x_3,
            eff_x_4,
            eff_x_5,
            eff_x_6,
            eff_x_7,
            eff_x_8,
            eff_x_9,
        ]
        eff_data_y = [
            eff_y_1,
            eff_y_2,
            eff_y_3,
            eff_y_4,
            eff_y_5,
            eff_y_6,
            eff_y_7,
            eff_y_8,
            eff_y_9,
        ]
        # ---------------------- Eff Plot Chart -------------------------------
        eff_x_list_plot = []
        eff_y_list_plot = []
        eff_size_lst_plot = (
            dfkdin.query(f"fac_number == '{fac_number}' and eff_rl !=''")["eff_rl"]
            .unique()
            .tolist()
        )


        for eff_size_plot in eff_size_lst_plot:
            eff_flow_plot = (
                dfkdin.query(
                    f"data_type =='EFF' and eff_rl == '{eff_size_plot}' and fac_number == '{fac_number}'"
                )
                .sort_values("se_quence", ascending=True)["flow"]
                .tolist()
            )
            # print("Flow :",eff_flow)
            eff_x_list_plot.append(eff_flow_plot)
            # eff_flow_list.sort()
            eff_head_plot = (
                dfkdin.query(
                    f"data_type =='EFF' and eff_rl == '{eff_size_plot}' and fac_number == '{fac_number}'"
                )
                .sort_values("se_quence", ascending=True)["head"]
                .tolist()
            )
            eff_y_list_plot.append(eff_head_plot)

            
        eff_size_lst_plot = sorted(eff_size_lst_plot)
        rightSelcet = 0
        # print('eff_size_lst_plot',eff_size_lst_plot)
        selected_indices = [i for i, item in enumerate(eff_size_lst_plot) if 'R' in item]
        for index in selected_indices:
            rightSelcet = index
            break
            
        # print(eff_y_list_plot)
        (
            eff_x_1_plot,
            eff_x_2_plot,
            eff_x_3_plot,
            eff_x_4_plot,
            eff_x_5_plot,
            eff_x_6_plot,
            eff_x_7_plot,
            eff_x_8_plot,
            eff_x_9_plot,
            eff_x_10_plot,
            eff_x_11_plot,
            eff_x_12_plot,
            eff_x_13_plot,
            eff_x_14_plot,
            eff_x_15_plot,
        ) = eff_x_list_plot + [[0]] * (15 - len(eff_size_lst_plot))

        (
            eff_y_1_plot,
            eff_y_2_plot,
            eff_y_3_plot,
            eff_y_4_plot,
            eff_y_5_plot,
            eff_y_6_plot,
            eff_y_7_plot,
            eff_y_8_plot,
            eff_y_9_plot,
            eff_y_10_plot,
            eff_y_11_plot,
            eff_y_12_plot,
            eff_y_13_plot,
            eff_y_14_plot,
            eff_y_15_plot,
        ) = eff_y_list_plot + [[0]] * (15 - len(eff_size_lst_plot))
        "----------------------------------------------------------------------"


        x_max = float(
            (
                max(
                    [
                        max(imp_x_1),
                        max(imp_x_2),
                        max(imp_x_3),
                        max(imp_x_4),
                        max(imp_x_5),
                        max(imp_x_6),
                        max(imp_x_7),
                        max(imp_x_8),
                        max(imp_x_9),
                    ]
                )
            )
        )
        x_min = float(
            (
                min(
                    [
                        min(imp_x_1),
                        min(imp_x_2),
                        min(imp_x_3),
                        min(imp_x_4),
                        min(imp_x_5),
                        min(imp_x_6),
                        min(imp_x_7),
                        min(imp_x_8),
                        min(imp_x_9),
                    ]
                )
            )
        )
        y_max = float(
            (
                max(
                    [
                        max(imp_y_1),
                        max(imp_y_2),
                        max(imp_y_3),
                        max(imp_y_4),
                        max(imp_y_5),
                        max(imp_y_6),
                        max(imp_y_7),
                        max(imp_y_8),
                        max(imp_y_9),
                    ]
                )
            )
        )
        y_min = float(
            (
                min(
                    [
                        min(imp_y_1),
                        min(imp_y_2),
                        min(imp_y_3),
                        min(imp_y_4),
                        min(imp_y_5),
                        min(imp_y_6),
                        min(imp_y_7),
                        min(imp_y_8),
                        min(imp_y_9),
                    ]
                )
            )
        )

        if rightSelcet is None:
            rightSelcet = len(eff_size_lst)-1

        # print('eff_size_lst_plot_sort',eff_size_lst_plot)
        # print('eff_size_lst_plot',eff_size_lst_plot[0])
        # print('eff_size_lst_plot',eff_size_lst_plot[rightSelcet])
        flow_input = float(fflow)  # รอรับจากลูกค้า
        Head_input = float(hhead)  # รอรับจากลูกค้า

        coefficients_eff_left = np.polyfit(eff_y_list_plot[0],eff_x_list_plot[0],degree)
        equation_func_eff_left = np.poly1d(coefficients_eff_left)
        x_y_check_eff_left = equation_func_eff_left(Head_input)

        coefficients_eff_right = np.polyfit(eff_y_list_plot[rightSelcet],eff_x_list_plot[rightSelcet],degree)
        equation_func_eff_right = np.poly1d(coefficients_eff_right)
        x_y_check_eff_right = equation_func_eff_right(Head_input)

        # print('x_y_check_eff_left',x_y_check_eff_left)
        # print('x_y_check_eff_right',x_y_check_eff_right)
        # print(type(y_value_top))
        # print(type(Head_input))
        # print( y_value_top > Head_input)
        # print( Head_input < y_value_botton)
        # print(Head_input > y_value_center)
        # print(name, y_value_top, y_value_botton,y_value_center,"\n")
        # (y_value_top < Head_input or Head_input > y_value_botton) and Head_input > y_value_center
        # ['KDIN40-32H 2900rpm'] y_value_top < Head_input or Head_input < y_value_botton or Head_input < y_value_center
        # Impeller (y_value_top > Head_input and y_value_botton < Head_input) and Head_input > y_value_center
        # y_value_top < Head_input or Head_input < y_value_botton or Head_input < y_value_center
        try:
            x, y = flow_input, Head_input
            if y_value_top < Head_input or Head_input < y_value_botton or Head_input < y_value_center:
                print("NOT PASS",fac_number)
                pass
            elif x_y_check_eff_left < flow_input:
                print("PASS",fac_number)
                target = np.array([x, y])
                print(target)
                def closest(lst, K):
                    lst = np.array(lst)
                    idx = (np.abs(lst - K)).argmin()
                    return lst[idx]

                def closest_point(points, target):
                    distances = np.sqrt(np.sum((points - target) ** 2, axis=1))
                    closest_index = np.argmin(distances)
                    return points[closest_index]

                ###################################################################################
               # Impeller dimension
                coefficients = []
                equation_func = []
                x_y_check = []
                
                for i in range(len(im_size_lst)):
                    coefficients.append(np.polyfit(imp_data_x[i], imp_data_y[i], degree))
                    equation_func.append(np.poly1d(coefficients[i]))
                    x_y_check.append((flow_input,equation_func[i](flow_input)))
                    
                ### imp_1
                # print('equation_func',x_y_check)
                
                imp_near_x_y1 = np.array(closest_point(x_y_check, target))
                imp_in_near_x_y1 = [i for i, value in enumerate(x_y_check) if value[0] == imp_near_x_y1[0] and value[1] == imp_near_x_y1[1]]
                # print('imp_in_near_x_y1',imp_in_near_x_y1)
                imp_in_near_x_y1 = imp_in_near_x_y1[0]
                x_y_check[imp_in_near_x_y1] = 0, 0

                # print('imp_in_near_x_y1',imp_in_near_x_y1)
                imp_near_x_y2 = np.array(closest_point(x_y_check, target))
                imp_in_near_x_y2 = [i for i, value in enumerate(x_y_check) if value[0] == imp_near_x_y2[0] and value[1] == imp_near_x_y2[1]]
                # print('imp_in_near_x_y2',imp_in_near_x_y2)
                imp_in_near_x_y2 = imp_in_near_x_y2[0]
                # print('imp_in_near_x_y2',imp_in_near_x_y2)

                # # print(imp_near_x_y1)
                # imp_in_near_x_y1 = [i for i, value in enumerate(x_y_check) if value[0] == imp_near_x_y1[0] and value[1] == imp_near_x_y1[1]]
                # print('imp_in_near_x_y1',imp_in_near_x_y1)
                # imp_in_near_x_y1 = imp_in_near_x_y1[0]
                # # print(imp_in_near_x_y1[0])
                # print('imp_in_near_x_y1',imp_in_near_x_y1)
                # x_y_check[imp_in_near_x_y1] = 0, 0

                # # print("x_y_check[imp_in_near_x_y1]",x_y_check)
                # imp_in_near_x_y2 = imp_in_near_x_y1 +1 
                # print("dwad",imp_in_near_x_y2)

                # imp_near_x_y2 = x_y_check[imp_in_near_x_y2]
                # # print(im_size_lst[imp_in_near_x_y2])
                # # print("imp_near_x_y1", imp_near_x_y1)
                # print("imp_near_x_y2", imp_near_x_y2)

                imp_dis_unit = abs(
                    im_size_lst[imp_in_near_x_y1] - im_size_lst[imp_in_near_x_y2]
                )
                
                imp_d1 = math.sqrt(
                    (imp_near_x_y2[0] - imp_near_x_y1[0]) ** 2
                    + (imp_near_x_y2[1] - imp_near_x_y1[1]) ** 2
                )
                imp_d2 = math.sqrt(
                    (imp_near_x_y1[0] - target[0]) ** 2 + (imp_near_x_y1[1] - target[1]) ** 2
                )
                # print("im_size_lst[imp_in_near_x_y1]", im_size_lst[imp_in_near_x_y1])
                # print("im_size_lst[imp_in_near_x_y2]", im_size_lst[imp_in_near_x_y2])
                # print("imp_dis_unit",imp_dis_unit)
                # print("imp_d1",imp_d1)
                # print("imp_d2",imp_d2)

                imp_dis_all = math.sqrt(
                    (imp_near_x_y2[0] - imp_near_x_y1[0]) ** 2
                    + (imp_near_x_y2[1] - imp_near_x_y1[1]) ** 2
                )

                imp_dis_clo_1 = math.sqrt(
                    (imp_near_x_y1[0] - target[0]) ** 2 + (imp_near_x_y1[1] - target[1]) ** 2
                )

                imp_dis_clo_2 = math.sqrt(
                    (imp_near_x_y2[0] - target[0]) ** 2 + (imp_near_x_y2[1] - target[1]) ** 2
                )

                # print("imp_dis_all",imp_dis_all)
                # print("imp_dis_clo_1",imp_dis_clo_1)
                # print("imp_dis_clo_2",imp_dis_clo_2)
                # print("imp_dis_all", imp_dis_all)
                # print("imp_dis_clo_1", imp_dis_clo_1)
                # print("imp_dis_clo_2", imp_dis_clo_2)
                imp_test = abs((imp_near_x_y1[1]-y) /y) * 100
                # print(imp_test)
                # if imp_test < 1:
                #     imp_output = im_size_lst[imp_in_near_x_y1]
                # print("im_size_lst[imp_in_near_x_y1]",im_size_lst[imp_in_near_x_y1])
                # print("im_size_lst[imp_in_near_x_y2]",im_size_lst[imp_in_near_x_y2])
                # print("imp_dis_all",imp_dis_all)
                # print("imp_dis_clo_2",imp_dis_clo_2)
                # print("imp_near_x_y2",imp_near_x_y2)
                # if imp_near_x_y2 == (0.0, 0.0):
                #     # print("ออก")
                #     return
                if im_size_lst[imp_in_near_x_y1] > im_size_lst[imp_in_near_x_y2]:
                    if imp_dis_all < imp_dis_clo_2:
                        imp_output = abs(
                            (imp_dis_unit * imp_d2 / imp_d1) + im_size_lst[imp_in_near_x_y1]
                        )
                    elif imp_dis_all > imp_dis_clo_2:
                        imp_output = abs(
                            (imp_dis_unit * imp_d2 / imp_d1) - im_size_lst[imp_in_near_x_y1]
                        )
                elif im_size_lst[imp_in_near_x_y1] < im_size_lst[imp_in_near_x_y2]:
                    if imp_dis_all < imp_dis_clo_2:
                        imp_output = abs(
                            (imp_dis_unit * imp_d2 / imp_d1) - im_size_lst[imp_in_near_x_y1]
                        )
                        
                    elif imp_dis_all > imp_dis_clo_2:
                        imp_output = abs(
                            (imp_dis_unit * imp_d2 / imp_d1) + im_size_lst[imp_in_near_x_y1]
                        )
             
                # if imp_output > max(im_size_lst):
                #     # print("imp เกินกราฟ")
                #     return
                # elif imp_output < min(im_size_lst):
                #     # print("imp ตกกราฟ")
                #     return
                # print("Fac-number",fac_number)
                # print("Impeller dimension is %f mm" % (imp_output))
                


                ####kw
                n_x1 = closest(kw_size_lst, imp_output)
                # print("kw",kw_size_lst)
                # print("imp_output",imp_output)
                t1 = kw_size_lst.index(n_x1)
                kw_size_lst[t1] = 0
                n_x2 = closest(kw_size_lst, imp_output)
                t2 = kw_size_lst.index(n_x2)

                # print("n_x1",n_x1)
                # print("n_x2",n_x2)
                # print("t1",t1)
                # print("t2",t2)
                kw_x1 = power_data_x[t1]
                kw_y1 = power_data_y[t1]
                near_x1 = closest(kw_x1, x)
                k1 = kw_x1.index(near_x1)
                near_y1 = kw_y1[k1]

                kw_x2 = power_data_x[t2]
                kw_y2 = power_data_y[t2]
                near_x2 = closest(kw_x2, x)
                k2 = kw_x2.index(near_x2)
                near_y2 = kw_y2[k2]

                dis_y_all = abs(near_y2 - near_y1)
                dis_unit = abs(n_x1 - n_x2)
                # print("n_x1",n_x1)
                # print("n_x2",n_x2)
                # print("near_y1",near_y1)
                # print("near_y2",near_y2)
                dis_y_unit = dis_y_all / dis_unit
                # print("dis_y_unit",dis_y_unit)
                if n_x1 > n_x2:
                    power = abs(dis_y_unit - near_y1)

                elif n_x1 < n_x2:
                    power = abs(dis_y_unit + near_y1)

                # print('Power requirment = %f kW' %(power))

                ## Efficiency
                # coefficients_eff = []
                # equation_func_eff = []
                # x_y_check_eff = []
                # for i in range(len(eff_size_lst)):
                #     coefficients_eff.append(np.polyfit(eff_data_x[i], eff_data_y[i], degree))
                #     equation_func_eff.append(np.poly1d(coefficients_eff[i]))
                #     x_y_check_eff.append((flow_input,equation_func_eff[i](flow_input)))
                # print("x_y_check_eff",x_y_check_eff)
                combiend_eff1 = list(zip(eff_data_x[0], eff_data_y[0]))
                combiend_eff2 = list(zip(eff_data_x[1], eff_data_y[1]))
                combiend_eff3 = list(zip(eff_data_x[2], eff_data_y[2]))
                combiend_eff4 = list(zip(eff_data_x[3], eff_data_y[3]))
                combiend_eff5 = list(zip(eff_data_x[4], eff_data_y[4]))
                combiend_eff6 = list(zip(eff_data_x[5], eff_data_y[5]))
                combiend_eff7 = list(zip(eff_data_x[6], eff_data_y[6]))
                combiend_eff8 = list(zip(eff_data_x[7], eff_data_y[7]))
                combiend_eff9 = list(zip(eff_data_x[8], eff_data_y[8]))
          
                try:
                    eff_list_fir = []
                    eff_list_fir.append(closest_point(combiend_eff1, target))
                    eff_list_fir.append(closest_point(combiend_eff2, target))
                    eff_list_fir.append(closest_point(combiend_eff3, target))
                    eff_list_fir.append(closest_point(combiend_eff4, target))
                    eff_list_fir.append(closest_point(combiend_eff5, target))
                    eff_list_fir.append(closest_point(combiend_eff6, target))
                    eff_list_fir.append(closest_point(combiend_eff7, target))
                    eff_list_fir.append(closest_point(combiend_eff8, target))
                    eff_list_fir.append(closest_point(combiend_eff9, target))
                except:
                    pass
                eff_near_x_y1 = np.array(closest_point(eff_list_fir, target))
                eff_in_near_x_y1 = [i for i, value in enumerate(eff_list_fir) if value[0] == eff_near_x_y1[0] and value[1] == eff_near_x_y1[1]]
                eff_in_near_x_y1 = eff_in_near_x_y1[0]
                eff_list_fir[eff_in_near_x_y1] = 0, 0

                # print("eff_in_near_x_y1", eff_in_near_x_y1)
                # print("eff_in_near_x_y2", eff_in_near_x_y2)

                # print("eff_list_fir", eff_list_fir)
                eff_near_x_y2 = np.array(closest_point(eff_list_fir, target))
                eff_in_near_x_y2 = [i for i, value in enumerate(eff_list_fir) if value[0] == eff_near_x_y2[0] and value[1] == eff_near_x_y2[1]]
                eff_in_near_x_y2 = eff_in_near_x_y2[0]
                # print("eff_list_fir",eff_list_fir)
                # print("eff_near_x_y1",eff_in_near_x_y1)
                # print("eff_near_x_y2",eff_in_near_x_y2)
                # print("eff_d1",eff_d1)
                # print("eff_d2",eff_d2)
                # print("eff_size_lst[eff_in_near_x_y1]",eff_size_lst[eff_in_near_x_y1])
                # print("eff_size_lst[eff_in_near_x_y2]",eff_size_lst[eff_in_near_x_y2])
                eff_dis_all = math.sqrt(
                    (eff_near_x_y2[0] - eff_near_x_y1[0]) ** 2
                    + (eff_near_x_y2[1] - eff_near_x_y1[1]) ** 2
                )

                eff_dis_clo_1 = math.sqrt(
                    (eff_near_x_y1[0] - target[0]) ** 2 + (eff_near_x_y1[1] - target[1]) ** 2
                )

                eff_dis_clo_2 = math.sqrt(
                    (eff_near_x_y2[0] - target[0]) ** 2 + (eff_near_x_y2[1] - target[1]) ** 2
                )

                # print("eff_dis_all",eff_dis_all)
                # print("eff_dis_clo_1",eff_dis_clo_1)
                # print("eff_dis_clo_2",eff_dis_clo_2)

                eff_dis_unit = abs(
                    eff_size_lst[eff_in_near_x_y1] - eff_size_lst[eff_in_near_x_y2]
                )
                eff_d1 = math.sqrt(
                    (eff_near_x_y2[0] - eff_near_x_y1[0]) ** 2
                    + (eff_near_x_y2[1] - eff_near_x_y1[1]) ** 2
                )
                eff_d2 = math.sqrt(
                    (eff_near_x_y1[0] - target[0]) ** 2 + (eff_near_x_y1[1] - target[1]) ** 2
                )
                if eff_size_lst[eff_in_near_x_y1] > eff_size_lst[eff_in_near_x_y2]:
                    if eff_dis_all < eff_dis_clo_2 and eff_dis_all < eff_dis_clo_1:
                        # print("[.....................]")
                        return
                    if eff_dis_all < eff_dis_clo_2:
                        eff_output = abs(
                            (eff_dis_unit * eff_d2 / eff_d1) + eff_size_lst[eff_in_near_x_y1]
                        )
                    elif eff_dis_all > eff_dis_clo_2:
                        eff_output = abs(
                            (eff_dis_unit * eff_d2 / eff_d1) - eff_size_lst[eff_in_near_x_y1]
                        )

                elif eff_size_lst[eff_in_near_x_y1] < eff_size_lst[eff_in_near_x_y2]:
                    if eff_dis_all < eff_dis_clo_2 and eff_dis_all < eff_dis_clo_1:
                        # print("[.....................]")
                        return
                    if eff_dis_all < eff_dis_clo_2:
                        eff_output = abs(
                            (eff_dis_unit * eff_d2 / eff_d1) - eff_size_lst[eff_in_near_x_y1]
                        )
                    elif eff_dis_all > eff_dis_clo_2:
                        eff_output = abs(
                            (eff_dis_unit * eff_d2 / eff_d1) + eff_size_lst[eff_in_near_x_y1]
                        )
                    # print('Efficiency is = %f percent'%(eff_output))
                
                if eff_output >= max(eff_size_lst):
                    eff_output = max(eff_size_lst)
                elif eff_output < min(eff_size_lst):
                    # print("ค่าeffไม่ถึง")
                    return
                # print("Efficiency is = %f percent" % (eff_output))

                # Power
                pgnq = (1000 * 9.81 * y * (x / 3600)) / 1000
                eff_pre = eff_output / 100
                power = pgnq / eff_pre
                # print("Power requirment = %f kW" % (power))

                # NPSHR
                npshr_near_x = closest(npshr_x_1, x)
                npshr_near_in = npshr_x_1.index(npshr_near_x)
                npshr_near_y = npshr_y_1[npshr_near_in]
            
                pre_eff1 = list(zip(eff_data_x[0], eff_data_y[0]))
                pre_eff2 = list(zip(eff_data_x[1], eff_data_y[1]))
                pre_eff3 = list(zip(eff_data_x[2], eff_data_y[2]))
                pre_eff4 = list(zip(eff_data_x[3], eff_data_y[3]))
                pre_eff5 = list(zip(eff_data_x[4], eff_data_y[4]))
                pre_eff6 = list(zip(eff_data_x[5], eff_data_y[5]))
                pre_eff7 = list(zip(eff_data_x[6], eff_data_y[6]))
                pre_eff8 = list(zip(eff_data_x[7], eff_data_y[8]))
                pre_eff9 = list(zip(eff_data_x[8], eff_data_y[8]))



                empty_data = ([], [])
                try:
                    ready_eff1_x, ready_eff1_y = sort_eff(pre_eff1)
                except:
                    ready_eff1_x, ready_eff1_y = empty_data
                try:
                    ready_eff2_x, ready_eff2_y = sort_eff(pre_eff2)
                except:
                    ready_eff2_x, ready_eff2_y = empty_data
                try:
                    ready_eff3_x, ready_eff3_y = sort_eff(pre_eff3)
                except:
                    ready_eff3_x, ready_eff3_y = empty_data
                try:
                    ready_eff4_x, ready_eff4_y = sort_eff(pre_eff4)
                except:
                    ready_eff4_x, ready_eff4_y = empty_data
                try:
                    ready_eff5_x, ready_eff5_y = sort_eff(pre_eff5)
                except:
                    ready_eff5_x, ready_eff5_y = empty_data
                try:
                    ready_eff6_x, ready_eff6_y = sort_eff(pre_eff6)
                except:
                    ready_eff6_x, ready_eff6_y = empty_data
                try:
                    ready_eff7_x, ready_eff7_y = sort_eff(pre_eff7)
                except:
                    ready_eff7_x, ready_eff7_y = empty_data
                try:
                    ready_eff8_x, ready_eff8_y = sort_eff(pre_eff8)
                except:
                    ready_eff8_x, ready_eff8_y = empty_data
                try:
                    ready_eff9_x, ready_eff9_y = sort_eff(pre_eff9)
                except:
                    ready_eff9_x, ready_eff9_y = empty_data

                ready_eff_x_list = [ready_eff1_x, ready_eff2_x, ready_eff3_x, ready_eff4_x, ready_eff5_x, ready_eff6_x, ready_eff7_x, ready_eff8_x, ready_eff9_x]
                ready_eff_y_list = [ready_eff1_y, ready_eff2_y, ready_eff3_y, ready_eff4_y, ready_eff5_y, ready_eff6_y, ready_eff7_y, ready_eff8_y, ready_eff9_y]

                chart = get_plot(fac_number,name,im_size_lst,imp_data_x,imp_data_y,eff_size_lst_plot,eff_x_list_plot,eff_y_list_plot,eff_size_lst,ready_eff_x_list,ready_eff_y_list,flow_input,Head_input,imp_output, eff_output, power, npshr_near_y)
                # print("Impeller dimension is %f mm" % (imp_output))
                # print('Power requirment = %f kW' %(power))
                # print("Efficiency is = %f percent" % (eff_output))
                # print('NPSHr is %f m'%npshr_near_y)
            
                return name, imp_output, eff_output, power, npshr_near_y,chart
        except:
            pass


def get_plot(fac_number,name,im_size_lst,imp_data_x,imp_data_y,eff_size_lst_plot,eff_x_list_plot,eff_y_list_plot,eff_size_lst,eff_x_list,eff_y_list,flow_input,Head_input,imp_output, eff_output, power, npshr_output):
    fix, ax = plt.subplots(figsize=(5,5))
    # plt.switch_backend('AGG')
    for i in range(len(im_size_lst)):
        ax.plot(imp_data_x[i], imp_data_y[i],linewidth=0.5,color='black')
        
    # for i in range(len(eff_size_lst)):
    #     plt.plot(eff_x_list[i], eff_y_list[i],)
    for i in range(len(eff_size_lst_plot)):
        ax.plot(eff_x_list_plot[i], eff_y_list_plot[i],linewidth=1, color='blue')
    ax.set_ylabel("Head")
    ax.set_xlabel("Flow")
    plt.title(name)
    for i in range(len(im_size_lst)):
        ax.text(imp_data_x[i][0], imp_data_y[i][0], f"{im_size_lst[i]}mm")
    for i in range(len(eff_size_lst)):
        ax.text(eff_x_list[i][0], eff_y_list[i]
                 [0], f"{eff_size_lst[i]}%")
        ax.text(eff_x_list[i][-1], eff_y_list[i]
                 [-1], f"{eff_size_lst[i]}%")
    ax.plot(flow_input, Head_input, marker='.', markersize=5,color='red')
    ax.text(0, 0, f"Fac-number: {fac_number}\nFlow: {flow_input}\nHead: {Head_input}\nImpeller dimension: {imp_output:.2f}mm\nEfficiency: {eff_output:.2f} %\nPower requirement: {power:.2f} kw\nNPSHr: {npshr_output:.2f} m")
    flow_chart = flow_input
    head_chart = Head_input
    x_head_input = []
    y_head_input = []
    while head_chart > 0.0:
        x_head_input.append(flow_input)
        y_head_input.append(head_chart - 0.1)
        head_chart -= 0.1
    ax.plot(x_head_input, y_head_input, color='red',linewidth=0.5)
    # print(x_head_input, y_head_input)
    x_flow_input = []
    y_flow_input = []
    while flow_chart > 0.0:
        x_flow_input.append(flow_chart - 0.1)
        y_flow_input.append(Head_input)
        flow_chart -= 0.1
    ax.plot(x_flow_input, y_flow_input,color='red',linewidth=0.5)
    # plt.xticks(rotation=45)
    ax.minorticks_on()
    

    
    graph = get_graph()
    
    return graph


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png',dpi=500)
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

# loaddata_kdin('FAC-0022', 100, 40,mySQL("KDIN"))