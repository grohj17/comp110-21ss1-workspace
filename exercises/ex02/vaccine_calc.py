"""A vaccination calculator."""

__author__ = "730201179"

from datetime import datetime, timedelta

population: str = input("How large is the population? ")
doses_given: str = input("How many doses of the vaccine have already been administered? ")
doses_per_day: str = input("How mainy doses are being given daily? ")
tgt_pct: str = input("What percent of the population are we hoping to vaccinate? ")
target_percent_vaccinated: int = int(tgt_pct)
necessary_vaccinated: float = int(population) * target_percent_vaccinated * .01
already_vaccinated: float = int(doses_given) / 2
remaining_target_unvaccinated: int = round(necessary_vaccinated) - round(already_vaccinated)
vaccinated_daily: float = int(doses_per_day) / 2
tgt_day: float = round(remaining_target_unvaccinated / vaccinated_daily)
today: datetime = datetime.today()
one_day: timedelta = timedelta(int(tgt_day))
tomorrow: datetime = today + one_day
fnl_stmt: str = "We will reach "
fnl_stmt_2: str = "% vaccination in "
fnt_stmt_3: str = " days, which falls on "
print("Population: " + population)
print("Doses administered: " + doses_given)
print("Doses per day: " + doses_per_day)
print("Target percent vaccinated: " + tgt_pct)
print(fnl_stmt + tgt_pct + fnl_stmt_2 + str(tgt_day) + fnt_stmt_3 + tomorrow.strftime("%B %d, %Y"))