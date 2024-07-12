from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# 1. Función para obtener coordenadas de una ciudad
def obtener_coordenadas(ciudad):
    geolocator = Nominatim(user_agent="viaje_app")
    location = geolocator.geocode(ciudad)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

# 2. Función para calcular la distancia entre dos ciudades
def calcular_distancia(ciudad_origen, ciudad_destino):
    coords_origen = obtener_coordenadas(ciudad_origen)
    coords_destino = obtener_coordenadas(ciudad_destino)
    
    if coords_origen and coords_destino:
        distancia_km = geodesic(coords_origen, coords_destino).kilometers
        distancia_millas = geodesic(coords_origen, coords_destino).miles
        return distancia_km, distancia_millas
    else:
        return None, None

# 3. Función para calcular la duración del viaje dependiendo del medio de transporte
def duracion_viaje(distancia_km, medio_transporte):
    if medio_transporte == "auto":
        velocidad = 100  # km/h
    elif medio_transporte == "avion":
        velocidad = 800  # km/h
    elif medio_transporte == "bicicleta":
        velocidad = 20  # km/h
    else:
        velocidad = 5  # km/h (caminando)
    
    duracion_horas = distancia_km / velocidad
    return duracion_horas

def main():
    while True:
        # 4. Solicitar “Ciudad de Origen” y “Ciudad de Destino”, en español
        ciudad_origen = input("Ingrese la Ciudad de Origen (o 's' para salir): ")
        if ciudad_origen.lower() == 's':
            break

        ciudad_destino = input("Ingrese la Ciudad de Destino: ")
        
        # 5. Calcular la distancia entre las ciudades
        distancia_km, distancia_millas = calcular_distancia(ciudad_origen, ciudad_destino)
        
        if distancia_km is None:
            print("No se pudieron encontrar las coordenadas para las ciudades ingresadas.")
            continue

        # 6. Mostrar la duración del viaje en millas, kilómetros y la duración del viaje
        print(f"\nDistancia entre {ciudad_origen} y {ciudad_destino}:")
        print(f"{distancia_km:.2f} km")
        print(f"{distancia_millas:.2f} millas\n")

        # 7. Mostrar la narrativa del viaje
        print("Medios de transporte disponibles: auto, avion, bicicleta, caminando")
        medio_transporte = input("Ingrese el medio de transporte: ").lower()

        duracion_horas = duracion_viaje(distancia_km, medio_transporte)
        
        print(f"\nLa duración estimada del viaje es: {duracion_horas:.2f} horas\n")
        
        # 8. Mostrar detalles del viaje
        print(f"Detalles del viaje desde {ciudad_origen} a {ciudad_destino}:")
        print(f"Distancia: {distancia_km:.2f} km ({distancia_millas:.2f} millas)")
        print(f"Medio de transporte: {medio_transporte}")
        print(f"Duración estimada: {duracion_horas:.2f} horas\n")

if __name__ == "__main__":
    main()
