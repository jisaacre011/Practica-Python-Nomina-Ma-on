def exchange_money(budget, exchange_rate):
    """
    Convierte una cantidad de dinero (budget) usando la tasa de cambio dada.
    Devuelve el equivalente en la moneda extranjera.
    """
    return budget * exchange_rate

def main():
    print("=== Calculadora de Divisas para Viajeros Frecuentes ===\n")
    print("Moneda base: USD (dólares estadounidenses)\n")
    
    # Tasas aproximadas de venta (USD a moneda local) en marzo 2026
    tasas = {
        "JPY": 157.0,   # Japón - yenes
        "MXN": 17.55,   # México - pesos mexicanos
        "EUR": 0.859,   # Alemania/Europa - euros
        "COP": 3745,    # Colombia - pesos colombianos
        "DOP": 60.0,    # República Dominicana - pesos dominicanos
        "CNY": 6.90,    # China - yuanes
        "ARS": 1200,    # Argentina - pesos argentinos
        "UAH": 42.0,    # Ucrania - grivnas
        # Puedes agregar más: "GBP": 0.78, "BRL": 5.65, etc.
    }
    
    print("Monedas disponibles:")
    for moneda in tasas:
        print(f"  - {moneda}")
    
    while True:
        moneda_destino = input("\n¿A qué moneda quieres convertir? (ej: JPY, MXN, EUR, COP, DOP, CNY, ARS, UAH) → ").upper()
        if moneda_destino in tasas:
            break
        print("Moneda no reconocida. Intenta de nuevo.")
    
    while True:
        accion = input("¿Quieres COMPRAR esa moneda o VENDER esa moneda? (comprar/vender) → ").lower()
        if accion in ["comprar", "vender"]:
            break
        print("Responde solo 'comprar' o 'vender'.")
    
    try:
        budget = float(input(f"¿Cuántos USD tienes / quieres cambiar? → "))
    except ValueError:
        print("Ingresa un número válido.")
        return
    
    tasa = tasas[moneda_destino]
    
    # Ajuste simple por compra/venta (spread típico ~1-3%)
    if accion == "comprar":
        # Para comprar moneda extranjera → usas tasa de venta (un poco peor)
        tasa_ajustada = tasa * 1.015   # +1.5% aprox (spread ejemplo)
        resultado = exchange_money(budget, tasa_ajustada)
        print(f"\nPara **COMPRAR** {moneda_destino} con {budget:.2f} USD:")
        print(f"→ Recibes aproximadamente **{resultado:,.1f} {moneda_destino}**")
        print(f"(tasa aplicada ≈ {tasa_ajustada:.3f})")
    
    else:  # vender
        # Para vender moneda extranjera y obtener USD → tasa de compra (peor para ti)
        # Invertimos la lógica
        tasa_ajustada = tasa / 1.025   # -2.5% aprox
        resultado = budget / tasa_ajustada   # porque ahora vendes la extranjera
        print(f"\nPara **VENDER** {moneda_destino} y obtener USD:")
        print(f"→ Recibes aproximadamente **{resultado:,.2f} USD**")
        print(f"(tasa aplicada ≈ {tasa_ajustada:.3f})")


if __name__ == "__main__":
    main()