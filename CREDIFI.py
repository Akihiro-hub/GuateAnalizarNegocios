import streamlit as st
import numpy as np
import pandas as pd

st.write("## Análisis de negocios (PyMEs) y sus solicitudes del crédito, mediante la entrevista y la visita por el colaborador de la cooperativa
st.write("### :green[(Modelo GuateCrece)]")
st.write("###### Cuando una cooperativa recibe consultas sobre el crédito por un negocio asociado, será importante analizar, mediante la entrevista y la visita, :red[(i) demandas del capital de trabajo o para la inversión y (ii) la situación de la operación de la empresa solicitante]. (NOTA: Los detalles de cada uno de estos puntos a analizar en cada uno de rubros del negocio se presentarán, dependiendo de su selección en las opciones a la izquierda.)")

rubro = st.sidebar.selectbox("Rubro de negocio a analizar", ["Seleccione", "Carpintería", "Panadería", "Restaurante(Comedor)", "Negocio de impresión", "Construcción", "Corte y confección", "Mercadito(Pulpería)", "Escuela del idioma", "Reparación del auto"])

if rubro == "Seleccione":
    st.header(" :green[Puntos a analizar sobre la demanda del fondo en general]", divider="green") 
    st.write("#### :green[(1) ¿Qué tenemos que analizar la solicitud del crédito para el capital de trabajo?]") 
    st.write("###### Cuando una cooperativa recibe la solicitud del crédito, primero, tendrá que analizar el objetivo del uso del crédito. Abajo se presentan los puntos a analizar la solicitud para el capital de trabajo.") 
    st.write("###### El capital de trabajo se necesita para mantener la operación diaria del negocio. Algunas veces, la cantidad necesaria del capital de trabajo se puede aumentar, por (i) la expansión del negocio, (ii) el inventario sobrante, (iii) los costos operativos elevados, (iv) el motivo temporal, etc.") 

    col1, col2 = st.columns(2)
    with col1:
        st.write("##### :red[Lista de chequeo]", divider="red") 
        st.write("###### Con relación a la solicitud del crédito para el capital de trabajo, deberá averiguar los siguientes.")
        OP1 = st.checkbox("¿El negocio no tiene el inventario sobrante? ¿No tiene el inventario de productos que ya están fuera de moda y difíciles de vender? (Si el volumen del inventario se ha aumentado mucho, ¿tiene su causa razonable?)")
        OP2 = st.checkbox("¿Las ventas y compras están y estrían estables hoy y en el futuro? (En caso afirmativo, ¿la empresa aplica ciertas medidas para solucionarla?)")
        OP3 = st.checkbox("¿El valor de las cuentas por cobrar no es muy alto? ¿El mismo no se ha aumentado drasticamente en operaciones recientes?")
        OP4 = st.checkbox("¿El aumento de la necesidad del capital de trabajo se genera por la ineficiencia operativa, tales como la reducción drástica de la venta, aumento considerable del costos operativos, etc.? (En caso afirmativo, ¿la empresa aplica ciertas medidas para solucionarla?)")
        OP5 = st.checkbox("¿El monto de crédito solicitado, para el capital de trabajo normal, no supera el monto a calcular por la siguiente herramienta?")
        OP6 = st.checkbox("¿El empresario no solicita el crédito por otros motivos personales?")
        if OP1 and OP2 and OP3 and OP4 and OP5 and OP6:
            st.toast("¡Buen observado!")
            st.balloons()
        elif OP6:
            st.toast("La ineficiencia operativa, aumento del inventario, etc. aumentarán la demanda del capital de trabajo.")
                
    with col2:
        st.write("##### :blue[Herramienta para el análisis]", divider="blue") 
        st.write("###### :blue[Calculadora del monto total necesario del capital de trabajo normal del negocio]")  
        e = st.number_input("Valor del inventario (GTQ)", 1, 10000000000000, 8000)
        f = st.number_input("Cuentas por pagar (GTQ)", 1, 10000000000000, 2000)
        g = st.number_input("Cuentas por cobrar (GTQ)", 1, 1000000000000, 4000)
        h = e + g - f
        st.write("##### Resultado del cálculo: Monto total necesario del capital de trabajo normal (GTQ):")
        st.text(h)
        st.write("###### :red[Cabe decir que el monto a prestar para el capital de trabajo normal no debe superar dicho monto.]")

    st.write("#### :green[(2) ¿Qué tenemos que analizar la solicitud del crédito para el capital de inversión?]") 
    st.write("###### Cuando una cooperativa recibe la solicitud del crédito, primero, tendrá que analizar el objetivo del uso del crédito. Abajo se presentan los puntos a analizar la solicitud para el capital de inversión.") 
    st.write("###### La inversión se hace para (i) montar o expandir el negocio, (ii) desarrollar nuevos productos y/o (iii) sustituir equipos ya viejos. Cabe decir que la inversión aumentará las necesidades del capital de trabajo.") 

    col1, col2 = st.columns(2)
    with col1:
        st.write("##### :red[Lista de chequeo]", divider="red") 
        st.write("###### Con relación a la solicitud del crédito para el capital de inversión, deberá averiguar los siguientes.")
        OP1 = st.checkbox("¿El motivo de inversión es razonable? (Posibles motivos pueden incluir; compra del equipo nuevo para aumentar la producción, sustitución de equipos ya viejos, y/o desarrollo de nuevos mercados y negocios.)")
        OP2 = st.checkbox("¿La empresa podrá esperar un aumento de la venta por la inversión de nueva maquinaria, recibiendo las ordenes de los clientes?")
        OP3 = st.checkbox("¿La inversión no causará la falta del capital de trabajo, mediante el aumento de costos operativos, incluyendo la compra aumentada de materias primas, costos financieros elevados, etc.?")
        OP4 = st.checkbox("¿El monto de ganancia (más depreciación) supera el importe de reembolso del crédito?")
        OP5 = st.checkbox("¿El negocio tiene suficiente espacio para instalar el equipo a comprar?")
        OP6 = st.checkbox("¿El plan de inversión es financieramente apropiada, aplicando la siguiente herramienta?")
        if OP1 and OP2 and OP3 and OP4 and OP5 and OP6:
            st.toast("¡Buen observado!")
            st.balloons()
        elif OP5:
            st.toast("La inversión aumentará necesidades del capital de trabajo, por ende, deberá analizar bien su factibilidad.")
                
    with col2:
        st.write("##### :blue[Herramienta para el análisis]", divider="blue") 
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
        st.write("###### La inversion con VPN negativo o insuficiente deberá rechazarse.")

    st.header(" :blue[Herramienta de referencia]", divider="blue") 
    st.write("###### :blue[El monto disponible para prestar dependerá de (i) cuota mensual a poder pagar, (ii) tasa de interés, y (iii) período de amortización, como se puede calcular mediante esta herramienta.]")
    a = st.number_input("Cuota mensual (GTQ)", 0, 1000000000, 2000)
    b = st.number_input("Tasa anual de interés %", 0, 100, 18)
    c = st.number_input("periodo de amortización (meses)", 0, 100, 12)
    d = (a * ((1 + b/1200)**c - 1)) / (b/1200 * (1 + b/1200)**c)
    st.write("##### :blue[Resultado del cálculo: Monto total disponible para el crédito (GTQ):]")
    st.text(round(d))

elif rubro == "Carpintería":
    st.title("¿Cómo analizar la operación de Carpintería?")
    col1, col2 = st.columns(2)
    with col1:
        st.write("### :green[Lista de chequeo]")
        OP1 = st.checkbox("¿Materias primas y productos finales se guardan de manera ordenada?")
        OP2 = st.checkbox("En el negocio de carpinteria, el uso eficiente de maderas aserradas es uno de los temas prioritarios para aumentar las ganancias, ya que la mayoría de los costos operativos son de materias primas. ¿No tiene muchos desperdicios a desechar? ¿Buen rendimiento de materias primas (maderas)?" )
        OP3 = st.checkbox("¿El negocio tiene el proveedor que suministra la madera aserrada de manera estable, con buenas condiciones de compras?" )
        OP4 = st.checkbox("¿El negocio tiene ciertos clientes habituales quienes pagan con buenas condiciones, o aplica algunas medidas para estabilizar sus ventas?" )
        OP5 = st.checkbox("¿El negocio intenta reducir el tiempo desde la compra de materias primas hasta la entrega (venta) de los productos a los clientes, para mejorar su flujo de caja?" )
            
        if OP1 and OP2 and OP3 and OP4 and OP5:
            st.toast("¡Probablemente bien operándose!")
            st.balloons()

    with col2:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### El costo de materia prima, sobre todo, maderas aserradas, representa la proporción alta en todos los costos de producción. La demanda del capital de trabajo se puede reducir, mediante (i) el aumento del rendimiento de las materias primas, y/o (ii) la reducción del tiempo entre la compra de materia prima y la venta de productos a los clientes.")
        st.write("###### La cooperativa deberá analizar (i) si el monto solicitado para el crédito será apropiado considerando el volumen del inventario, (ii) si el negocio utiliza eficientemente las materias primas, etc.")
    
        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión para el equipo es necesario, al inicio del negocio o al momento de expansión del mismo. El valor económico de la inversión necesaria se varía mucho, dependinedo del equipo a invertir.")
        st.write("###### La cooperativa deberá analizar (i) si el negocio tiene suficiente espacio para instalar el equipo a comprar, (ii) si el negocio podrá aguantar la elevación del monto necesario del capital de trabajo a generar por la inversión, (iii) otras alternativas que podrán aumentar la producitividad sin inversión, etc.")

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
        st.write("### :green[Lista de chequeo]")
        OP1 = st.checkbox("¿La panadería se localiza en la zona poblada o comercial? ¿No hay muchos competidores en la zona?")
        OP2 = st.checkbox("¿La panadería intenta reducir los productos sobrantes no vendidos? ¿Intenta vender el pan que elabora cada dia el mismo día?")
        OP3 = st.checkbox("¿Se elaboran distintos productos con la misma masa de pan?" )
        OP4 = st.checkbox("¿El negocio aplica redes sociales para el mercadeo?" )
        OP5 = st.checkbox("¿El negocio tiene clientes habituales y aplica medidas para que ellos no se aburren?" )
        if OP1 and OP2 and OP3 and OP4 and OP5:
            st.toast("¡Probablemente bien operándose!")
            st.balloons()
        
    with col2:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### Los clientes compran el pan en efectivo, por ende, la pendería no necesita tanto el capital de trabajo en muchos casos. Sin embargo, la misma demanda se puede elevar, si la variedad de productos es muy alta y/o la panadería tiene muchos sobrantes a desechar.")
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )
        
        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión para el equipo de producción e instalaciones de la tienda es necesaria, al inicio del negocio o al momento de expansión del mismo.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")


elif rubro == "Restaurante(Comedor)":
    st.title("¿Como analizar la operación de Restaurante/Comedor?")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### :green[Lista de chequeo]")
        OP1 = st.checkbox("¿El restaurante se localiza en la zona poblada o comercial? ¿No hay muchos competidores en la zona o puede generar la sinergia positica con otros comedores vecinales?")
        OP2 = st.checkbox("Si el restaurante ofrece alta variedad de menú, su oepración será complicada. En este caso, ¿el negocio intenta mejorar la eficiencia operativa?"  )
        OP3 = st.checkbox("En muchos restaurantes, el costo de matrias primas representa alrededor de 20 o 30% del monto de venta. ¿El negocio intenta mejorar el uso de materias primas?" )
        OP4 = st.checkbox("En caso que el comedor opera como comida rapira del tipo bufé, debe tener el inventario de comidas precocinados. En este caso, ¿el comedor tiene suficientes clientes fijos y puede estimar el volumen de la demanda de los clientes?" )
        OP5 = st.checkbox("¿El negocio aplica redes sociales para el mercadeo?" )
        OP6 = st.checkbox("¿El negocio tiene clientes habituales y aplica medidas para que ellos no se aburren?" )
        OP7 = st.checkbox("¿El negocio intenta incrementar la rotación de clientes?" )
        if OP1 and OP2 and OP3 and OP4 and OP5 and OP6 and OP7:
            st.toast("¡Probablemente bien operándose!")
            st.balloons()
        
    with col2:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### Los clientes pagan en efectivo, por ende, el restaurante no tiene alta demanda para el capital de trabajo, siempre y cuando el mismo no se opera en el espacio alquilado.")
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )
        
        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión es necesaria, al inicio del negocio o al momento de expansión del mismo.")
        st.write("###### Cuando el fuego y el aceite se utilizan mucho en la cocina, el coste de actualizar el equipamiento de la cocina es relativamente alto.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")

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
    st.title("¿Cómo analizar la operación del Negocio de impresion?")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### :green[Lista de chequeo]")
        OP1 = st.checkbox("Dado que muchos negocios de impresión son de la industria intensiva en la maquinaria, el monto de ganancias depende mucho de la tasa de utilización de los equipos de imprenta. ¿El negocio tiene suficientes clientes locales, que colocan las ordenes directas para que la empresa mantenga alta tasa de utilización de los equipos?")
        OP2 = st.checkbox("¿La tasa de utilización de los equipo de imprenta no es baja, debido al (i) tiempo preparatorio, (ii) cambios operativos frecuente y (iii) falta del mantenimineto?"  )
        OP3 = st.checkbox("¿La tecnología aplicada de la empresa es bien actualizada, en términos de diseño gráfico e impresión en diferentes materiales tales como ropas, letrero de anuncio, etc.? ¿Así sus productos y servicios ya están bien diversificados?" )

        if OP1 and OP2 and OP3:
            st.toast("¡Probablemente bien operándose!")
            st.balloons()

    with col2:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### Los negocios de la impresión suelen basarse de la demanda local. Si una empresa tiene cierto número de clientes habituales, su flujo de caja podrá ser estable.")
        st.write("###### La mayoría (alrededor de 70%) de los costos operativos son de los papeles. Si la empresa los compra en efectivo, necesitará el monto relativamente alto del capital de trabajo.")
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )

        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión es necesaria, al inicio del negocio y/o para actualización tecnológica.")
        st.write("###### Ciertas empresas de imresión necesitan inversiones de (i) computadoras para diseño gráficos, y (ii) máquina de imprenta para diferentes materiales. El equipo de imprenta es apropiado para aplicar leasing.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")

elif rubro == "Construcción":
    st.title("¿Cómo analizar la operación del negocio de Construcción?")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### :green[Lista de chequeo]")
        OP1 = st.checkbox("Dado que la operación del negocio de construcción se basa en el manejo de recursos humanos, ¿el negocio puede contratar trabajadores con buena capacidad?")
        OP2 = st.checkbox("Dado que el negocio puede tener alta demanda del capital de trabajo, ¿el negocio puede estimar el flujo de caja para proximos 3 o 6 meses?")
        OP3 = st.checkbox("¿El negocio se subcontrata por otra empresa más grade? ¿En caso afirmativo, su cliente paga con buenas condiciones?")

        if OP1 and OP2 and OP3:
            st.toast("¡Probablemente bien operándose!")
            st.balloons()
        
    with col2:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### Si la empresa tiene que esperar cierta parte de los pagos del cliente hasta la finalización de la obra, la demanda del capital de trabajo será elevada.")
        st.write("###### La mayoría de la demanda del capital de trabajo puede ser de la remuneración de trabajadores.")
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )
    
        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión es necesaria para compras de terreno, almacén de materias, y maquinaria para la construcción, al inicio del negocio y/o para actualización tecnológica.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")

elif rubro == "Corte y confección":
    st.title("¿Cómo analizar la operación del negocio de Corte y confección?")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### :green[Lista de chequeo]")
        OP1 = st.checkbox("Si el negocio tiene diferentes procesos productivos, ¿no se observan muchos productos en procesos y/o muchos desperdicios de materias primas, debido al desequibrio de lineas productivas?")
        OP2 = st.checkbox("Si el negocio tiene muchos trabajadores empleados, ¿no se observa alta diferencia de la capacidad técnica entre los trabajadores? Pues, la misma generará el desequibrio de líneas productivas, causando la falta del capital de trabajo.")
        OP3 = st.checkbox("Si el negocio tiene las maquinas modernas de coser y bordar, ¿dichas maquinas tengan alta tasa de operación, sin la producción innecesaria?")
        OP4 = st.checkbox("¿El negocio intenta reducir el tiempo desde la compra de materias primas hasta la venta (entrega) de productos?")
        OP5 = st.checkbox("En muchos casos, el negocio de corte y confección produce los productos después de la recepción de los ordenes. ¿El negocio tiene clientes habituales o rutas fijas de la venta?")
        
        if OP1 and OP2 and OP3 and OP4 and OP5:
            st.toast("¡Probablemente bien operándose!")
            st.balloons()

    with col2:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### La demanda del capital de trabajo es relativamente alta, ya que se necesita cierto tiempo desde la compra de materias primas hasta la venta (entrega) de los productos. Si el negocio reduce el tiempo operativo para la producción, podrá operar con menos monto del capital de trabajo.")
        st.write("###### La mayoría de la demanda del capital de trabajo puede ser de la remuneración de trabajadores y costos de materias primas.")
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )
    
        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión es necesaria para maquina de coser y bordar, al inicio del negocio y/o para actualización tecnológica. La maquina industrial de coser puede ser apropiado para aplicarse leasing.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")

elif rubro == "Mercadito(Pulpería)":
    st.title("¿Cómo analizar la operación del negocio de Mercadito(Pulperia)?")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### :green[Lista de chequeo]")
        OP1 = st.checkbox("¿La tienda se localiza en la zona poblada o comercial? ¿Puede generar la sinergia positiva con otras tiendas al por menor?")
        OP2 = st.checkbox("¿La tienda reconoce bien qué artículos se venden bien? ¿No tiene inventario muerto de artículos no vendidos? ¿No se ocurre la falta del inventario sobre los artículos demandados bien por sus clientes?" )
        OP3 = st.checkbox("¿El negocio tiene clientes habituales y aplica medidas para que ellos siguen comprar en la tienda?" )
        if OP1 and OP2 and OP3:
            st.toast("¡Probablemente bien operándose!")
            st.balloons()
        
    with col2:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### La demanda del capital de trabajo no sería muy alta, ya que los clientes pagan en efectivo.")
        st.write("###### Si la variedad de artículos es alta y la tienda tiene inventario muerto, la demanda del capital de trabajo estará elevada.")
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )

        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión es necesaria para la tienda y algunas aparatos como estantes, al inicio del negocio y/o al momento de la expanción del negocio.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")

elif rubro == "Reparación del auto":
    st.title("¿Cómo analizar la operación del negocio de Reparación del auto?")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### :green[Lista de chequeo]")
        OP1 = st.checkbox("¿El negocio se localiza al lado de carretera u otro sitio apropiado, para atraer la atención de ususarios potenciales?")
        OP2 = st.checkbox("¿Tiene suficiente número de clientes habituales, ofreciendo servicios de inspecciones, cambio de aceite, etc.?")
        OP3 = st.checkbox("¿El negocio tiene trabajadores con buena capacidad?")
        OP4 = st.checkbox("¿El negocio no tiene inventario sobrante de partes para la reparacion?")
        
        if OP1 and OP2 and OP3 and OP4:
            st.toast("¡Probablemente bien operándose!")
            st.balloons()
    
    with col2:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### La demanda del capital de trabajo no sería alta, ya que los clientes pagan en efectivo.")
        st.write("###### Si el negocio necesita comprar de antemano ciertas partes para la reparación, eso podrá aumentar la necesidad del capital de trabajo.")            
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )
    
        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión es necesaria para maquina de reparaciones, al inicio del negocio y/o para actualización tecnológica.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")


elif rubro == "Escuela del idioma":
    st.title("¿Cómo analizar la operación del negocio de Escuela del idioma español para turistas internacionales?")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### :green[Lista de chequeo]")
        OP1 = st.checkbox("¿La escuela se localiza en la zona a que vienen muchas turistas internacionales?")
        OP2 = st.checkbox("¿El negocio ofrece tambén servicios turísticos?")
        OP3 = st.checkbox("¿El negocio aplica redes sociales y página web para el mercadeo?" )
        OP4 = st.checkbox("¿El negocio tiene servicios diferenciados de sus competidores? ¿Ofrece las clases virtuales, además de presenciales?" )
        if OP1 and OP2 and OP3 and OP4:
            st.toast("¡Probablemente bien operándose!")
            st.balloons()
        
    with col2:
        st.write("### :blue[Necesidades del capital de trabajo]")
        st.write("###### Los clientes pagan en efectivo o tarjeta de crédito, por ende, el negocio no tiene alta demanda para el capital de trabajo.")
        st.write("###### La cooperativa deberá analizar si el objetivo de la solicitud del crédito es apropiado o no." )
        
        st.write("### :blue[Necesidades del capital de inversión]")
        st.write("###### La inversión es necesaria para la comutadora del uso de los almunos y el epacio para las clases, al inicio del negocio o al momento de expansión del mismo.")
        st.write("###### La cooperativa deberá analizar si la inversión no genera complicaciones en el flujo de caja del negocio o no.")

    st.header(" :blue[Calculador del monto de la meta de venta, en base al análisis de punto de equilibrio]", divider="blue") 
    st.write("###### :blue[Se puede calcular la meta de venta, en base al análisis del punto de equilibrio. Este calculadora se aplica con facilidad en casos de negocio de la escuela del idioma.]")  
    a = st.number_input("Precio unitario (¿cuánto un cliente paga a la semana?)", 1, 100000000000, 500)
    b = st.number_input("Costo variable unitario (¿cuánto debe pagar al maestro por cliente a la semana?)", 0, 100000000000, 300)
    c = st.number_input("Costo fijo mensual (alquiler del espacio, depreciación de la computadora, costo de electricidad, etc.)", 1, 100000000000, 8000)
    d = st.number_input("Ganancias mensuales que desea (GTS)", 1, 10000000000, 2000)
    CM = a-b
    CMR = CM/a

    st.write("##### Resultado del cálculo: Monto de la venta necesaria para alcanzar la ganancia deseada")
    st.text((c+d)/(CMR))
    st.write("##### Punto de equilibrio en venta (GTS)")
    st.text(c/CMR)

