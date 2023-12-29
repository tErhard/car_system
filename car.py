from tabulate import tabulate


class Car:
    
    def __init__(self, fuel_type, fuel_consumption, average_speed):
        self.fuel_type = fuel_type  # Тип пального (дизель або бензин)
        self.fuel_consumption = fuel_consumption  # Витрата палива на 100 км (літри)
        self.average_speed = average_speed  # Середня швидкість (км/год)
        self.CO2_emission_per_liter = {
            'бензин': 9.7,  # кг CO2 на літр
            'дизель': 11.3  # кг CO2 на літр
        }
        self.working_days_per_year = 250  # Кількість робочих днів на рік

    def time_fuel_CO2(self, distance):
        time_per_day = (distance / self.average_speed)  # Час подорожі на день (год)
        fuel_needed_per_day = (distance / 100) * self.fuel_consumption  # Витрати палива на день (літри)
        CO2_emission_per_day = fuel_needed_per_day * self.CO2_emission_per_liter[
        self.fuel_type]  # Кількість викидів CO2 за день (кг)

        time_per_year = time_per_day * self.working_days_per_year  # Час подорожі за рік (год)
        fuel_cost_per_year = fuel_needed_per_day * self.working_days_per_year  # Витрати палива за рік (літри)
        CO2_emission_per_year = CO2_emission_per_day * self.working_days_per_year  # Кількість викидів CO2 за рік (кг)

        return time_per_day, fuel_needed_per_day, CO2_emission_per_day, time_per_year, fuel_cost_per_year, CO2_emission_per_year


# Вибір типу пального
fuel_type_input = input("Виберіть тип пального (дизель або бензин): ").lower()

# Перевірка правильності введеного типу пального
while fuel_type_input not in ['дизель', 'бензин']:
    fuel_type_input = input("Будь ласка, введіть правильний тип пального (дизель або бензин): ").lower()

# Введення витрат палива на 100 км і середньої швидкості
fuel_consumption_input = float(input("Введіть витрати палива на 100 км (літри): "))
average_speed_input = float(input("Введіть середню швидкість (км/год): "))

# Створення екземпляру класу Car з введеними користувачем параметрами
car = Car(fuel_type=fuel_type_input, fuel_consumption=fuel_consumption_input, average_speed=average_speed_input)

# Введення відстані між точками а і b
distance_ab = float(input("Введіть відстань яку долаєте за робочий день (км): "))

# Розрахунок часу, витрат палива та викидів CO2 за день та за рік
time_per_day, fuel_cost_per_day, CO2_emission_per_day, time_per_year, fuel_cost_per_year, CO2_emission_per_year = car.time_fuel_CO2(
    distance_ab)

data = [
    ["День", time_per_day, fuel_cost_per_day, CO2_emission_per_day],
    ["Рік", time_per_year, fuel_cost_per_year, CO2_emission_per_year]
]

headers = ["Період", "Час подорожі (год)", "Витрати палива (л)", "Кількість викидів CO2 (кг)"]

table = tabulate(data, headers, tablefmt="grid")
print(table)
