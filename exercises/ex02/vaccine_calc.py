"""A vaccination calculator."""

__author__ = "730201179"

from datetime import datetime, timedelta

population: str = input("How large is the population? ")
doses_given: str = input("How many doses of the vaccine have already been administered? ")
doses_per_day: str = input("How mainy doses are being given daily? ")
target_percent_vaccinated_input: str = input ("What percent of the population are we hoping to vaccinate? ")
target_percent_vaccinated: int = int(target_percent_vaccinated_input)
necessary_vaccinated: float = int(population) * target_percent_vaccinated * .01
already_vaccinated: float = int(doses_given) / 2
remaining_target_unvaccinated: int = round(necessary_vaccinated) - round(already_vaccinated)
vaccinated_daily: float = int(doses_per_day) / 2
days_to_target: float = round(remaining_target_unvaccinated / vaccinated_daily)
today: datetime = datetime.today()
one_day: timedelta = timedelta(int(days_to_target))
tomorrow: datetime = today + one_day
print("Population: " + population)
print("Doses administered: " + doses_given)
print("Doses per day: " + doses_per_day)
print("Target percent vaccinated: " + target_percent_vaccinated_input)
print("We will reach " + target_percent_vaccinated_input + "% vaccination in " + str(days_to_target) + " days, which falls on " + tomorrow.strftime("%B, %d, %Y") + ".")