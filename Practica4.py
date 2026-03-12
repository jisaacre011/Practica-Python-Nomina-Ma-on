# =================================================================
# PRÁCTICA 4: CALCULADORA DE SUELDO NETO (REPÚBLICA DOMINICANA)
# =================================================================

# --- CONSTANTES DE LEY ---
TSS_PORCENTAJE = 0.0591    # 5.91% (SFS + AFP)
# Escalas anuales ISR DGII
EXENTO_ANUAL = 416220.00
ESCALA1_MAX = 624329.00
ESCALA2_MAX = 867123.00

print("========================================")
print("   SISTEMA DE NÓMINA DOMINICANA  ")
print("========================================\n")

try:
    # 1. Entrada de Sueldo
    sueldo_bruto = float(input("Ingrese el sueldo bruto mensual: RD$ "))
    if sueldo_bruto <= 0:
        print("Error: El sueldo debe ser un valor positivo.")
        exit()

    # 2. Entrada de Descuentos
    otros_descuentos = float(input("Ingrese otros descuentos adicionales: RD$ "))

    # 3. Lógica de Bonificación (Pregunta por antigüedad)
    tiene_bono = input("¿Aplica bonificación este mes? (si/no): ").lower()
    bono = 0
    if tiene_bono == "si":
        # PREGUNTA CLAVE SEGÚN LEY RD
        anos = int(input("¿Cuántos años tiene el empleado en la empresa?: "))
        if anos < 3:
            # 15 días de salario (medio sueldo)
            bono = sueldo_bruto / 2
            print(f"-> Aplica 15 días de salario por antigüedad ({anos} años)")
        else:
            # 30 días de salario (un sueldo completo)
            bono = sueldo_bruto
            print(f"-> Aplica 30 días de salario por antigüedad ({anos} años)")

    # 4. Doble Sueldo
    tiene_doble = input("¿Aplica doble sueldo (Navidad)? (si/no): ").lower()
    doble_sueldo = sueldo_bruto if tiene_doble == "si" else 0

    # --- CÁLCULOS ---
    descuento_tss = sueldo_bruto * TSS_PORCENTAJE
    
    # Cálculo ISR (sobre sueldo tras TSS)
    sueldo_sujeto_isr = (sueldo_bruto - descuento_tss) * 12
    if sueldo_sujeto_isr <= EXENTO_ANUAL:
        isr_anual = 0
    elif sueldo_sujeto_isr <= ESCALA1_MAX:
        isr_anual = (sueldo_sujeto_isr - EXENTO_ANUAL) * 0.15
    elif sueldo_sujeto_isr <= ESCALA2_MAX:
        isr_anual = 31216.00 + ((sueldo_sujeto_isr - ESCALA1_MAX) * 0.20)
    else:
        isr_anual = 79776.00 + ((sueldo_sujeto_isr - ESCALA2_MAX) * 0.25)
    
    descuento_isr = isr_anual / 12

    # Sueldo Neto
    total_descuentos = descuento_tss + descuento_isr + otros_descuentos
    sueldo_neto = (sueldo_bruto + bono + doble_sueldo) - total_descuentos

    # --- RESULTADOS ---
    print("\n" + "-"*40)
    print("        RESUMEN DE PAGO")
    print("-"*40)
    print(f"Sueldo Bruto:        RD$ {sueldo_bruto:>10,.2f}")
    print(f"Bonificación (+):    RD$ {bono:>10,.2f}")
    print(f"Doble Sueldo (+):    RD$ {doble_sueldo:>10,.2f}")
    print(f"Descuento TSS (-):   RD$ {descuento_tss:>10,.2f}")
    print(f"Retención ISR (-):   RD$ {descuento_isr:>10,.2f}")
    print(f"Otros Desc. (-):     RD$ {otros_descuentos:>10,.2f}")
    print("-" * 40)
    print(f"SUELDO NETO FINAL:   RD$ {sueldo_neto:>10,.2f}")
    print("-" * 40)

except ValueError:
    print("Error: Ingrese solo números. Para decimales use punto (.) no coma.")