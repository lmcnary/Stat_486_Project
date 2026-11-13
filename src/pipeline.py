
import pandas as pd
import numpy as np

from clean import clean_gas_prices, clean_kwh_prices, clean_cars

gas = clean_gas_prices()
kwh = clean_kwh_prices()
cars = clean_cars()


pricing = pd.merge(
    kwh,
    gas,
    on=["period", "stateid"],
    how="inner"
)

pricing = pricing.rename(
    columns={
        "price": "electricity_price",
        "value": "gas_price",
        "price-units": "electricity_units",
        "units": "gas_units"
    }
)

pricing.to_csv("data/clean/pricing_clean.csv", index=False)

car_pricing = cars.copy()

car_pricing["type"] = np.select(
    [
        car_pricing["Mileage Epa Combined Mpg Electric"].notna(),
        car_pricing["Trim Description"].fillna("").str.contains(r"diesel|tdi|dsl", case=False, na=False) |
        car_pricing["Trim Name"].fillna("").str.contains(r"diesel|tdi|dsl", case=False, na=False) |
        car_pricing["Model Name"].fillna("").str.contains(r"diesel|tdi|dsl", case=False, na=False),
        car_pricing["Trim Description"].fillna("").str.contains(r"hybrid", case=False, na=False) |
        car_pricing["Trim Name"].fillna("").str.contains(r"hybrid", case=False, na=False) |
        car_pricing["Model Name"].fillna("").str.contains(r"hybrid", case=False, na=False),
    ],
    ["electric", "diesel", "hybrid"],
    default="gas"
)

car_pricing = car_pricing[
    car_pricing["type"] != "diesel"
]

ANNUAL_MILEAGE = 13476

car_pricing["5yr_miles"] = ANNUAL_MILEAGE * 5
car_pricing["10yr_miles"] = ANNUAL_MILEAGE * 10

car_pricing["5yr_energy_cost"] = np.where(
    car_pricing["type"] == "electric",
    car_pricing["5yr_miles"] / 100 *
        car_pricing["Mileage Epa Kwh 100 Mi Electric"],
    car_pricing["5yr_miles"] /
        car_pricing["Mileage Combined Mpg"]
)

car_pricing["10yr_gallons_or_kwh"] = np.where(
    car_pricing["type"] == "electric",
    car_pricing["10yr_miles"] / 100 *
        car_pricing["Mileage Epa Kwh 100 Mi Electric"],
    car_pricing["10yr_miles"] /
        car_pricing["Mileage Combined Mpg"]
)

US_AVG_GAS_PRICE = pricing["gas_price"].mean()
US_AVG_ELECTRICITY_PRICE = pricing["electricity_price"].mean()

car_pricing["5yr_cost"] = (
    car_pricing["Trim MSRP"] +
    np.where(
        car_pricing["type"] == "electric",
        car_pricing["5yr_energy_cost"] *
            US_AVG_ELECTRICITY_PRICE,
        car_pricing["5yr_energy_cost"] *
            US_AVG_GAS_PRICE
    )
)

car_pricing["10yr_cost"] = (
    car_pricing["Trim MSRP"] +
    np.where(
        car_pricing["type"] == "electric",
        car_pricing["10yr_gallons_or_kwh"] *
            US_AVG_ELECTRICITY_PRICE,
        car_pricing["10yr_gallons_or_kwh"] *
            US_AVG_GAS_PRICE
    )
)

trim = car_pricing["Trim Description"].fillna("")
car_pricing["doors"] = trim.str.extract(r"(\d+)\s*dr", expand=False)
car_pricing["body type"] = trim.str.extract(r"\d+\s*dr\s+(.+?)\s*\(", expand=False)
car_pricing["body type"] = car_pricing["body type"].str.split("w/").str[0]
car_pricing["engine liters"] = trim.str.extract(r"(\d+?\.\d*)L", expand=False)
car_pricing["cylinders"] = (trim.str.extract(r"(\d+)cyl", expand=False))
car_pricing["turbo"] = (trim.str.contains(r"turbo", case=False, na=False))
car_pricing["transmission"] = trim.str.extract(r"(\d+\s*[AM]+|CVT|DCT|DSG|AT|MT|Automatic|Manual)", expand=False)

car_pricing.drop(columns=["Trim Description", "Trim Id", "5yr_miles", "10yr_miles"], inplace=True)

car_pricing.to_csv(
    "data/car_pricing_final.csv",
    index=False
)
