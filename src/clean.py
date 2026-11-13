
import pandas as pd
import numpy as np
from pathlib import Path

SOURCE = Path("data/source")
CLEAN = Path("data/clean")
CLEAN.mkdir(parents=True, exist_ok=True)
GAS_STATE_MAPPING = {
    "YCLE": ["OH"],
    "Y48SE": ["WA"],
    "R5XCA": ["WA", "OR", "NV", "AZ", "AK", "HI"],
    "R1Z": ["WV", "VA", "NC", "SC", "GA", "FL"],
    "SCO": ["CO"],
    "R30": ["NM", "TX", "AR", "LA", "MS", "AL"],
    "R50": ["WA", "OR", "NV", "CA", "AZ", "AK", "HI"],
    "YMIA": ["FL"],
    "R1Y": ["NY", "PA", "MD", "NJ", "DE"],
    "SOH": ["OH"],
    "R40": ["MT", "ID", "WY", "UT", "CO"],
    "SWA": ["WA"],
    "R10": ["ME", "VT", "NH", "MA", "CT", "RI",
            "NY", "PA", "MD", "NJ", "DE", "WV",
            "VA", "NC", "SC", "GA", "FL"],
    "R1X": ["ME", "VT", "NH", "MA", "CT", "RI"],
    "SFL": ["FL"],
    "YDEN": ["CO"],
    "SNY": ["NY"],
    "STX": ["TX"],
    "NUS": ["US"],
    "SMN": ["MN"],
    "R20": ["ND", "SD", "NE", "KS", "OK", "MO",
            "IA", "MN", "WI", "IL", "IN", "MI",
            "OH", "KY", "TN"]
}


def clean_gas_prices():
    gas = pd.read_csv(SOURCE / "gas_prices.csv")

    gas = gas[
        gas["product-name"] == "Conventional Regular Gasoline"
    ].copy()

    gas["stateid"] = gas["duoarea"].map(GAS_STATE_MAPPING)

    gas = gas.explode("stateid")

    gas = gas.groupby(
        ["period", "stateid", "units"],
        as_index=False
    )["value"].mean()

    gas.to_csv(CLEAN / "gas_prices_clean.csv", index=False)

    return gas

def clean_kwh_prices():
    kwh = pd.read_csv(SOURCE / "kwh_prices.csv")

    kwh = kwh[kwh["sectorid"] == "COM"].copy()

    kwh = kwh.drop(
        columns=["stateDescription", "sectorid", "sectorName"]
    )

    kwh["price"] = kwh["price"] / 100
    kwh["price-units"] = "$/kWh"

    kwh.to_csv(CLEAN / "kwh_prices_clean.csv", index=False)

    return kwh

def clean_cars():
    mileage = pd.read_csv(SOURCE / "mileages-sample.csv")

    mileage = mileage.drop(
        columns=[
            "Make Id", "Model Id", "Submodel Id","Mileage Id","Mileage Epa City Mpg","Mileage Epa Highway Mpg",
            "Mileage Range City","Mileage Range Highway","Mileage Epa City Mpg Electric","Mileage Epa Highway Mpg Electric",
            "Mileage Epa Time To Charge Hr 240v Electric", "Mileage Created", "Mileage Modified", "Mileage Range Electric"
        ]
    )

    msrp = pd.read_csv(SOURCE / "trims-sample.csv")

    msrp = msrp.drop(
        columns=[
            "Make Id", "Model Id", "Submodel Id", "Trim Description", 
            "Trim Created", "Trim Modified", "Trim Invoice"
        ]
    )

    cars = pd.merge(
        mileage,
        msrp,
        how="inner",
        on=[
            "Trim Id", "Model Year", "Make Name", "Model Name", 
            "Submodel Name", "Trim Name"
        ]
    )

    cars.to_csv(CLEAN / "cars_clean.csv", index=False)

    return cars
