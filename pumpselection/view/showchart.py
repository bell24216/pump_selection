import matplotlib.pyplot as plt
import pandas as pd
from pumpselection.view.connectDB import mydb
import base64
from io import BytesIO

def chart_kdin(fac_number,im_size_lst,kw_size_lst,eff_size_lst,npshr_size_lst):
    factory = pd.read_sql(f"SELECT fac_number,model_short,data_type,rpm,imp_dia,flow,head,eff,npshr,kw,model,se_quence,eff_rl FROM factory_table WHERE fac_number = '{fac_number}' ", con=mydb)
    imp_x_list = []
    imp_y_list = []
    for imp_dia in im_size_lst:
        flows = factory.query(
            f"data_type == 'QH' and imp_dia == {str(int(imp_dia))} and fac_number == '{fac_number}'"
        )["flow"].tolist()
        imp_x_list.append(flows)
        heads = factory.query(
            f"data_type == 'QH' and imp_dia == {str(int(imp_dia))} and fac_number == '{fac_number}'"
        )["head"].tolist()
        imp_y_list.append(heads)
    (imp_x_1,imp_x_2,imp_x_3,imp_x_4,imp_x_5,imp_x_6,imp_x_7,imp_x_8,imp_x_9,) = imp_x_list + [[0]] * (9 - len(im_size_lst))
    (imp_y_1,imp_y_2,imp_y_3,imp_y_4,imp_y_5,imp_y_6,imp_y_7,imp_y_8,imp_y_9,) = imp_y_list + [[0]] * (9 - len(im_size_lst))
    imp_data_x = [imp_x_1,imp_x_2,imp_x_3,imp_x_4,imp_x_5,imp_x_6,imp_x_7,imp_x_8,imp_x_9,]
    imp_data_y = [imp_y_1,imp_y_2,imp_y_3,imp_y_4,imp_y_5,imp_y_6,imp_y_7,imp_y_8,imp_y_9,]
############################################################################################################################################
    power_x_list = []
    power_y_list = []
    for kw_dia in kw_size_lst:
        flows = factory.query(
            f"data_type == 'KW' and imp_dia == {kw_dia}and fac_number == '{fac_number}'"
        )["flow"].tolist()
        power_x_list.append(flows)
        heads = factory.query(
            f"data_type == 'KW' and imp_dia == {kw_dia}and fac_number == '{fac_number}'"
        )["kw"].tolist()
        power_y_list.append(heads)
    (power_x_1,power_x_2,power_x_3,power_x_4,power_x_5,power_x_6,power_x_7,power_x_8,power_x_9,) = power_x_list + [[0]] * (9 - len(kw_size_lst))
    (power_y_1,power_y_2,power_y_3,power_y_4,power_y_5,power_y_6,power_y_7,power_y_8,power_y_9,) = power_y_list + [[0]] * (9 - len(kw_size_lst))
    power_data_x = [power_x_1,power_x_2,power_x_3,power_x_4,power_x_5,power_x_6,power_x_7,power_x_8,power_x_9,]
    power_data_y = [power_y_1,power_y_2,power_y_3,power_y_4,power_y_5,power_y_6,power_y_7,power_y_8,power_y_9,]
##########################################################################################################################################
    eff_x_list = []
    eff_y_list = []
    # print(eff_size_lst)
    for eff_size_plot in eff_size_lst:
        eff_flow_plot = (
            factory.query(
                f"data_type =='EFF' and eff_rl == '{eff_size_plot}' and fac_number == '{fac_number}'"
            )
            .sort_values("se_quence", ascending=True)["flow"]
            .tolist()
        )
        # print("Flow :",eff_flow)
        eff_x_list.append(eff_flow_plot)
        # eff_flow_list.sort()
        eff_head_plot = (
            factory.query(
                f"data_type =='EFF' and eff_rl == '{eff_size_plot}' and fac_number == '{fac_number}'"
            )
            .sort_values("se_quence", ascending=True)["head"]
            .tolist()
        )
        eff_y_list.append(eff_head_plot)
    (eff_x_1,eff_x_2,eff_x_3,eff_x_4,eff_x_5,eff_x_6,eff_x_7,eff_x_8,eff_x_9,) = eff_x_list + [[0]] * (9 - len(eff_size_lst))
    (eff_y_1,eff_y_2,eff_y_3,eff_y_4,eff_y_5,eff_y_6,eff_y_7,eff_y_8,eff_y_9,) = eff_y_list + [[0]] * (9 - len(eff_size_lst))
    eff_data_x = [eff_x_1,eff_x_2,eff_x_3,eff_x_4,eff_x_5,eff_x_6,eff_x_7,eff_x_8,eff_x_9,]
    eff_data_y = [eff_y_1,eff_y_2,eff_y_3,eff_y_4,eff_y_5,eff_y_6,eff_y_7,eff_y_8,eff_y_9,]
############################################################################################################################################
    npshr_x_list = []
    npshr_y_list = []
    for im_size in npshr_size_lst:
        flow_n = factory.query(
            f"data_type =='NPSHR'and fac_number == '{fac_number}'and imp_dia =={im_size}"
        )["flow"].tolist()
        npshr_x_list.append(flow_n)
        head_n = factory.query(
            f"data_type =='NPSHR' and fac_number == '{fac_number}'and imp_dia =={im_size}"
        )["npshr"].tolist()
        npshr_y_list.append(head_n)

    (npshr_x_1,npshr_x_2,npshr_x_3,npshr_x_4,npshr_x_5,npshr_x_6,npshr_x_7,npshr_x_8,npshr_x_9,) = npshr_x_list + [[0]] * (9 - len(npshr_size_lst))
    (npshr_y_1,npshr_y_2,npshr_y_3,npshr_y_4,npshr_y_5,npshr_y_6,npshr_y_7,npshr_y_8,npshr_y_9,) = npshr_y_list + [[0]] * (9 - len(npshr_size_lst))
    npshr_data_x = [npshr_x_1,npshr_x_2,npshr_x_3,npshr_x_4,npshr_x_5,npshr_x_6,npshr_x_7,npshr_x_8,npshr_x_9,]
    npshr_data_y = [npshr_y_1,npshr_y_2,npshr_y_3,npshr_y_4,npshr_y_5,npshr_y_6,npshr_y_7,npshr_y_8,npshr_y_9,]
#################################################################################################################################################
    # print(len(imp_data_x))
    # print(len(imp_data_y))


    fig, axs = plt.subplots(2, 2, figsize=(10, 10))  # กำหนดขนาดให้เหมาะสม

    # สร้างกราฟและเพิ่มข้อมูลใน subplot แต่ละตัว
    for i in range(len(im_size_lst)):
        axs[0][0].plot(imp_data_x[i], imp_data_y[i], linewidth=0.5, color='black')
        axs[0][0].text(imp_data_x[i][0], imp_data_y[i][0], f"{im_size_lst[i]}mm")
    axs[0][0].set_title("Impeller dimension")

    for i in range(len(eff_size_lst)):
        axs[0][1].plot(eff_data_x[i], eff_data_y[i], linewidth=0.5, color='black')
        axs[0][1].text(eff_x_list[i][0], eff_y_list[i][0], f"{eff_size_lst[i]}%")
    axs[0][1].set_title("Efficiency")

    for i in range(len(kw_size_lst)):
        axs[1][0].plot(power_data_x[i], power_data_y[i], linewidth=0.5, color='black')
        axs[1][0].text(power_x_list[i][-1], power_y_list[i][-1], f"{kw_size_lst[i]}mm")
    axs[1][0].set_title("Power required")

    for i in range(len(npshr_size_lst)):
        axs[1][1].plot(npshr_data_x[i], npshr_data_y[i], linewidth=0.5, color='black')
        axs[1][1].text(npshr_x_list[i][-1], npshr_y_list[i][-1], f"{npshr_size_lst[i]}mm")
    axs[1][1].set_title("NPSHR")

    plt.tight_layout()
    fig = plt.gcf()

    graph = get_graph()
    
    return graph

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png',dpi=1000)
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph