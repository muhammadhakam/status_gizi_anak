from flask import Flask, render_template, request
import pandas as pd

Flask_App = Flask(__name__) # Creating our Flask Instance

@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """
    
    return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
    """Route where we send calculator form input"""

    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name= "
    jk_a = request.form['jk']  
    age_a = request.form['age']
    pb_a = request.form['pb']
    bb_a = request.form['bb']
    lingkar_a = request.form['lingkar']
    Lila_a = request.form['Lila']

    try:
        jk = jk_a
        age_int = int(age_a) + 1
        pb_int = float(pb_a)
        bb_int = float(bb_a)
        lingkar_int = float(lingkar_a)
        Lila_int = float(Lila_a)
        
        #fungsi PB fro Age------------------------------------------------------------------------------------------------------
        median_pb = "pb_for_age.xlsx"
        df_median_pb = pd.read_excel(median_pb, sheet_name=jk ,usecols="C", nrows=age_int)
        last_item_pb = df_median_pb.to_numpy()
        data_median_pb = last_item_pb[-1]

        df_sd_pb = pd.read_excel(median_pb, sheet_name=jk ,usecols="J", nrows=age_int)
        last_item_pb = df_sd_pb.to_numpy()
        data_sd_pb = last_item_pb[-1]

        df_sdneg_pb = pd.read_excel(median_pb, sheet_name=jk ,usecols="H", nrows=age_int)
        last_item_pb = df_sdneg_pb.to_numpy()
        data_sdneg_pb = last_item_pb[-1]


        if pb_int<data_median_pb:
            zScore_pb = (pb_int-data_median_pb)/(data_median_pb-data_sdneg_pb)
        else :
            zScore_pb = (pb_int-data_median_pb)/(data_sd_pb-data_median_pb)
    
        if zScore_pb<-3:
            kondisi_pb = "Sangat Pendek (Severely Stunted)"
        elif -3<=zScore_pb<-2:
            kondisi_pb = "Pendek (Stunted)"
        elif -2<=zScore_pb<3:
            kondisi_pb = "Normal"
        else :
            kondisi_pb ="Tinggi"
        #-----------------------------------------------------------------------------------------------------------
        
        #fungsi BB for Age-----------------------------------------------------------------------------------------------------------------
        median_bb = "bb_for_age.xlsx"
        df_median_bb = pd.read_excel(median_bb, sheet_name=jk ,usecols="C", nrows=age_int)
        last_item_bb = df_median_bb.to_numpy()
        data_median_bb = last_item_bb[-1]

        sd_bb = "bb_for_age.xlsx"
        df_sd_bb = pd.read_excel(median_bb, sheet_name=jk ,usecols="I", nrows=age_int)
        last_item_bb = df_sd_bb.to_numpy()
        data_sd_bb = last_item_bb[-1]

        sdneg_bb = "bb_for_age.xlsx"
        df_sdneg_bb = pd.read_excel(median_bb, sheet_name=jk ,usecols="G", nrows=age_int)
        last_item_bb = df_sdneg_bb.to_numpy()
        data_sdneg_bb = last_item_bb[-1]


        if bb_int<data_median_bb:
            zScore_bb = (bb_int-data_median_bb)/(data_median_bb-data_sdneg_bb)
        else :
            zScore_bb = (bb_int-data_median_bb)/(data_sd_bb-data_median_bb)
            
        if zScore_bb<-3:
            kondisi_bb = "Sangat Badan Sangat Kurang (Severely Underweight)"
        elif -3<=zScore_bb<-2:
            kondisi_bb = "Berat Badan Kurang (Underweight)"
        elif -2<=zScore_bb<1:
            kondisi_bb = "Berat Badan Normal"
        else :
            kondisi_bb ="Resiko berat badan lebih"
        #------------------------------------------------------------------------------------------------------------------------------------------------------------
        #fungsi BB for PB------------------------------------------------------------------------------------------------------------------
        median = "bb_for_pb.xlsx"
        df_median = pd.read_excel(median, sheet_name=jk ,usecols="A,C")
        df = df_median.set_index('LENGTH')
        data_index = df.loc[[pb_int]]
        data_median = data_index.to_numpy()

        sd = "bb_for_pb.xlsx"
        df_sd = pd.read_excel(sd, sheet_name=jk ,usecols="A,I")
        df = df_sd.set_index('LENGTH')
        data_index = df.loc[[pb_int]]
        data_sd = data_index.to_numpy()

        sdneg = "bb_for_pb.xlsx"
        df_sdneg = pd.read_excel(sd, sheet_name=jk ,usecols="A,I")
        df = df_sdneg.set_index('LENGTH')
        data_index = df.loc[[pb_int]]
        data_sdneg = data_index.to_numpy()


        if bb_int<data_median:
            zScore = (bb_int-data_median)/(data_median-data_sdneg)
        else :
            zScore = (bb_int-data_median)/(data_sd-data_median)
            
        if zScore<-3:
            kondisi = "Gizi Buruk"
        elif -3<=zScore<-2:
            kondisi = "Gizi Kurang"
        elif -2<=zScore<1:
            kondisi = "Gizi Baik (Normal)"
        elif 1<zScore<=2:
            kondisi = "Beresiko Gizi Lebih"
        elif 2<zScore<=3:
            kondisi = "Gizi Lebih"
        else :
            kondisi ="Obesitas"


        #-------------------------------------------------------------------------------------------------------

        #Fungsi Lila---------------------------------------------------
        if Lila_int < 11.5 :
            kondisi_Lila = "Gizi Buruk"
        elif 11.5 <= Lila_int < 12.4 :
            kondisi_Lila = "Gizi Kurang"
        else :
            kondisi_Lila = "Gizi Baik"
        
        #fungsi lingkar Kepala-------------------------------------------------------------
        median_lingkar = "pb_for_age.xlsx"
        df_median_lingkar = pd.read_excel(median_lingkar, sheet_name=jk ,usecols="C", nrows=age_int)
        last_item_lingkar = df_median_lingkar.to_numpy()
        data_median_lingkar = last_item_lingkar[-1]

        sd_lingkar = "pb_for_age.xlsx"
        df_sd_lingkar = pd.read_excel(median_lingkar, sheet_name=jk ,usecols="J", nrows=age_int)
        last_item_lingkar = df_sd_lingkar.to_numpy()
        data_sd_lingkar = last_item_lingkar[-1]

        sdneg_lingkar = "pb_for_age.xlsx"
        df_sdneg_lingkar = pd.read_excel(median_lingkar, sheet_name=jk ,usecols="H", nrows=age_int)
        last_item_lingkar = df_sdneg_lingkar.to_numpy()
        data_sdneg_lingkar = last_item_lingkar[-1]


        if pb_int<data_median_lingkar:
            zScore_lingkar = (lingkar_int-data_median_lingkar)/(data_median_lingkar-data_sdneg_lingkar)
        else :
            zScore_lingkar = (lingkar_int-data_median_lingkar)/(data_sd_lingkar-data_median_lingkar)
            
        if zScore_lingkar<-3:
            kondisi_lingkar = "Sangat kecil"
        elif -3<=zScore_lingkar<-2:
            kondisi_lingkar = "Kecil"
        elif -2<=zScore_lingkar<=2:
            kondisi_lingkar = "Normal"
        else :
            kondisi_lingzScore_lingkar ="Sangat Besar"

        return render_template(
            'index.html',
            kondisi_pb=kondisi_pb,
            kondisi_bb=kondisi_bb,
            kondisi=kondisi,
            kondisi_Lila=kondisi_Lila,
            kondisi_lingkar=kondisi_lingkar,
            zScore_pb=zScore_pb,
            zScore_bb=zScore_bb,
            zScore=zScore,
            zScore_lingkar=zScore_lingkar,
            calculation_success=True
        )
        
    except ZeroDivisionError:
        return render_template(
            'index.html',
            calculation_success=False,
            error="You cannot divide by zero"
        )
        
    except ValueError:
        return render_template(
            'index.html',
            calculation_success=False,
            error="Cannot perform numeric operations with provided input"
        )

if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()
