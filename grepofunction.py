def TranslateContestName(name):
    match name:
        case "1. Chouettes de guerre d'Athènes":
            return "athens", "https://docs.google.com/spreadsheets/d/1qHVw-vP0lCIVVsRb--ZYHcxIUGtru0LqKKf2yA1ZoNM/edit?usp=sharing"
        case "2. Hoplites de Sparte":
            return "sparta", "https://docs.google.com/spreadsheets/d/13dxDYJBkYOdjHmXN4BOzw-gIgtai7qZZ3PMxpEEw948/edit?usp=sharing"
        case "3. Pégases de Corinthe":
            return "corinth", "https://docs.google.com/spreadsheets/d/1cNnKSw9rgMlp4J1s_u_gSAHgAe-asZT9a4Vd1wDmVPA/edit?usp=sharing"
        case "4. Éclairs d'Olympe":
            return "olympia", "https://docs.google.com/spreadsheets/d/1L5BBTMLZSxGLskZhUzjYC7K8thOR451Uk0RY5xsPl4s/edit?usp=sharing"
        case _:
            return "Name not valid"
        
def calculate_max_transportable_units(total_population, ship_capacity, ship_population_cost):
    max_units = 0
    best_ship_count = 0
    best_remaining_capacity = 0
    best_remaining_population = 0

    # Try every possible number of ships from the maximum down to 0
    for num_ships in range(total_population // ship_population_cost, -1, -1):
        # Calculate population used by the current number of ships
        population_used_by_ships = num_ships * ship_population_cost
        
        # Calculate remaining population for units
        remaining_population = total_population - population_used_by_ships
        
        # Calculate total transport capacity of the ships
        total_transport_capacity = num_ships * ship_capacity
        
        # The number of units that can be transported
        transportable_units = min(remaining_population, total_transport_capacity)
        
        # Check if this configuration is better
        if transportable_units > max_units:
            max_units = transportable_units
            best_ship_count = num_ships
            best_remaining_capacity = total_transport_capacity - transportable_units
            best_remaining_population = remaining_population

    return {
        'max_ships': best_ship_count,
        'transportable_units': max_units,
        'remaining_capacity': best_remaining_capacity,
        'remaining_population': best_remaining_population - max_units
    }

# Example usage:
total_population = 3490
ship_capacity = 16
ship_population_cost = 5

result = calculate_max_transportable_units(total_population, ship_capacity, ship_population_cost)
print(result)
