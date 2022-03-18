from ast import Return
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.message
import random
from ejemplo import consultaBD, reporte_inversor1_neiva, reporte_inversor2_neiva, reporte_inversor3_neiva,reporte_inversor1_mosquera,reporte_inversor2_mosquera,reporte_inversor1_medellin_p12,reporte_inversor2_medellin_p12,reporte_inversor3_medellin_p12,reporte_inversor1_medellin_tn,reporte_inversor2_medellin_tn,reporte_inversor1_medellin_p6,reporte_inversor2_medellin_p6,reporte_inversor3_medellin_p6,reporte_inversor1_giron,reporte_inversor2_giron,reporte_inversor3_giron,reporte_inversor4_giron,reporte_inversor5_giron,reporte_inversor6_giron,reporte_inversor1_monteria,reporte_inversor2_monteria,reporte_inversor1_cartagena,reporte_inversor2_cartagena,reporte_inversor3_cartagena,reporte_inversor4_cartagena,reporte_inversor1_valledupar_hangar,reporte_inversor2_valledupar_hangar,reporte_inversor3_valledupar_hangar,reporte_inversor4_valledupar_hangar,reporte_inversor5_valledupar_hangar,reporte_inversor6_valledupar_hangar,reporte_inversor1_valledupar_riego,reporte_inversor2_valledupar_riego,reporte_inversor3_valledupar_riego

consultaBD()
indicador_conec ="""
                    <a class="btn-floating pulse teal accent-3"
                      ><img
                        style="padding: 7px; height: 25px; width: 25px"
                        src="https://i.postimg.cc/N0QH4PTM/Icon-Wifi-Blanco.png"
                        alt="icono de Conectividad"
                    /></a>
"""
indicador_conec_defic = """
                    <a class="btn-floating pulse  warnig"
                      ><img
                        style="padding: 7px; height: 25px; width: 25px"
                        src="https://i.postimg.cc/N0QH4PTM/Icon-Wifi-Blanco.png"
                        alt="icono de Conectividad"
                    /></a>
"""
indicador_conec_null = """
                    <a class="btn-floating pulse  conect_null"
                      ><img
                        style="padding: 7px; height: 25px; width: 25px"
                        src="https://i.postimg.cc/N0QH4PTM/Icon-Wifi-Blanco.png"
                        alt="icono de Conectividad"
                    /></a>
"""
indicador_desco ="""
                    <a class="btn-floating pulse red darken-2"
                      ><img
                        style="padding: 7px; height: 25px; width: 25px"
                        src="https://i.postimg.cc/N0QH4PTM/Icon-Wifi-Blanco.png"
                        alt="icono de Conectividad"
                    /></a>
"""
conectividad_inv1_neiva = int(reporte_inversor1_neiva[0][1])
conectividad_inv2_neiva = int(reporte_inversor2_neiva[0][1])
conectividad_inv3_neiva = int(reporte_inversor3_neiva[0][1])
conectividad_inv1_mosquera = int(reporte_inversor1_mosquera[0][1])
conectividad_inv2_mosquera = int(reporte_inversor2_mosquera[0][1])
conectividad_inv1_medellin_p12 = int(reporte_inversor1_medellin_p12[0][1])
conectividad_inv2_medellin_p12 = int(reporte_inversor2_medellin_p12[0][1])
conectividad_inv3_medellin_p12 = int(reporte_inversor3_medellin_p12[0][1])
conectividad_inv1_medellin_tn = int(reporte_inversor1_medellin_tn[0][1])
conectividad_inv2_medellin_tn = int(reporte_inversor2_medellin_tn[0][1])
conectividad_inv1_medellin_p6 = int(reporte_inversor1_medellin_p6[0][1])
conectividad_inv2_medellin_p6 = int(reporte_inversor2_medellin_p6[0][1])
conectividad_inv3_medellin_p6 = int(reporte_inversor3_medellin_p6[0][1])
conectividad_inv1_giron = int(reporte_inversor1_giron[0][1])
conectividad_inv2_giron = int(reporte_inversor2_giron[0][1])
conectividad_inv3_giron = int(reporte_inversor3_giron[0][1])
conectividad_inv4_giron = int(reporte_inversor4_giron[0][1])
conectividad_inv5_giron = int(reporte_inversor5_giron[0][1])
conectividad_inv6_giron = int(reporte_inversor6_giron[0][1])
conectividad_inv1_monteria = int(reporte_inversor1_monteria[0][1])
conectividad_inv2_monteria = int(reporte_inversor2_monteria[0][1])
conectividad_inv1_cartagena = int(reporte_inversor1_cartagena[0][1])
conectividad_inv2_cartagena = int(reporte_inversor2_cartagena[0][1])
conectividad_inv3_cartagena = int(reporte_inversor3_cartagena[0][1])
conectividad_inv4_cartagena = int(reporte_inversor4_cartagena[0][1])
conectividad_inv1_valledupar_hangar = int(reporte_inversor1_valledupar_hangar[0][1])
conectividad_inv2_valledupar_hangar = int(reporte_inversor2_valledupar_hangar[0][1])
conectividad_inv3_valledupar_hangar = int(reporte_inversor3_valledupar_hangar[0][1])
conectividad_inv4_valledupar_hangar = int(reporte_inversor4_valledupar_hangar[0][1])
conectividad_inv5_valledupar_hangar = int(reporte_inversor5_valledupar_hangar[0][1])
conectividad_inv6_valledupar_hangar = int(reporte_inversor6_valledupar_hangar[0][1])
conectividad_inv1_valledupar_riego = int(reporte_inversor1_valledupar_riego[0][1])
conectividad_inv2_valledupar_riego = int(reporte_inversor2_valledupar_riego[0][1])
conectividad_inv3_valledupar_riego = int(reporte_inversor3_valledupar_riego[0][1])

def validador(params): 
  if ( params > 70 ):
   return indicador_conec
  elif (params > 40 ):
    return indicador_conec_defic
  elif (params > 10 ):
    return indicador_conec_null
  else:
   return indicador_desco

cuerpoHtml = """
   <!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8" />  
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
   
    <style type="text/css">
    .btn-large {
    height: 54px;
    line-height: 54px;
    font-size: 15px;
    padding: 0 28px;
}
.warnig {
        background-color: #e6e953 !important;
}
.conect_null {
        background-color: #f07706 !important;
}
.red {
    background-color: #F44336 !important;
}
.red.darken-2 {
    background-color: #D32F2F !important;
}
    .waves-effect {
    position: relative;
    cursor: pointer;
    display: inline-block;
    overflow: hidden;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
    vertical-align: middle;
    z-index: 1;
    -webkit-transition: .3s ease-out;
    transition: .3s ease-out;
}

    .material-icons {
    font-family: 'Material Icons';
    font-weight: normal;
    font-style: normal;
    font-size: 24px;
    line-height: 1;
    letter-spacing: normal;
    text-transform: none;
    display: inline-block;
    white-space: nowrap;
    word-wrap: normal;
    direction: ltr;
    -webkit-font-smoothing: antialiased;
}
.container {
  margin: 0 auto;
  max-width: 1080px;
  width: 60%;
    text-decoration: none;
    }
      @media only screen and (min-width: 401px) {
      .container {
          width: 90%;   
      }
      body{
        font-size: 12px;
      }
       .imagen_logo_sena {
        margin:0;
      }
    }

    @media only screen and (min-width: 601px) {
      .container {
          width: 75%;   
      }
      body{
        font-size: 15px;
      }
      .imagen_logo_sena {
        margin:0;
      }
    }

    @media only screen and (min-width: 993px) {
      .container {
        width: 70%;
        }
        body{
          font-size: 20px;
        }
    }

    *, *:before, *:after {
  -webkit-box-sizing: inherit;
  box-sizing: inherit;
}
.hoverable {
  -webkit-transition: -webkit-box-shadow .25s;
  transition: -webkit-box-shadow .25s;
  transition: box-shadow .25s;
  transition: box-shadow .25s, -webkit-box-shadow .25s;
}
.orange {
  background-color: #ff9800 !important;
}
.orange.darken-3 {
  background-color: #ef6c00 !important;
}
.collapsible-header {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    cursor: pointer;
    -webkit-tap-highlight-color: transparent;
    line-height: 1.5;
    padding: 1rem;
    background-color: #fff;
    border-bottom: 1px solid #ddd;
    justify-content: center;
}
table {
  width: 100%;
  display: table;
  border-collapse: collapse;
  border-spacing: 0;
}
table, th, td {
  border: none;
}
td, th {
    padding: 15px 5px;
    display: table-cell;
    text-align: left;
    vertical-align: middle;
    border-radius: 2px;
}
tr {
    border-bottom: 1px solid rgba(0,0,0,0.12);
}
.teal.accent-3 {
    background-color: #1de9b6 !important;
}
.teal {
    background-color: #009688 !important;
}
.btn-floating {
    display: inline-block;
    color: #fff;
    position: relative;
    overflow: hidden;
    z-index: 1;
    width: 40px;
    height: 40px;
    line-height: 40px;
    padding: 0;
    background-color: #26a69a;
    border-radius: 50%;
    -webkit-transition: background-color .3s;
    transition: background-color .3s;
    cursor: pointer;
    vertical-align: middle;
}
.btn-floating:before {
    border-radius: 0;
}
.pulse {
    overflow: visible;
    position: relative;
}
.pulse::before {
    content: '';
    display: block;
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background-color: inherit;
    border-radius: inherit;
    -webkit-transition: opacity .3s, -webkit-transform .3s;
    transition: opacity .3s, -webkit-transform .3s;
    transition: opacity .3s, transform .3s;
    transition: opacity .3s, transform .3s, -webkit-transform .3s;
    animation: palpitar 1s linear infinite alternate;
    will-change: transform;
    z-index: -1;
}
li {
    display: list-item;
    text-align: -webkit-match-parent;
    
}

.collapsible {
    border-top: 1px solid #ddd;
    border-right: 1px solid #ddd;
    border-left: 1px solid #ddd;
    margin: .5rem 0 1rem 0;
}
ul {
    display: block;
    list-style-type: disc;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
   padding: 0;
}

            img {
            height: 200px;
            width: 100%;
            }
            body {
           font-family: 'Brush Script MT', cursive;
            background: rgb(211, 211, 235);
            }
            .sede_sena {
            margin-left: 125px;
            }
            .sena_sistema_monitoreo {
            margin-top: 10px;
            padding: 0 20px 0 20px;
            }
            .distitor {
            background-color: blanchedalmond;
            }
            .imagen_logo_sena {
            margin: 0 50px 0 70px ;
            border-radius: 50%;
            height: 90px;
            width: 90px;
            }
            .contenedor_logo {
            position: absolute;
            top: 0;
            left: 40.6rem;
            }

                 @keyframes palpitar {
              0%{
                transform: rotate(45deg) scale(1);
              }
              50%{
                transform: rotate(45deg) scale(1.5);
              }
              100%{
                transform: rotate(45deg) scale(1);
              }
            }
        </style>
     
   
  </head>     
      
  <body>
  
    <div class="contenedor_logo">
    
    </div>
    <div class="container " >
     <div class=" hoverable orange darken-3">
       
      <img src="https://erenovable.com/wp-content/uploads/2012/09/Fotovoltaica.jpg" alt="Publicidad de nuestro producto">
     </div>

     <ul class="collapsible" style="background-color: rgb(250, 251, 252);">

      <span>
        <div class="collapsible-header distitor" >
          <div class="contenedor_logo">
            <img class="imagen_logo_sena" src="https://i.postimg.cc/15D01WtM/logo-Sena-1.png" alt="">
          </div >
            <h1 style="font-weight: bolder;" >Reporte Sistema de Monitoreo 10 Mar 2022 </h1>
          </div>
      </span>
      <span>
        <div class="collapsible-header" >
          <div class="sede_sena">
            <h2>Medellin</h2>
          </div>
        </div>
        <div class="container">
        <table>
          <thead>
            <tr>
                <th>Conect</th>         
                <th>Inversor</th>
                <th>Sede Complejo Central piso 12</th>   
                
                <th>Porcentaje</th>  
                <th>Energia Generada kWh</th>
                <th>Energia Consumida kWh</th> 
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>"""+validador(conectividad_inv1_medellin_p12)+""" </td>
              <td>inversor #1</td>
                 <td></td>
             
              <td>% """+str(reporte_inversor1_medellin_p12[0][1])+"""</td>
               <td>"""+str(reporte_inversor1_medellin_p12[0][2])+"""</td>
                <td>"""+str(reporte_inversor1_medellin_p12[0][3])+"""</td>
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv2_medellin_p12))+""" </td>
              <td>inversor #2 </td>
                      <td></td>
             
              <td>% """+str(reporte_inversor2_medellin_p12[0][1])+"""</td>
               <td>"""+str(reporte_inversor2_medellin_p12[0][2])+"""</td>
                <td>"""+str(reporte_inversor2_medellin_p12[0][3])+"""</td>

            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv3_medellin_p12))+""" </td>
              <td>inversor #3 </td>
                      <td></td>
             
              <td>% """+str(reporte_inversor3_medellin_p12[0][1])+"""</td>
               <td>"""+str(reporte_inversor3_medellin_p12[0][2])+"""</td>
                <td>"""+str(reporte_inversor3_medellin_p12[0][3])+"""</td>
             
            </tr> 
          </tbody>
          <thead>
            <tr>
                <th></th>         
                <th>Inversores</th>
                <th>Sede Complejo Central piso 6</th> 
               
                <th>Porcentaje</th>  
                <th>Energia Generada kWh</th>
                <th>Energia Consumida kWh</th>      
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>"""+str(validador(conectividad_inv1_medellin_p6))+"""</td>
              <td> inversor #1 </td>
                   <td></td>
             
              <td>% """+str(reporte_inversor1_medellin_p6[0][1])+"""</td>
               <td>"""+str(reporte_inversor1_medellin_p6[0][2])+"""</td>
                <td>"""+str(reporte_inversor1_medellin_p6[0][3])+"""</td>
         
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv2_medellin_p6))+"""</td>
              <td> inversor #2 </td>
                     <td></td>
             
              <td>% """+str(reporte_inversor2_medellin_p6[0][1])+"""</td>
               <td>"""+str(reporte_inversor2_medellin_p6[0][2])+"""</td>
                <td>"""+str(reporte_inversor2_medellin_p6[0][3])+"""</td>

            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv3_medellin_p6))+"""</td>
              <td> inversor #3 </td>
                     <td></td>
             
              <td>% """+str(reporte_inversor3_medellin_p6[0][1])+"""</td>
               <td>"""+str(reporte_inversor3_medellin_p6[0][2])+"""</td>
                <td>"""+str(reporte_inversor3_medellin_p6[0][3])+"""</td>
             
            </tr>
     
          </tbody>
          <thead>
            <tr>
                <th> </th>         
                <th>Inversor</th>
                <th>Sede Complejo Central Torre Norte</th>  
                
                <th>Porcentaje</th>  
                <th>Energia Generada kWh</th>
                <th>Energia Consumida kWh</th>     
            </tr>
          </thead>
          <tbody>
      
            <tr>
              <td>"""+str(validador(conectividad_inv1_medellin_tn))+"""</td>
              <td> inversor #1 </td>
                         <td></td>
             
              <td>% """+str(reporte_inversor1_medellin_tn[0][1])+"""</td>
               <td>"""+str(reporte_inversor1_medellin_tn[0][2])+"""</td>
                <td>"""+str(reporte_inversor1_medellin_tn[0][3])+"""</td>

            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv2_medellin_tn))+"""</td>
              <td> inversor #2 </td>
                           <td></td>
             
              <td>% """+str(reporte_inversor2_medellin_tn[0][1])+"""</td>
               <td>"""+str(reporte_inversor2_medellin_tn[0][2])+"""</td>
                <td>"""+str(reporte_inversor2_medellin_tn[0][3])+"""</td>
             
            </tr>
          </tbody>
        </table>
      </div>
      </span>
      <span>
        <div class="collapsible-header"  >
          <div class="sede_sena">
            <h2>Valledupar</h2>
          </div>
        </div>
        <div class="container">
        <table>
          <thead>
            <tr>
                <th>Conectividad</th>
                <th>Inversores</th>
                <th>Sede: Centro Biotecnologico del Caribe Hangar</th>
                
                <th>Porcentaje</th>  
                <th>Energia Generada kWh</th>
                <th>Energia Consumida kWh</th>       
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>"""+str(validador(conectividad_inv1_valledupar_hangar))+"""</td>
              <td> inversor #1 </td>
              <td></td>
             
              <td>% """+str(reporte_inversor1_valledupar_hangar[0][1])+"""</td>
               <td>"""+str(reporte_inversor1_valledupar_hangar[0][2])+"""</td>
                <td>"""+str(reporte_inversor1_valledupar_hangar[0][3])+"""</td>
         
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv2_valledupar_hangar))+"""</td>
              <td> inversor #2 </td>
              <td></td>
             
              <td>% """+str(reporte_inversor2_valledupar_hangar[0][1])+"""</td>
               <td>"""+str(reporte_inversor2_valledupar_hangar[0][2])+"""</td>
                <td>"""+str(reporte_inversor2_valledupar_hangar[0][3])+"""</td>

            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv3_valledupar_hangar))+"""</td>
              <td> inversor #3 </td>
              <td></td>
             
              <td>% """+str(reporte_inversor3_valledupar_hangar[0][1])+"""</td>
               <td>"""+str(reporte_inversor3_valledupar_hangar[0][2])+"""</td>
                <td>"""+str(reporte_inversor3_valledupar_hangar[0][3])+"""</td>
             
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv4_valledupar_hangar))+"""</td>
              <td> inversor #4 </td>
              <td></td>
             
              <td>% """+str(reporte_inversor4_valledupar_hangar[0][1])+"""</td>
               <td>"""+str(reporte_inversor4_valledupar_hangar[0][2])+"""</td>
                <td>"""+str(reporte_inversor4_valledupar_hangar[0][3])+"""</td>
         
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv5_valledupar_hangar))+"""</td>
              <td> inversor #5 </td>
              <td></td>
             
              <td>% """+str(reporte_inversor5_valledupar_hangar[0][1])+"""</td>
               <td>"""+str(reporte_inversor5_valledupar_hangar[0][2])+"""</td>
                <td>"""+str(reporte_inversor5_valledupar_hangar[0][3])+"""</td>

            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv6_valledupar_hangar))+"""</td>
              <td> inversor #6 </td>
              <td></td>
             
              <td>% """+str(reporte_inversor2_medellin_tn[0][1])+"""</td>
               <td>"""+str(reporte_inversor2_medellin_tn[0][2])+"""</td>
                <td>"""+str(reporte_inversor2_medellin_tn[0][3])+"""</td>
             
            </tr>
          </tbody>
          <thead>
            <tr>
                <th></th>
                <th>Inversores</th>
                <th>Sede:Centro Biotecnologico del Caribe Riego</th>   
              
                <th>Porcentaje</th>  
                <th>Energia Generada kWh</th>
                <th>Energia Consumida kWh</th>    
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>"""+str(validador(conectividad_inv1_valledupar_riego))+"""</td>
              <td> inversor #1 </td>
             <td></td>
             
              <td>% """+str(reporte_inversor1_valledupar_riego[0][1])+"""</td>
               <td>"""+str(reporte_inversor1_valledupar_riego[0][2])+"""</td>
                <td>"""+str(reporte_inversor1_valledupar_riego[0][3])+"""</td>
         
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv2_valledupar_riego))+"""</td>
              <td> inversor #2 </td>
             <td></td>
             
              <td>% """+str(reporte_inversor2_valledupar_riego[0][1])+"""</td>
               <td>"""+str(reporte_inversor2_valledupar_riego[0][2])+"""</td>
                <td>"""+str(reporte_inversor2_valledupar_riego[0][3])+"""</td>

            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv3_valledupar_riego))+"""</td>
              <td> inversor #3 </td>
              <td></td>
             
              <td>% """+str(reporte_inversor3_valledupar_riego[0][1])+"""</td>
               <td>"""+str(reporte_inversor3_valledupar_riego[0][2])+"""</td>
                <td>"""+str(reporte_inversor3_valledupar_riego[0][3])+"""</td>
             
            </tr>
          </tbody>
        </table>
      </div>
      </span>
      <span>
        <div class="collapsible-header" >
          <div class="sede_sena">
            <h2>Mosquera</h2>
          </div>
        </div>
        <div class="container">
        <table>
          <thead>
            <tr>
                <th>Conectividad</th>
                <th>Inversores</th>
                <th>Centro de Biotecnologia Agropecuaria</th>
                <th>Conteo2m</th>
                <th>Porcentaje</th>  
                <th>Energia Generada kWh</th>
                <th>Energia Consumida kWh</th>     
            </tr>
          </thead>
         
"""

cuerpoHtml2 = """
        <tbody>
            <tr>
              <td>"""+str(validador(conectividad_inv1_mosquera))+"""</td>
                         <td> inversor #1 </td>
                <td></td>
             
              <td>% """+str(reporte_inversor1_mosquera[0][1])+"""</td>
               <td>"""+str(reporte_inversor1_mosquera[0][2])+"""</td>
                <td>"""+str(reporte_inversor1_mosquera[0][3])+"""</td>
         
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv2_mosquera))+"""</td>
              <td> inversor #2 </td>
                <td></td>
             
              <td>% """+str(reporte_inversor2_mosquera[0][1])+"""</td>
               <td>"""+str(reporte_inversor2_mosquera[0][2])+"""</td>
                <td>"""+str(reporte_inversor2_mosquera[0][3])+"""</td>
            </tr>
          </tbody>
        </table>
      </div>
      </span>
      <span>
        <div class="collapsible-header" >
          <div class="sede_sena">
            <h2>Cartagena</h2>
          </div>
        </div>
        <div class="container">
        <table>
          <thead>
            <tr>
                <th>Conectividad</th>
                <th>Inversores</th>
                <th>Sede: Centro para la Industria Petroquimica</th>
                
                <th>Porcentaje</th>  
                <th>Energia Generada kWh</th>
                <th>Energia Consumida kWh</th>       
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>"""+str(validador(conectividad_inv1_cartagena))+"""</td>
              <td>inversor #1 </td>
                    <td></td>
             
              <td>% """+str(reporte_inversor1_cartagena[0][1])+"""</td>
               <td>"""+str(reporte_inversor1_cartagena[0][2])+"""</td>
                <td>"""+str(reporte_inversor1_cartagena[0][3])+"""</td>
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv2_cartagena))+"""</td>
              <td>inversor #2 </td>
                    <td></td>
             
              <td>% """+str(reporte_inversor2_cartagena[0][1])+"""</td>
               <td>"""+str(reporte_inversor2_cartagena[0][2])+"""</td>
                <td>"""+str(reporte_inversor2_cartagena[0][3])+"""</td>
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv3_cartagena))+"""</td>
              <td>inversor #3 </td>
                    <td></td>
             
              <td>% """+str(reporte_inversor3_cartagena[0][1])+"""</td>
               <td>"""+str(reporte_inversor3_cartagena[0][2])+"""</td>
                <td>"""+str(reporte_inversor3_cartagena[0][3])+"""</td>  
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv4_cartagena))+"""</td>
              <td>inversor #4 </td>
                   <td></td>
             
              <td>% """+str(reporte_inversor4_cartagena[0][1])+"""</td>
               <td>"""+str(reporte_inversor4_cartagena[0][2])+"""</td>
                <td>"""+str(reporte_inversor4_cartagena[0][3])+"""</td>   
            </tr>
          </tbody>
        </table>
      </div>
      </span>
      <span>
        <div class="collapsible-header" >
          <div class="sede_sena">
            <h2>Monteria</h2>
          </div>
        </div>
        <div class="container">
        <table>
          <thead>
            <tr>
                <th>Conectividad</th>
                <th>Inversores</th>
                <th>Sede: Centro De Comercio, Industria y Turismo</th>
                
                <th>Porcentaje</th>  
                <th>Energia Generada kWh</th>
                <th>Energia Consumida kWh</th>        
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>"""+str(validador(conectividad_inv1_monteria))+"""</td>
              <td>inversor #1 </td>
                   <td></td>
             
              <td>% """+str(reporte_inversor1_monteria[0][1])+"""</td>
               <td>"""+str(reporte_inversor1_monteria[0][2])+"""</td>
                <td>"""+str(reporte_inversor1_monteria[0][3])+"""</td>
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv2_monteria))+"""</td>
              <td>inversor #2 </td>
                   <td></td>
             
              <td>% """+str(reporte_inversor2_monteria[0][1])+"""</td>
               <td>"""+str(reporte_inversor2_monteria[0][2])+"""</td>
                <td>"""+str(reporte_inversor2_monteria[0][3])+"""</td>  
            </tr>
          </tbody>
        </table>
      </div>
      </span>
      <span>
        <div class="collapsible-header" >
          <div class="sede_sena">
            <h2>Giron</h2>
          </div>
        </div>
        <div class="container">
        <table>
          <thead>
            <tr>
                <th>Conectividad</th>
                <th>Inversores</th>
                <th>Sede: Centro Industrial de Mantenimiento Integral</th>
                
                <th>Porcentaje</th>  
                <th>Energia Generada kWh</th>
                <th>Energia Consumida kWh</th>       
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>"""+str(validador(conectividad_inv1_giron))+"""</td>
              <td>inversor #1 </td>
              <td></td>
             
              <td>% """+str(reporte_inversor1_giron[0][1])+"""</td>
               <td>"""+str(reporte_inversor1_giron[0][2])+"""</td>
                <td>"""+str(reporte_inversor1_giron[0][3])+"""</td>       
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv2_giron))+"""</td>
              <td>inversor #2 </td>
             <td></td>
             
              <td>% """+str(reporte_inversor2_giron[0][1])+"""</td>
               <td>"""+str(reporte_inversor2_giron[0][2])+"""</td>
                <td>"""+str(reporte_inversor2_giron[0][3])+"""</td>
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv3_giron))+"""</td>
              <td>inversor #3 </td>
              <td></td>
             
              <td>% """+str(reporte_inversor3_giron[0][1])+"""</td>
               <td>"""+str(reporte_inversor3_giron[0][2])+"""</td>
                <td>"""+str(reporte_inversor3_giron[0][3])+"""</td>         
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv4_giron))+"""</td>
              <td>inversor #4 </td>
              <td></td>
             
              <td>% """+str(reporte_inversor4_giron[0][1])+"""</td>
               <td>"""+str(reporte_inversor4_giron[0][2])+"""</td>
                <td>"""+str(reporte_inversor4_giron[0][3])+"""</td>      
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv5_giron))+"""</td>
              <td>inversor #5 </td>
              <td></td>
             
              <td>% """+str(reporte_inversor5_giron[0][1])+"""</td>
               <td>"""+str(reporte_inversor5_giron[0][2])+"""</td>
                <td>"""+str(reporte_inversor5_giron[0][3])+"""</td>
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv6_giron))+"""</td>
              <td>inversor #6 </td>
              <td></td>
             
              <td>% """+str(reporte_inversor6_giron[0][1])+"""</td>
               <td>"""+str(reporte_inversor6_giron[0][2])+"""</td>
                <td>"""+str(reporte_inversor6_giron[0][3])+"""</td>
            </tr>
          </tbody>
        </table>
      </div>
      </span>
      <span>
        <div class="collapsible-header" >
          <div class="sede_sena">
            <h2>Neiva</h2>
          </div>
        </div>
        <div class="container">

   <table>
          <thead>
            <tr>
                <th>Conectividad</th>
                <th>Inversores</th>
                <th>Sede: Centro de la Industria, la Empresa y los Servicios</th> 
                
                <th>Porcentaje</th>  
                <th>Energia Generada kWh</th>
                <th>Energia Consumida kWh</th>  
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>"""+str(validador(conectividad_inv1_neiva))+"""</td>
              <td>inversor #1 </td>   
                           <td></td>
             
              <td>% """+str(reporte_inversor1_neiva[0][1])+"""</td>
               <td>"""+str(reporte_inversor1_neiva[0][2])+"""</td>
                <td>"""+str(reporte_inversor1_neiva[0][3])+"""</td>
             
            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv2_neiva))+"""</td>
              <td>inversor #2</td>
                         <td></td>
             
              <td>% """+str(reporte_inversor2_neiva[0][1])+"""</td>
               <td>"""+str(reporte_inversor2_neiva[0][2])+"""</td>
                <td>"""+str(reporte_inversor2_neiva[0][3])+"""</td>

            </tr>
            <tr>
              <td>"""+str(validador(conectividad_inv3_neiva))+"""</td>
              <td>inversor #3 </td>
                          <td></td>
             
              <td>% """+str(reporte_inversor3_neiva[0][1])+"""</td>
               <td>"""+str(reporte_inversor3_neiva[0][2])+"""</td>
                <td>"""+str(reporte_inversor3_neiva[0][3])+"""</td>
            </tr>
          </tbody>
        </table>
      </div>
      </span>
          <span>
            <div class="container">
              <a class="waves-effect orange darken-3 btn-large" style="border-radius: 5px; margin:25px 0; width: 90%; color: white; text-align: center;">Ver detalle</a>
            </div>
          </span>
    </ul>
    </div>
  </body>
</html>"""

def emailCheck(_email, subject, messages):
    #msg = MIMEMultipart()
    msg = email.message.Message()
    #message = messages
 
# setup the parameters of the message
    msg['From'] = "esteban.gomez@suncoenergy.com.co"
    msg['To'] = _email
    msg['Subject'] = subject
 
# add in the message body
    msg.add_header('Content-Type' , 'text/html')
    msg.set_payload(cuerpoHtml+cuerpoHtml2)
    # msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg['From'], 'Alchimist1997')
    server.sendmail(msg['From'],  msg['To'], msg.as_string() )
    server.quit()


if __name__ == '__main__':
    emailCheck()