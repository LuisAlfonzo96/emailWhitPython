import pymysql 
reporte_inversor1_neiva = []
reporte_inversor2_neiva = []
reporte_inversor3_neiva = []
reporte_inversor1_mosquera = []
reporte_inversor2_mosquera = []
reporte_inversor1_medellin_p12 = []
reporte_inversor2_medellin_p12 = []
reporte_inversor3_medellin_p12 = []
reporte_inversor1_medellin_tn = []
reporte_inversor2_medellin_tn = []
reporte_inversor1_medellin_p6 = []
reporte_inversor2_medellin_p6 = []
reporte_inversor3_medellin_p6 = []
reporte_inversor1_giron = []
reporte_inversor2_giron = []
reporte_inversor3_giron = []
reporte_inversor4_giron = []
reporte_inversor5_giron = []
reporte_inversor6_giron = []
reporte_inversor1_monteria = []
reporte_inversor2_monteria = []
reporte_inversor1_cartagena = []
reporte_inversor2_cartagena = []
reporte_inversor3_cartagena = []
reporte_inversor4_cartagena = []
reporte_inversor1_valledupar_hangar = []
reporte_inversor2_valledupar_hangar = []
reporte_inversor3_valledupar_hangar = []
reporte_inversor4_valledupar_hangar = []
reporte_inversor5_valledupar_hangar = []
reporte_inversor6_valledupar_hangar = []
reporte_inversor1_valledupar_riego = []
reporte_inversor2_valledupar_riego = []
reporte_inversor3_valledupar_riego = []

def obtener_conexion():
    return pymysql.connect(host='mysql.engenius.com.co',
                                user='infovisitas',
                                password='desarrollo2020'
                                )
def consultaBD(fechaInicio, fechaFinal):
    #SEMANAL
    query_semanal_neiva_inv1 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66f4951876687205222' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_neiva_inv2 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '6704951876687205326' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_neiva_inv3 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '6744951876687205129' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_mosquera_inv1 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66c54498366871952' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_mosquera_inv2 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66854498366871952' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC"
    query_semanal_medellin_inv1_p12 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '6714951876687205329' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC"
    query_semanal_medellin_inv2_p12 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '6704951876687204835' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_medellin_inv3_p12 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '6664951876687205226' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_medellin_inv1_tn ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '6704951876687204835' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_medellin_inv2_tn ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66a4951876687204832' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_medellin_inv1_p6 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66d4951876687205218' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_medellin_inv2_p6 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66c4951876687205127' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_medellin_inv3_p6 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66b4951876687204837' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_giron_inv1 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '6694951876687205125' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_giron_inv2 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66e4951876687205128' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_giron_inv3 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '6644951876687205123' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_giron_inv4 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66b4951876687205027' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_giron_inv5 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66a4951876687205029' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_giron_inv6 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66d4951876687205334' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_monteria_inv1 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66a4951876687204839' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_monteria_inv2 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66e4951876687205034' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_cartagena_inv1 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66a4951876687204839' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_cartagena_inv2 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66e4951876687205031' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_cartagena_inv3 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66e4951876687205034' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_cartagena_inv4 ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '6724951876687205324' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_valledupar_inv1_hangar ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66f4951876687205132' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_valledupar_inv2_hangar ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66e4951876687205328' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_valledupar_inv3_hangar ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66c4951876687204836' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_valledupar_inv4_hangar ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66b4951876687205131' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_valledupar_inv5_hangar ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66b4951876687205032' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_valledupar_inv6_hangar ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/5040) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '6684951876687205130' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_valledupar_inv1_riego ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/10080) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66e4951876687205217' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_valledupar_inv2_riego ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/10080) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '66b4951876687205332' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
    query_semanal_valledupar_inv3_riego ="SELECT COUNT(*) as Conteo, (COUNT(*)*100/10080) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon FROM `central_saas`.Data_Sena WHERE SER = '6664951876687205333' AND FECHA BETWEEN '" + fechaInicio + "' AND '" + fechaFinal + "' ORDER BY FECHA DESC" 
  # DIARIO 
#     query_neiva_inv1 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66f4951876687205222' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_neiva_inv2 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '6704951876687205326' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_neiva_inv3 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '6744951876687205129' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_mosquera_inv1 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66c54498366871952' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_mosquera_inv2 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66854498366871952' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_medellin_inv1_p12 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '6714951876687205329' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_medellin_inv2_p12 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '6704951876687204835' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_medellin_inv3_p12 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '6664951876687205226' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_medellin_inv1_tn = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '6704951876687204835' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_medellin_inv2_tn = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66a4951876687204832' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_medellin_inv1_p6 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66d4951876687205218' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_medellin_inv2_p6 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66c4951876687205127' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_medellin_inv3_p6 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66b4951876687204837' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_giron_inv1 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '6694951876687205125' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_giron_inv2 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66e4951876687205128' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_giron_inv3 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '6644951876687205123' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_giron_inv4 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66b4951876687205027' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_giron_inv5 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66a4951876687205029' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_giron_inv6 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66d4951876687205334' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_monteria_inv1 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66a4951876687204839' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_monteria_inv2 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66e4951876687205034' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_cartagena_inv1 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66a4951876687204839' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_cartagena_inv2 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66e4951876687205031' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_cartagena_inv3 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66e4951876687205034' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_cartagena_inv4 = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '6724951876687205324' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_valledupar_inv1_hangar = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66f4951876687205132' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_valledupar_inv2_hangar = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66e4951876687205328' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_valledupar_inv3_hangar = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66c4951876687204836' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_valledupar_inv4_hangar = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66b4951876687205131' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_valledupar_inv5_hangar = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66b4951876687205032' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_valledupar_inv6_hangar = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/720) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '6684951876687205130' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_valledupar_inv1_riego = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/1440) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66e4951876687205217' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_valledupar_inv2_riego = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/1440) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '66b4951876687205332' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
#     query_valledupar_inv3_riego = "SELECT COUNT(*) as Conteo, (COUNT(*)*100/1440) as Porcentaje, (MAX(CAST(E_G as DECIMAL(10,2))) - MIN(CAST(E_G as DECIMAL(10,2))))/10000 EnergiaGen, ((MAX(CAST(E_C1 as DECIMAL(10,2))) + MAX(CAST(E_C2 as DECIMAL(10,2))) + MAX(CAST(E_C3 as DECIMAL(10,2)))) - (MIN(CAST(E_C1 as DECIMAL(10,2))) + MIN(CAST(E_C2 as DECIMAL(10,2))) + MIN(CAST(E_C3 as DECIMAL(10,2)))))/10000 as EnergiaCon  FROM `central_saas`.Data_Sena WHERE SER = '6664951876687205333' AND FECHA BETWEEN '2022-03-15 00:00:00' AND '2022-03-15 23:59:59' ORDER BY FECHA DESC"
    bd = obtener_conexion()
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_neiva_inv1)
            datos = cursor.fetchall()
            tupla_db, = datos
            reporte_inversor1_neiva.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3], 'neiva_inv1'])
            # print(reporte_inversor1_neiva, 'est es el segundo prin')
            # print(tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3], 'neiva_inv1')
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_neiva_inv2)
            datos = cursor.fetchall()
            tupla_db, = datos
            reporte_inversor2_neiva.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_neiva_inv3)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor3_neiva.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_mosquera_inv1)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor1_mosquera.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_mosquera_inv2)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor2_mosquera.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_medellin_inv1_p12)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor1_medellin_p12.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_medellin_inv2_p12)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor2_medellin_p12.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_medellin_inv3_p12)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor3_medellin_p12.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_medellin_inv1_tn)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor1_medellin_tn.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_medellin_inv2_tn)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor2_medellin_tn.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_medellin_inv1_p6)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor1_medellin_p6.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_medellin_inv2_p6)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor2_medellin_p6.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_medellin_inv3_p6)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor3_medellin_p6.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_giron_inv1)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor1_giron.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_giron_inv2)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor2_giron.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_giron_inv3)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor3_giron.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_giron_inv4)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor4_giron.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_giron_inv5)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor5_giron.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_giron_inv6)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor6_giron.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_monteria_inv1)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor1_monteria.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_monteria_inv2)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor2_monteria.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_cartagena_inv1)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor1_cartagena.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_cartagena_inv2)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor2_cartagena.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_cartagena_inv3)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor3_cartagena.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_cartagena_inv4)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor4_cartagena.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_valledupar_inv1_hangar)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor1_valledupar_hangar.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_valledupar_inv2_hangar)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor2_valledupar_hangar.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_valledupar_inv3_hangar)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor3_valledupar_hangar.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_valledupar_inv4_hangar)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor4_valledupar_hangar.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_valledupar_inv5_hangar)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor5_valledupar_hangar.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_valledupar_inv6_hangar)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor6_valledupar_hangar.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_valledupar_inv1_riego)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor1_valledupar_riego.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_valledupar_inv2_riego)
            tupla_db, = datos
            datos = cursor.fetchall()
            reporte_inversor2_valledupar_riego.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
    with bd.cursor() as cursor:
            cursor.execute(query_semanal_valledupar_inv3_riego)
            datos = cursor.fetchall()
            tupla_db, = datos
            reporte_inversor3_valledupar_riego.append([tupla_db[0],round(tupla_db[1],2),tupla_db[2],tupla_db[3]])
            print('Consulta Finalizada...')

if __name__ == '__main__':
    consultaBD()


#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |// '.
#                 / \\|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | \\\  -  #/ |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~