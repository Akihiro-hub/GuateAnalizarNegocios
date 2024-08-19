import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# セッション状態を初期化
if 'page' not in st.session_state:
    st.session_state['page'] = 'checklist'

# ページのナビゲーションを制御
def switch_to_analysis():
    st.session_state['page'] = 'analysis'

import time
def main():
    while True:
        time.sleep(360 * 360)  # Sleep for 6 hours

rubro = st.sidebar.selectbox("Rubro de negocio (o tema) a analizar", ["Seleccione", "Carpintería", "Panadería", "Restaurante(Comedor)", "Negocio de impresión", "Construcción", "Corte y confección", "Mercadito(Pulpería)", "Reparación del auto", "Capital de trabajo", "Capital de inversiones", "Análisis de estados financieros"])

if rubro == "Seleccione":
    st.write("## Análisis de negocios (PyMEs) y sus solicitudes del crédito, mediante la entrevista y la visita por el colaborador de la cooperativa")
    col1, col2 = st.columns(2)
    with col1: 
        st.write("### :blue[(Modelo GuateCrece)]")
        st.write("###### Cuando una cooperativa recibe consultas sobre el crédito por un negocio asociado, será importante analizar, mediante la entrevista y la visita, :blue[(i) demandas del capital de trabajo o para la inversión y (ii) la situación de la operación de la empresa solicitante,] considerando las caracterísiticas de la operación que cada uno de los rubros del negocio tiene.") 
        st.write("###### (NOTA: Los detalles de puntos a analizar en cada uno de rubros del negocio como carpintería, panadería, etc. y temas transversales como el analísis de estados financieros se presentarán, dependiendo de su selección en las opciones presentadas a la izquierda.)")
    with col2:
        st.image("Logo.png", width = 280)

elif rubro == "Capital de trabajo":
    st.write("#### :green[¿Qué tenemos que analizar la solicitud del crédito para el capital de trabajo?]") 
    st.write("###### Cuando una cooperativa recibe la solicitud del crédito, primero, tendrá que analizar el objetivo del uso del crédito. Abajo se presentan los puntos a analizar la solicitud para el capital de trabajo.") 
    st.write("###### El capital de trabajo se necesita para mantener la operación diaria del negocio. Algunas veces, la cantidad necesaria del capital de trabajo se puede aumentar, por (i) la expansión del negocio, (ii) el inventario sobrante, (iii) los costos operativos elevados, (iv) el motivo temporal, etc.") 


    st.write("#### :red[Lista de chequeo]", divider="red") 
    st.write("###### :red[Con relación a la solicitud del crédito para el capital de trabajo, deberá averiguar los siguientes.]")
    OP1 = st.checkbox("¿El negocio no tiene el inventario sobrante? ¿No tiene saldos de productos que estén fuera de temporada o de moda, que sean difíciles de vender? (Si hay un aumento alto en la cantidad de inventario de productos, ¿tiene una causa razonable?)")
    OP2 = st.checkbox("¿Considera que las ventas y compras de los productos están y estrían estables hoy y en el futuro? (En caso no afirmativo, ¿la empresa aplica ciertas medidas para mejorar?)")
    OP3 = st.checkbox("¿El valor de las cuentas por cobrar no es alto en este tiempo? ¿Esta situación responde porque no ha habido un aumento drástico en operaciones recientes?")
    OP4 = st.checkbox("¿El aumento de la necesidad del capital de trabajo se genera por la ineficiencia operativa, tales como la reducción drástica de la venta, aumento considerable del costos operativos, etc.? (En caso afirmativo, ¿la empresa aplica ciertas medidas para solucionarla?)")

    if st.button("Ya la lista de chequeo se ha llenada y vamos a analizar"):
        switch_to_analysis()  # 分析ページに切り替える

if st.session_state['page'] == 'analysis':
    st.write("## :blue[Sugerencias]")
    selected_count = sum([OP1, OP2, OP3, OP4])
    # Mensaje principal basado en la cantidad de selecciones
    if selected_count == 4:
        st.write("Probablemente se ha observado bien.")
        st.balloons()
    else:
        st.write("La demanda del capital de trabajo se aumentará por (i) la ineficiencia operativa, y (ii) condiciones inapropiadas de compras y ventas. Si la ineficiencia operativa genera la demanda adicional del capital, es importante asesorar el negocio con miras a su mejora.")

    # Mensaje final obligatorio
    st.write("La siguiente calculadora puede identificar el monto total necesario del capital de ytabajo normal de la empresa. El monto solicitado del crédito no debe superar el monto calculado.")

    st.write("#### :blue[Herramienta para el análisis]", divider="blue") 
    st.write("###### :blue[Calculadora del monto total necesario del capital de trabajo normal del negocio]")  
    e = st.number_input("Valor del inventario (GTQ)", 1, 10000000000000, 8000)
    f = st.number_input("Cuentas por pagar (GTQ)", 1, 10000000000000, 2000)
    g = st.number_input("Cuentas por cobrar (GTQ)", 1, 1000000000000, 4000)
    h = e + g - f

    st.write("##### Resultado del cálculo: Monto total necesario del capital de trabajo normal (GTQ):")
    st.text(h)

elif rubro == "Capital de inversiones":
    st.write("#### :green[¿Qué tenemos que analizar la solicitud del crédito para el capital de inversión?]") 
    st.write("###### Cuando una cooperativa recibe la solicitud del crédito, primero, tendrá que analizar el objetivo del uso del crédito. Abajo se presentan los puntos a analizar la solicitud para el capital de inversión.") 
    st.write("###### La inversión se hace para (i) montar o expandir el negocio, (ii) desarrollar nuevos productos y/o (iii) sustituir equipos ya viejos. Cabe decir que la inversión aumentará las necesidades del capital de trabajo.") 

    st.write("#### :red[Lista de chequeo]", divider="red") 
    st.write("###### :red[Con relación a la solicitud del crédito para el capital de inversión, deberá averiguar los siguientes.]")
    OP1 = st.checkbox("¿El motivo de inversión es razonable? (Posibles motivos pueden incluir; compra del equipo nuevo para aumentar la producción, sustitución de equipos ya viejos, y/o desarrollo de nuevos mercados y negocios.)")
    OP2 = st.checkbox("¿La empresa podrá esperar un aumento de la venta por la inversión de nueva maquinaria, recibiendo las ordenes de los clientes?")
    OP3 = st.checkbox("¿La inversión no causará la falta del capital de trabajo, mediante el aumento de costos operativos, incluyendo la compra aumentada de materias primas, costos financieros elevados, etc.?")
    OP4 = st.checkbox("¿El monto de ganancia (más depreciación) supera el importe de reembolso del crédito?")
    OP5 = st.checkbox("¿El negocio tiene suficiente espacio para instalar el equipo a comprar?")

    if st.button("Ya la lista de chequeo se ha llenada y vamos a analizar"):
        switch_to_analysis()  # 分析ページに切り替える

if st.session_state['page'] == 'analysis':

        st.write("## :blue[Sugerencias]")
        selected_count = sum([OP1, OP2, OP3, OP4, OP5])
        # Mensaje principal basado en la cantidad de selecciones
        if selected_count == 5:
            st.write("Probablemente se ha observado bien.")
            st.balloons()
        else:
            st.write("La inversión puede generar no sólo el aumento de la producción sino tambien el aumento de costos operativos, posiblemente cansando la falta de liquidez del negocio. Por lo cual, es importante analizar si la inversión será oportuna o no, considerando la situación de mercado, o sea, la demanda de cliente, y la competencia con sus competidores.")

    # Mensaje final obligatorio
    st.write("Es importante analizar si el proyecto de la inversión es apropiada o no, aplicando la siguiente calculadora.")

    st.write("#### :blue[Herramienta para el análisis]", divider="blue") 
    st.write("###### :blue[Calculadora del valor presente neto del proyecto]")  
    a = st.number_input("¿Cuánto se debe invertir al inicio del proyecto (GTQ)?", 0, 10000000000000, 50000)
    b = st.number_input("¿Cuál es tasa de costo del capital del negocio (%)?", 0, 100, 12)
    c = st.number_input("¿Cuánto podrá ganar al año por el proyecto de inversión? (De manera más precisa tiene que decirse como el flujo anual de caja, que es casi igual a ganancias menos depreciación: GTQ)", 1, 1000000000000, 20000)
    d = st.number_input("Duración del proyecto (años)", 1, 100, 4)


    lst = [c for i in range(d)]
    lst0 = [-1 * a]
    lst = lst0 + lst
    npv = sum(lst / (1 + b/100) ** t for t, lst in enumerate(lst)) 
    rate = b/100
        
    st.write("#### Valor Presente Neto (VPN) de la inversión (GTQ):")
    st.text(f"VPN: {round(npv)}")
    st.write("###### :blue[La inversion con VPN negativo o insuficiente deberá rechazarse.]")

elif rubro == "Carpintería":
    st.title("¿Cómo analizar la operación de Carpintería?")
    col1, col2 = st.columns(2)

    with col1:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### El costo de materia prima, sobre todo, maderas aserradas, representa la proporción alta en todos los costos de producción. La demanda del capital de trabajo se puede reducir, mediante (i) el aumento del rendimiento de las materias primas, y/o (ii) la reducción del tiempo entre la compra de materia prima y la venta de productos a los clientes.")
        st.write("###### La cooperativa deberá analizar (i) si el monto solicitado para el crédito será apropiado considerando el volumen del inventario, (ii) si el negocio utiliza eficientemente las materias primas, etc.")
    
        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión para el equipo es necesario, al inicio del negocio o al momento de expansión del mismo. El valor económico de la inversión necesaria se varía mucho, dependinedo del equipo a invertir.")
        st.write("###### La cooperativa deberá analizar (i) si el negocio tiene suficiente espacio para instalar el equipo a comprar, (ii) si el negocio podrá aguantar la elevación del monto necesario del capital de trabajo a generar por la inversión, (iii) otras alternativas que podrán aumentar la producitividad sin inversión, etc.")

    with col2:
        st.write("### :green[Lista de chequeo]")
        st.write("##### :green[Marque todos los puntos que la empresa ha logrado.]")
        OP1 = st.checkbox("En el negocio de carpinteria, el uso eficiente de maderas aserradas es uno de los temas prioritarios para aumentar las ganancias, ya que la mayoría de los costos operativos son de materias primas. ¿No tiene muchos desperdicios a desechar? ¿Buen rendimiento de materias primas (maderas)?")
        OP2 = st.checkbox("¿Materias primas y productos finales se guardan de manera ordenada?")
        OP3 = st.checkbox("¿El negocio tiene el proveedor que suministra la madera aserrada de manera estable, con buenas condiciones de compras?")
        OP4 = st.checkbox("¿El negocio tiene ciertos clientes habituales quienes pagan con buenas condiciones, o aplica algunas medidas para estabilizar sus ventas?")
        OP5 = st.checkbox("¿El negocio intenta reducir el tiempo desde la compra de materias primas hasta la entrega (venta) de los productos a los clientes, para mejorar su flujo de caja?")

    if st.button("Ya la lista de chequeo se ha llenada y vamos a analizar"):
        switch_to_analysis()  # 分析ページに切り替える

if st.session_state['page'] == 'analysis':

        st.write("## :blue[Sugerencias]")
        
        selected_count = sum([OP1, OP2, OP3, OP4, OP5])

        # Mensaje principal basado en la cantidad de selecciones
        if selected_count == 5:
            st.write("Probablemente el negocio operaría apropiadamente.")
            st.balloons()
        elif selected_count in [3, 4]:
            st.write("El negocio tendrá que mejorar sus operaciones en ciertos puntos.")
        else:
            st.write("El negocio tiene que fortalecerse.")
        
        # Mensajes adicionales para checkboxes no seleccionados
        if not OP1:
            st.write("El rendimiento de materias primas se podrá mejorar, mediante el diseño apropiado de los productos, el desarrollo de nuevos productos de segunda línea utilizando pedazos de la madera, el aumento de las órdenes con el volumen suficiente, el procesamiento de las maderas aserradas después de la recepción de las ordenes, etc.")
        if not OP2:
            st.write("El taller desordenado podrá causar la ineficiencia operativa, aumentando la demanda del capital de trabajo.")
        if not OP3:
            st.write("El suministro estable de la materia prima es esencial, ya que la mayoría de los costos operativos del negocio de la carpintería son de la materia prima.")
        if not OP4:
            st.write("El aumento de clientes habituales podrá causar la venta estable y la mejora de la eficiencia operativa.")
        if not OP5:
            st.write("El tiempo largo entre la compra de materias primas hasta la entrega de los productos a los clientes, aumentará la demanda del capital de trabajo.")
        
        # Mensaje final obligatorio
        st.write("Si la empresa se dedica principalmente a la producción prospectiva para el inventario y vende alta variedad de productos, será esencial aumentar (1) la proporción de producción basada de las órdenes de los clientes y (2) los productos con diseños semejantes, reduciendo el coste de las materias primas y aumentando los beneficios, con ventas estables. Es importante que la empresa mantenga el inventario de maderas aserradas de seguridad con el volumen apropiado. Si el negocio tiene el inventario en exceso, tendrá dificultades en su liquidez financiero, además de aumento del riesgo de corrosión de la madera. Por el contrario, si las existencias de materias primas son bajas demasiado, existe el riesgo de perder oportunidades por no poder atender los pedidos de los clientes.")
        st.write("La siguiente calculadora puede identificar el volumen del inventario de seguridad, que determina a la vez la cantidad necesaria del capital de trabajo.")
            
    st.header(" :red[Calculador del inventario de seguridad]", divider="red") 
    st.write("###### :red[Es importante calcular el volumen del inventario de seguridad, que se refiere a la cantidad necesaria a mantener siempre para evitar escasez, en ciertas materias importnates, como maderas aserradas en la carpintería.]")  

    a = st.number_input("¿Hace 5 días (o semana) cuántas piezas de madera aserrada se consumieron?", 0, 10000, 30)
    b = st.number_input("¿Hace 4 días (o semana) cuántas piezas de madera aserrada se consumieron?", 0, 10000, 25)
    c = st.number_input("¿Hace 3 días (o semana) cuántas piezas de madera aserrada se consumieron?", 0, 10000, 45)
    d = st.number_input("¿Hace 2 días (o semana) cuántas piezas de madera aserrada se consumieron?", 0, 10000, 37)
    e = st.number_input("¿Ayer (o semana pasada) cuántas piezas de madera aserrada se consumieron?", 0, 10000, 18)
    g = st.number_input("¿Cuánto días (o semanas) debe esperar la recepción de maderas después de la colocación de la orden?", 0, 300, 5)
    
    
    data = [a, b, c, d, e]
    SD = np.std(data, ddof=1) 
    import math
    Inventario_seguridad1 = 2.33 * SD * math.sqrt(g)
    Inventario_seguridad5 = 1.64 * SD * math.sqrt(g)   
    Inventario_seguridad10 = 1.28 * SD * math.sqrt(g)

    st.write("##### Resultado de cálculo:") 
    st.write("###### Volumen de inventaruio de seguridad con la probabilidad de escasez de 1% (piezas)")
    st.text(round(Inventario_seguridad1))
    st.write("###### Volumen de inventaruio de seguridad con la probabilidad de escasez de 5% (piezas)")
    st.text(round(Inventario_seguridad5))
    st.write("###### Volumen de inventaruio de seguridad con la probabilidad de escasez de 10% (piezas)")
    st.text(round(Inventario_seguridad10))

elif rubro == "Panadería":
    st.title("¿Cómo analizar la operación de Panadería?")

    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### Los clientes compran el pan en efectivo, por ende, la pendería no necesita tanto el capital de trabajo en muchos casos. Sin embargo, la misma demanda se puede elevar, si la variedad de productos es muy alta y/o la panadería tiene muchos sobrantes a desechar.")
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )
        
        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión para el equipo de producción e instalaciones de la tienda es necesaria, al inicio del negocio o al momento de expansión del mismo.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")

    with col2:
        st.write("### :green[Lista de chequeo]")
        st.write("##### :green[Marque todos los puntos que la empresa ha logrado.]")
        OP1 = st.checkbox("¿La panadería se localiza en la zona poblada o comercial? ¿No hay muchos competidores en la zona?")
        OP2 = st.checkbox("¿Intenta reducir los productos sobrantes no vendidos? ¿Intenta vender el pan que elabora cada dia el mismo día?")
        OP3 = st.checkbox("¿Elabora distintos productos con la misma masa de pan?" )
        OP4 = st.checkbox("¿Aplica redes sociales para el mercadeo?" )
        OP5 = st.checkbox("¿Tiene suficiente número de clientes habituales y aplica medidas para que ellos no se aburren?" )
        OP6 = st.checkbox("¿La decoración interior y exterior de la tienda transmite una sensación de limpieza e invita a la compra?" )

    if st.button("Ya la lista de chequeo se ha llenada y vamos a analizar"):
        switch_to_analysis()  # 分析ページに切り替える

if st.session_state['page'] == 'analysis':
        st.write("## :blue[Sugerencias]")
        selected_count = sum([OP1, OP2, OP3, OP4, OP5, OP6])
        
        # Mensaje principal basado en la cantidad de selecciones
        if selected_count == 6:
            st.write("Probablemente el negocio operaría apropiadamente.")
            st.balloons()
        elif selected_count in [4, 5]:
            st.write("El negocio tendrá que mejorar sus operaciones en ciertos puntos.")
        else:
            st.write("El negocio tiene que fortalecerse.")
        
        # Mensajes adicionales para checkboxes no seleccionados
        if not OP1:
            st.write("La presencia de competidores en la misma zona, aunque representa una amenaza, también puede ser una oportunidad. La concentración de varias panaderías en un área específica puede atraer la atención de los consumidores y, como resultado, aumentar las ventas totales en esa zona. En este caso, es deseable que cada tienda ofrezca productos diferenciados.")
        if not OP2:
            st.write("La producción y venta diaria de pan fresco puede fortalecer la competitividad. Sin embargo, esto aumenta la necesidad de capital de trabajos y los costos operativos. Por lo tanto, será importante aumentar clientes habituales, para poder estimar con precisión la demanda diaria de productos.")
        if not OP3:
            st.write("La estandarización puede aumentar las ganancias, reduciendo los costos.")
        if not OP4:
            st.write("Aunque la aplicación de redes sociales será importante, la misma aumentará la carga de trabajos.")
        if not OP5:
            st.write("Posibles medidas para aumentar clientes fijos incluyen; (i) Emitir tarjetas de fidelidad para ofrecer descuentos a los clientes que compran con frecuencia, (ii) lanzar nuevos productos cada mes para mantener a los clientes habituales interesados, (iii) ofrecer una taza de café gratis a los clientes que compran pan, etc.")
        
        # Mensaje final obligatorio
        st.write("En una panadería, cuando hay una gran variedad de productos, tiende a aumentar los costos de venta. Sin embargo, si la variedad de productos es limitada, no será atractivo para los clientes. Es importante aumentar clientes habituales y diseñar una composición de productos adecuada basada en su demanda. Además, al utilizar colores como el marrón y el crema en el diseño interior y exterior de la tienda, se puede estimular el apetito por el pan.")
        st.image("pan.jpg", width = 400)

    st.write("## :blue[Análisis de punto de equilibrio]") 
    st.write("En un negocio como panadería, es fácil aplicar el análisis de punto de equilibrio, que puede identificar el monto a debe vender. La siguiente calculadora lo facilita.")
    st.write("###### Se puede calcular la meta de venta, en base al análisis del punto de equilibrio. Mientras que el siguiente ejemplo se refiere a un caso de panadería, esta calculadora se puede aplicar en cualquier negocio.")  
    a = st.number_input("Precio unitario (¿cuánto cuesta un paquete de panes a vender como promedio?, GTQ)", 1, 100000000000, 15)
    b = st.number_input("Costo variable unitario (¿cuánto vale el costo de materias primas para un paquete?, GTQ)", 0, 100000000000, 3)
    c = st.number_input("Costo fijo mensual (alquiler del espacio, depreciación de la maquina, costo de electricidad, etc., GTQ)", 1, 100000000000, 3000)
    d = st.number_input("Ganancias mensuales que desea (GTQ)", 1, 10000000000, 800)
    CM = a-b
    CMR = CM/a
    st.write("##### Monto de la venta necesaria para alcanzar la ganancia deseada (GTQ)")
    st.text(round((c+d)/(CMR)))
    st.write("##### Punto de equilibrio en venta (GTQ)")
    st.text(round(c/CMR))
                    
elif rubro == "Restaurante(Comedor)":
    st.title("¿Como analizar la operación de Restaurante/Comedor?")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### Los clientes pagan en efectivo, por ende, el restaurante no tiene alta demanda para el capital de trabajo, siempre y cuando el mismo no se opera en el espacio alquilado.")
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )
        
        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión es necesaria, al inicio del negocio o al momento de expansión del mismo.")
        st.write("###### Cuando el fuego y el aceite se utilizan mucho en la cocina, el coste de actualizar el equipamiento de la cocina es relativamente alto.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")

    with col2:
        st.write("### :green[Lista de chequeo]")
        st.write("##### :green[Marque todos los puntos que la empresa ha logrado.]")
        OP1 = st.checkbox("¿El restaurante se localiza en la zona poblada o comercial? ¿No hay muchos competidores en la zona o puede generar la sinergia positiva con otros comedores vecinales?")
        OP2 = st.checkbox("Si ofrece alta variedad de menú, su operación será complicada. En este caso, ¿el negocio intenta mejorar la eficiencia operativa?"  )
        OP3 = st.checkbox("El costo de materias primas representa alrededor de 20 o 30% del monto de venta, en muchos casos. ¿El negocio intenta mejorar el uso de materias primas?" )
        OP4 = st.checkbox("En caso que el comedor opera como comida rapida del tipo bufé, debe tener el inventario de comidas precocinados. En este caso, ¿el comedor tiene suficientes clientes fijos y puede estimar el volumen de la demanda de los clientes?" )
        OP5 = st.checkbox("¿Aplica redes sociales?" )
        OP6 = st.checkbox("¿Tiene suficiente número de clientes habituales y aplica medidas para que ellos no se aburren?" )
        OP7 = st.checkbox("¿Intenta incrementar la rotación de clientes?" )

    if st.button("Ya la lista de chequeo se ha llenada y vamos a analizar"):
        switch_to_analysis()  # 分析ページに切り替える

if st.session_state['page'] == 'analysis':
        st.write("## :blue[Sugerencias]")
        selected_count = sum([OP1, OP2, OP3, OP4, OP5, OP6, OP7])
        
        # Mensaje principal basado en la cantidad de selecciones
        if selected_count == 7:
            st.write("Probablemente el negocio operaría apropiadamente.")
            st.balloons()
        elif selected_count in [4, 5, 6]:
            st.write("El negocio tendrá que mejorar sus operaciones en ciertos puntos.")
        else:
            st.write("El negocio tiene que fortalecerse.")
        
        # Mensajes adicionales para checkboxes no seleccionados
        if not OP5:
            st.write("Aunque la aplicación de redes sociales será importante, la misma aumentará la carga de trabajos.")
        if not OP1:
            st.write("Si en una misma zona hay restaurantes que se diferencian entre sí, se puede aumentar el volumen de ventas de toda la zona. Por ejemplo, si en una misma zona hay una pizzería, un restaurante de comida peruana y un comedor de carne asado, pueden atraer a diferentes tipos de clientes sin competir directamente entre sí, aumentando así el atractivo general de la zona.")
        
        # Mensaje final obligatorio
        st.write("En un restaurante, una amplia variedad de platos en el menú complica la adquisición de materias primas y la gestión de inventario. Además, si se producen faltantes, la incapacidad de atender los pedidos de los clientes puede generar insatisfacción. Por otro lado, si el menú es demasiado limitado, puede resultar poco atractivo para los clientes. Por lo tanto, es recomendable ofrecer un menú del día para evitar que los clientes se aburran y simplificar las operaciones al poder atender pedidos similares. Las ventas de un restaurante se pueden estimar en función de la cantidad de asientos, por lo que se recomienda utilizar la siguiente calculadora.")

    st.header(" :blue[Herramienta para estimar el monto de venta del comedor]", divider="blue") 
    st.write("###### :blue[El monto de la venta de un restaurante o cafetería se puede estimar, aplicando esta calculadora. Así, la cooperativa podrá analizar la capacidad de pagos del negocio.]")  
    a = st.number_input("¿Cuánto asientos tiene el comedor?", 0, 1000, 20)
    b = st.number_input("Tasa de ocupacion de los asientos por los clientes (%)", 0, 100, 50)
    c = st.number_input("Veces estimadas de rotación de los clientes al día", 1, 10, 3)
    d = st.number_input("Promedio estimado de la venta por cliente (GTS)", 1, 1000, 40)
    e = st.number_input("Días de operación al mes (Días)", 1, 31, 25)

    st.write("###### :red[La tasa de ocupacion puede ser 50%, ya que sólo dos personas pueden ocupar la mesa para cuatro personas. La rotacion de los clientes al día puede ser 4 o 5 veces, como 2 rotaciones a horas de almuerzo y 2 rotaciones a horas de cena.]")
    E = a*d*(b/100)*c

    st.write("##### Resultado del cálculo: Monto esperado de la venta diaria")
    st.text(E)
    st.write("##### Resultado del cálculo: Monto esperado de la venta mensual")
    st.text(E*e)

            
elif rubro == "Negocio de impresión":
    st.title("¿Cómo analizar la operación del Negocio de impresión?")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### Los negocios de la impresión suelen basarse de la demanda local. Si una empresa tiene cierto número de clientes habituales, su flujo de caja podrá ser estable.")
        st.write("###### La mayoría (alrededor de 70%) de los costos operativos son de los papeles. Si la empresa los compra en efectivo, necesitará el monto relativamente alto del capital de trabajo.")
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )

        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión es necesaria, al inicio del negocio y/o para actualización tecnológica.")
        st.write("###### Ciertas empresas de imresión necesitan inversiones de (i) computadoras para diseño gráficos, y (ii) máquina de imprenta para diferentes materiales. El equipo de imprenta es apropiado para aplicar leasing.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")

    with col2:
        st.write("### :green[Lista de chequeo]")
        st.write("##### :green[Marque todos los puntos que la empresa ha logrado.]")
        OP1 = st.checkbox("Dado que muchos negocios de impresión son de la industria intensiva en la maquinaria, el monto de ganancias depende mucho de la tasa de utilización de los equipos de imprenta. ¿El negocio tiene suficientes clientes locales, que colocan las ordenes directas para que la empresa mantenga alta tasa de utilización de los equipos?")
        OP2 = st.checkbox("La tasa de utilización de los equipo de imprenta puede bajarse por (i) el tiempo preparatorio largo, (ii) los cambios operativos frecuentes y/o (iii) la falta del mantenimineto ¿No se observan estos?"  )
        OP3 = st.checkbox("¿La tecnología aplicada de la empresa es bien actualizada, en términos de diseño gráfico e impresión en diferentes materiales tales como ropas, letrero de anuncio, etc.? ¿Así sus productos y servicios ya están bien diversificados?" )

    if st.button("Ya la lista de chequeo se ha llenada y vamos a analizar"):
        st.write("## :blue[Sugerencias]")
        selected_count = sum([OP1, OP2, OP3])
        
        # Mensaje principal basado en la cantidad de selecciones
        if selected_count == 3:
            st.write("Probablemente el negocio operaría apropiadamente.")
            st.balloons()
        elif selected_count in [1, 2]:
            st.write("El negocio tendrá que mejorar sus operaciones en ciertos puntos.")
        else:
            st.write("El negocio tiene que fortalecerse.")
        
        # Mensajes adicionales para checkboxes no seleccionados
        if not OP1 or not OP2:
            st.write("La elavación de la tasa de operación del equipo será escencial para aumentar las ganacias, en caso del negocio intensivo en la maquinaria como la empresa de impresión.")
        if not OP3:
            st.write("La actualizacion de la tecnología requiere el empleo de ingenieros nuevos y/o la compra de nueva maquinaria. Es importante analizar si vale la pena realizar dichas medidas para la innovación, considerando la situación de clientes y competidores.")
        
        # Mensaje final obligatorio
        st.write("En un negocio de impresión, la operación depende de las ordenes de los clientes. Es decir, el negocio inicia el diseño y prepara el arreglo de la maquinaria, después de la recepción de la orden, puesto que la empresa deberá producir los productos variados, dependiendo de las ordenes. En este sentido, la mejora de ediciencia operativa en términos de la ingeniería industrial, es uno de los temas importantes.")

elif rubro == "Construcción":
    st.title("¿Cómo analizar la operación del negocio de Construcción?")

    col1, col2 = st.columns(2)
    
    with col1: 
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### Si la empresa tiene que esperar cierta parte de los pagos del cliente hasta la finalización de la obra, la demanda del capital de trabajo será elevada.")
        st.write("###### La mayoría de la demanda del capital de trabajo puede ser de la remuneración de trabajadores.")
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )
    
        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión es necesaria para compras de terreno, almacén de materias, y maquinaria para la construcción, al inicio del negocio y/o para actualización tecnológica.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")
   
    with col2:
        st.write("### :green[Lista de chequeo]")
        st.write("##### :green[Marque todos los puntos que la empresa ha logrado.]")
        OP1 = st.checkbox("Dado que la operación del negocio de construcción se basa en el manejo de recursos humanos, ¿el negocio puede contratar trabajadores con buena capacidad?")
        OP2 = st.checkbox("Dado que el negocio puede tener alta demanda del capital de trabajo, ¿el negocio puede estimar el flujo de caja para proximos 3 o 6 meses?")
        OP3 = st.checkbox("¿El negocio se subcontrata por otra empresa más grade? ¿En caso afirmativo, su cliente paga con buenas condiciones?")

    if st.button("Ya la lista de chequeo se ha llenada y vamos a analizar"):
        st.write("## :blue[Sugerencias]")
        selected_count = sum([OP1, OP2, OP3])
        
        # Mensaje principal basado en la cantidad de selecciones
        if selected_count == 3:
            st.write("Probablemente el negocio operaría apropiadamente.")
            st.balloons()
        elif selected_count in [1, 2]:
            st.write("El negocio tendrá que mejorar sus operaciones en ciertos puntos.")
        else:
            st.write("El negocio tiene que fortalecerse.")
        
        # Mensajes adicionales para checkboxes no seleccionados
        if not OP2 or not OP3:
            st.write("El manejo del capital de trabajo es uno de los temas pripriotarios en el negocio de construcción. Si el negocio debe mantener cierto volumen del inventario de materias primas, tendrá que identificar el volumen apropiado a mantener.")
        
        # Mensaje final obligatorio
        st.write("En el negocio de construcción, la demanda depende mucho de la economía local y su flujo circulante de fondos. Además, el mismo negocio puede generar la demanda de otras industrias. En este sentido, es importante analizar tambien el entorno del negocio también para el desarrollo del negocio.")

elif rubro == "Corte y confección":
    st.title("¿Cómo analizar la operación del negocio de Corte y confección?")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### La demanda del capital de trabajo es relativamente alta, ya que se necesita cierto tiempo desde la compra de materias primas hasta la venta (entrega) de los productos. Si el negocio reduce el tiempo operativo para la producción, podrá operar con menos monto del capital de trabajo.")
        st.write("###### La mayoría de la demanda del capital de trabajo puede ser de la remuneración de trabajadores y costos de materias primas.")
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )
    
        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión es necesaria para maquina de coser y bordar, al inicio del negocio y/o para actualización tecnológica. La maquina industrial de coser puede ser apropiado para aplicarse leasing.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")

    with col2:
        st.write("### :green[Lista de chequeo]")
        st.write("##### :green[Marque todos los puntos que la empresa ha logrado.]")
        OP1 = st.checkbox("Si el negocio tiene diferentes procesos productivos, ¿no se observan muchos productos en procesos y/o muchos desperdicios de materias primas, debido al desequibrio de lineas productivas?")
        OP2 = st.checkbox("Si el negocio tiene muchos trabajadores empleados, ¿no se observa alta diferencia de la capacidad técnica entre los trabajadores? Pues, la misma generará el desequibrio de líneas productivas, causando la falta del capital de trabajo.")
        OP3 = st.checkbox("Si el negocio tiene las maquinas modernas de coser y bordar, ¿dichas maquinas tengan alta tasa de operación, sin la producción innecesaria?")
        OP4 = st.checkbox("¿El negocio intenta reducir el tiempo desde la compra de materias primas hasta la venta (entrega) de productos?")
        OP5 = st.checkbox("En muchos casos, el negocio de corte y confección produce los productos después de la recepción de los ordenes. ¿El negocio tiene clientes habituales o rutas fijas de la venta?")
    
    if st.button("Ya la lista de chequeo se ha llenada y vamos a analizar"):
        st.write("## :blue[Sugerencias]")
        selected_count = sum([OP1, OP2, OP3, OP4, OP5])
        # Mensaje principal basado en la cantidad de selecciones
        if selected_count == 5:
            st.write("Probablemente el negocio operaría apropiadamente.")
            st.balloons()
        elif selected_count in [3, 4]:
            st.write("El negocio tendrá que mejorar sus operaciones en ciertos puntos.")
        else:
            st.write("El negocio tiene que fortalecerse.")
        
        # Mensajes adicionales para checkboxes no seleccionados
        if not OP1 or not OP2 or not OP3 or not OP4:
            st.write("Procesos de producción en la industria textil tienden a ser complejos. En el caso de las camisas, a menudo se cose por separado las mangas, el cuello y la parte principal, para luego unirlas. En estos casos, si la capacidad de producción de cada componente es variada, aumentará los productos en proceso. Además, si la máquina de coser se descompone con frecuencia en el proceso de unir las diferentes partes, la producción en total se diseminuirá. Será importante asegurar que dicho proceso no se convierta en un cuello de botella. Estos puntos señalados tienen que considerarse, para aumentar las ganancias, reduciendo el monto necesario del capital de trabajo.")
        if not OP5:
            st.write("La operación de un negocio de corte y confección se basa de las ordenes de los clientes, por ende, el suficiente número de clientes fieles podrá aumentar la eficiencia operativa.")
        
        # Mensaje final obligatorio
        st.write("En la mejora de la gestión y la evaluación de necesidades de capital en la industria textil, la existencia de clientes estables y el equilibrio de las líneas productivas suelen ser factores importantes.")
        

elif rubro == "Mercadito(Pulpería)":
    st.title("¿Cómo analizar la operación del negocio de Mercadito(Pulperia)?")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### La demanda del capital de trabajo no sería muy alta, ya que los clientes pagan en efectivo.")
        st.write("###### Si la variedad de artículos es alta y la tienda tiene inventario muerto, la demanda del capital de trabajo estará elevada.")
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )

        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión es necesaria para la tienda y algunas aparatos como estantes, al inicio del negocio y/o al momento de la expanción del negocio.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")

    with col2:
        st.write("### :green[Lista de chequeo]")
        st.write("##### :green[Marque todos los puntos que la empresa ha logrado.]")
        OP1 = st.checkbox("¿La tienda se localiza en la zona poblada o comercial? ¿Puede generar la sinergia positiva con otras tiendas al por menor?")
        OP2 = st.checkbox("¿La tienda reconoce bien qué artículos se venden bien? ¿No tiene inventario muerto de artículos no vendidos? ¿No se ocurre la falta del inventario sobre los artículos demandados bien por sus clientes?" )
        OP3 = st.checkbox("¿El negocio tiene clientes habituales y aplica medidas para que ellos sigan ser clientes fieles?" )
    
    if st.button("Ya la lista de chequeo se ha llenada y vamos a analizar"):
        st.write("## :blue[Sugerencias]")
        selected_count = sum([OP1, OP2, OP3])
        # Mensaje principal basado en la cantidad de selecciones
        if selected_count == 3:
            st.write("Probablemente el negocio operaría apropiadamente.")
            st.balloons()
        elif selected_count in [1, 2]:
            st.write("El negocio tendrá que mejorar sus operaciones en ciertos puntos.")
        else:
            st.write("El negocio tiene que fortalecerse.")
        
        # Mensajes adicionales para checkboxes no seleccionados
        if not OP1:
            st.write("Mientras que otras tiendas vecinales pueden ser competidores, también contribuir para que la zona sea atractiva como el sector comercial.")
        if not OP2:
            st.write("Es importante que el negocio compre los artículos, dependiendo de la demanda.")
        
        # Mensaje final obligatorio
        st.write("La demanda del capital de trabajo depende de compras e inventario de artículos a vender. Dependiendo de la necesidad, será importante asesorar para adecuar proveedores del negocio.")
        
    
elif rubro == "Reparación del auto":
    st.title("¿Cómo analizar la operación del negocio de Reparación del auto?")

    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### La demanda del capital de trabajo no sería alta, ya que los clientes pagan en efectivo.")
        st.write("###### Si el negocio necesita comprar de antemano ciertas partes para la reparación, eso podrá aumentar la necesidad del capital de trabajo.")            
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )
        
        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión es necesaria para maquina de reparaciones, al inicio del negocio y/o para actualización tecnológica.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")

    with col2:
        st.write("### :green[Lista de chequeo]")
        st.write("##### :green[Marque todos los puntos que la empresa ha logrado.]")
        OP1 = st.checkbox("¿El negocio se localiza al lado de carretera u otro sitio apropiado, para atraer la atención de ususarios potenciales?")
        OP2 = st.checkbox("¿Tiene suficiente número de clientes habituales, ofreciendo servicios de inspecciones, cambio de aceite, etc.?")
        OP3 = st.checkbox("¿El negocio tiene trabajadores con buena capacidad?")
        OP4 = st.checkbox("¿El negocio no tiene inventario sobrante de partes para la reparación?")
    
        if st.button("Ya la lista de chequeo se ha llenada y vamos a analizar"):        
            st.write("## :blue[Sugerencias]")
            selected_count = sum([OP1, OP2, OP3, OP4])
            # Mensaje principal basado en la cantidad de selecciones
            if selected_count == 4:
                st.write("Probablemente el negocio operaría apropiadamente.")
                st.balloons()
            elif selected_count in [2, 3]:
                st.write("El negocio tendrá que mejorar sus operaciones en ciertos puntos.")
            else:
                st.write("El negocio tiene que fortalecerse.")
            
        # Mensajes adicionales para checkboxes no seleccionados
        if OP2:
            st.write("Si clientes habituales pagan a crédito, la demanda del capital de trabajo se aumentará.")
        if OP4:       
            st.write("Si no hay proveedores apropiados cerca del negocio, el negocio deberá tener el inventario de las partes. Eso aumentará la demanda del capital de trabajo.")
            
        # Mensaje final obligatorio
        st.write("La demanda del capital de trabajo depende de las condiciones operativas, y es importante intentar reducirla. Si el negocio tiene la maquinaria recien invertida, es importante aumentar la tasa de operación de la misma.")

elif rubro == "Análisis de estados financieros":
    st.title("Análisis de estados financieros")
    st.write("###### Si la empresa solicitante tiene estados financieros, podrá analizarlos, aplicando el siguiente calculador.")

    # Initial values
    initial_values = {
        "Cash": 2000,
        "Inventory": 8000,
        "Other current assets": 5000,
        "Fixed assets": 25000,
        "Short term liabilities": 10000,
        "Long term liabilities": 10000,
        "Capital (equity)": 20000,
        "Annual sales": 50000,
        "Cost of sales (production)": 25000,
        "Administrative expenses": 19000,
        "Financial costs": 5000,
        "Inventory0": 1000,
        "Fixed assets0": 29000,    
        "liabilities0": 17000,            
    }

    # User inputs
    col1, col2 = st.columns(2)
    with col1:
        st.write("##### Resumen de Balances Generales")
        cash = st.number_input("Efectivo", value=initial_values["Cash"])
        inventory = st.number_input("Inventario", value=initial_values["Inventory"])
        other_current_assets = st.number_input("Otros activos corrientes", value=initial_values["Other current assets"])
        fixed_assets = st.number_input("Activos fijos", value=initial_values["Fixed assets"])
        short_term_liabilities = st.number_input("Pasivos a corto plazo", value=initial_values["Short term liabilities"])
        long_term_liabilities = st.number_input("Pasivos a largo plazo", value=initial_values["Long term liabilities"])
        capital_equity = st.number_input("Capital propio", value=initial_values["Capital (equity)"])
    with col2:        
        st.write("##### Resumen del Estado de Resultados")   
        annual_sales = st.number_input("Ventas anuales", value=initial_values["Annual sales"])
        cost_of_sales = st.number_input("Costo de ventas (producciones)", value=initial_values["Cost of sales (production)"])
        admin_expenses = st.number_input("Gastos administrativos", value=initial_values["Administrative expenses"])
        financial_costs = st.number_input("gastos financieros (pago de intereses)", value=initial_values["Financial costs"])

        st.write("##### Informaciones financieras del año anterior (opcional)")
        inventory0 = st.number_input("Inventario en el añó anterior", value=initial_values["Inventory0"])
        fixed_assets0 = st.number_input("Activos fijos en el año anterior", value=initial_values["Fixed assets0"])
        liabilities0 = st.number_input("Pasivos totales en el año pasado", value=initial_values["liabilities0"])


    # Calculations
    total_assets = cash + inventory + other_current_assets + fixed_assets
    total_liabilities_equity = short_term_liabilities + long_term_liabilities + capital_equity

    # Financial Ratios
    current_ratio = (cash + inventory + other_current_assets) / short_term_liabilities
    quick_ratio = (cash + other_current_assets) / short_term_liabilities
    cash_turnover_period = cash / (annual_sales / 12)
    gross_profit_margin = (annual_sales - cost_of_sales) / annual_sales
    operating_income_margin = (annual_sales - cost_of_sales - admin_expenses) / annual_sales
    net_profit_margin = (annual_sales - cost_of_sales - admin_expenses - financial_costs) / annual_sales
    roi = (annual_sales - cost_of_sales - admin_expenses) / total_assets
    capital_adequacy_ratio = capital_equity / total_liabilities_equity
    times_interest_earned = (annual_sales - cost_of_sales - admin_expenses) / financial_costs
    inventory_turnover_period = inventory / (annual_sales / 12)

    if st.button("Analizar"):

        # Display results
        if total_assets != total_liabilities_equity:
            st.warning("El monto total de activos tiene que ser igual a la suma de la deuda y el capital propio.")
            st.metric("Margen de beneficio bruto", round(gross_profit_margin * 100, 2))
            st.metric("Margen de beneficio operativo", round(operating_income_margin * 100, 2))
            st.metric("Margen de beneficio neto", round(net_profit_margin * 100, 2))
        else:
         # Mensaje final obligatorio
            st.write("Será muy ideal que la Razón corriente sea 2 veces o más y la Razón rápida sea 1 vez o más, segun muchos libros de texto, aunque tales libros no son realísticos en algunos casos.")
            st.write("Períodos de rotación de efectivo e inventario no tienen que ser mucho ni poco. Mucho período significa la ineficiencia operativa, y poco período quiere decir la falta de dichos recursos.")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write("##### Indicadores de estabilidad y liquidez")
                st.metric("Razón corriente (Current ratio) (veces)", round(current_ratio, 2))
                st.metric("Razón rápida (Quick ratio) (veces)", round(quick_ratio, 2))
                st.metric("Período de rotación de efectivo (meses)", round(cash_turnover_period, 2))
                st.metric("Razón de adecuación de capital (veces)", round(capital_adequacy_ratio * 100, 2))
                st.metric("Veces de interés ganado (veces)", round(times_interest_earned, 2))   
            with col2:
                st.write("##### Indicadores de rentabilidad y eficiencia")
                st.metric("ROI (Retorno sobre activos totales) (%)", round(roi * 100, 2))
                st.metric("Margen de beneficio bruto (%)", round(gross_profit_margin * 100, 2))
                st.metric("Margen de beneficio operativo (%)", round(operating_income_margin * 100, 2))
                st.metric("Margen de beneficio neto (%)", round(net_profit_margin * 100, 2))
                st.metric("Período de rotación de inventario (meses)", round(inventory_turnover_period, 2))
                
             # Warnings
            if current_ratio <= 1 or quick_ratio <= 0.6 or cash_turnover_period <= 0.8:
                st.warning("El negocio puede tener dificultades en su liquidez.")
            if operating_income_margin <= 0.05:
                st.warning("La rentabilidad del negocio puede ser baja.")
            if inventory_turnover_period >= 3:
                st.warning("La eficiencia operativa, en términos de rotación de inventario puede ser baja.")
            if cash_turnover_period >= 3:
                st.warning("La eficiencia operativa, en términos de rotación de efectivo puede ser baja.")
            if times_interest_earned <= 1 or capital_adequacy_ratio <= 0.5:
                st.warning("El negocio puede estar altamente endeudado, considerando su nivel de ganancias o nivel del capital propio.")
            
            st.write("El resultado del flujo de caja de la emperesa se presenta abajo. Si el flujo de caja en operación es positivo, el negocio genera beneficios para hacer inversiones en muchos casos. Si el flujo de caja en inversiones es poistivo, el negocio posiblemente vende sus activos fijos para cubrir las pérdidas operativas o pagos de deuda. Si el flujo de caja en finanzas es positivo, la empresa utiliza los préstamos para sus operaciones y/o inversiones.")
            # Cashflow values
            OperationalCF = annual_sales - cost_of_sales - admin_expenses - financial_costs + inventory0 - inventory
            InvestmentCF = fixed_assets0 - fixed_assets
            FinancialCF = short_term_liabilities + long_term_liabilities - liabilities0 
           
            # Data for plotting
            cashflows = {                
                'Flujo de caja en Operación': OperationalCF,
                'Flujo de caja en Inversión': InvestmentCF,
                'Flujo de caja en Finanzas': FinancialCF
            }

            # Colors based on value
            colors = ['blue' if value >= 0 else 'red' for value in cashflows.values()]
            
            # Plotting
            fig, ax = plt.subplots()
            ax.barh(list(cashflows.keys()), list(cashflows.values()), color=colors)
            
            # Adding labels
            for index, value in enumerate(cashflows.values()):
                ax.text(value, index, f'{value}', va='center', ha='left' if value >= 0 else 'right')

            ax.set_xlabel('Cantidad (GTQ)')
            ax.set_title('Resumen del resultado del análisis del flujo de caja')

            # Display in Streamlit
            st.pyplot(fig)

