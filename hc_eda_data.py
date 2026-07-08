
# =============================================================================
# IMPORTS
# =============================================================================

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# =============================================================================
# LOAD DATA
# =============================================================================

base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(
    base_dir,
    "hc_petr_annual.csv"
)

petr_annual_data = pd.read_csv(path, low_memory=False)



# =============================================================================
# EXPLORATORY DATA ANALYSIS (EDA)
# =============================================================================

print("\n" + "=" * 80)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 80)

# -------------------------------------------------------------------------
# General summary
# -------------------------------------------------------------------------

total_prod = petr_annual_data["prod_pet_annual"].sum()
n_pozos = petr_annual_data["idpozo"].nunique()
n_empresas = petr_annual_data["empresa"].nunique()

summary = pd.DataFrame({
    "total_production": [total_prod],
    "n_wells": [n_pozos],
    "n_companies": [n_empresas]
})

print("\nGENERAL SUMMARY")
print("-" * 80)
print(summary)


# -------------------------------------------------------------------------
# Production summary statistics
# -------------------------------------------------------------------------

production_summary = (
    petr_annual_data["prod_pet_annual"]
    .describe()
    .reset_index()
)

production_summary.columns = ["metric", "value"]

print("\nPRODUCTION SUMMARY")
print("-" * 80)
print(production_summary)

# -------------------------------------------------------------------------
# Production by resource type
# -------------------------------------------------------------------------

resource_summary = (
    petr_annual_data
    .groupby("tipo_de_recurso", as_index=False)
    .agg(
        wells=("idpozo", "nunique"),
        total_production=("prod_pet_annual", "sum"),
        mean_production=("prod_pet_annual", "mean")
    )
    .sort_values("total_production", ascending=False)
)

#Filter =! "NO DISCRIMINADO"

resource_summary_filter = resource_summary[resource_summary["tipo_de_recurso"] != "NO DISCRIMINADO"]

print("\nPRODUCTION BY RESOURCE TYPE")
print("-" * 80)
print(resource_summary_filter)

# -------------------------------------------------------------------------
# Production by basin
# -------------------------------------------------------------------------

basin_summary = (
    petr_annual_data
    .groupby("cuenca", as_index=False)
    .agg(
        wells=("idpozo", "nunique"),
        total_production=("prod_pet_annual", "sum"),
        mean_production=("prod_pet_annual", "mean")
    )
    .sort_values("total_production", ascending=False)
)

print("\nPRODUCTION BY BASIN")
print("-" * 80)
print(basin_summary)

# -------------------------------------------------------------------------
# Production by basin and resource type
# -------------------------------------------------------------------------

basin_resource_summary = (
    petr_annual_data
    .groupby(
        ["cuenca", "tipo_de_recurso"],
        as_index=False
    )
    .agg(
        wells=("idpozo", "nunique"),
        total_production=("prod_pet_annual", "sum"),
        mean_production=("prod_pet_annual", "mean")
    )
    .sort_values(
        ["cuenca", "total_production"],
        ascending=[True, False]
    )
)

print("\nPRODUCTION BY BASIN AND RESOURCE TYPE")
print("-" * 80)
print(basin_resource_summary)

# -------------------------------------------------------------------------
# Production by formacion
# -------------------------------------------------------------------------

formacion_summary = (
    petr_annual_data
    .groupby("formacion", as_index=False)
    .agg(
        pozos=("idpozo", "nunique"),
        total_production=("prod_pet_annual", "sum"),
        mean_production=("prod_pet_annual", "mean")
    )
    .sort_values("total_production", ascending=False)
)

print("\nPRODUCTION BY FORMACION")
print("-" * 80)
print(formacion_summary)

# -------------------------------------------------------------------------
# Production by province
# -------------------------------------------------------------------------

province_summary = (
    petr_annual_data
    .groupby("provincia", as_index=False)
    .agg(
        wells=("idpozo", "nunique"),
        total_production=("prod_pet_annual", "sum"),
        mean_production=("prod_pet_annual", "mean")
    )
    .sort_values("total_production", ascending=False)
)

print("\nPRODUCTION BY PROVINCE")
print("-" * 80)
print(province_summary)

# -------------------------------------------------------------------------
# Production by company
# -------------------------------------------------------------------------

company_summary = (
    petr_annual_data
    .groupby("empresa", as_index=False)
    .agg(
        wells=("idpozo", "nunique"),
        total_production=("prod_pet_annual", "sum"),
        mean_production=("prod_pet_annual", "mean")
    )
    .sort_values("total_production", ascending=False)
)

print("\nPRODUCTION BY COMPANY")
print("-" * 80)
print(company_summary)

# =============================================================================
# SAVE DASHBOARD TABLES
# =============================================================================

dashboard_dir = os.path.join(
    base_dir,
    "dashboard_data"
)

os.makedirs(
    dashboard_dir,
    exist_ok=True
)

# -------------------------------------------------------------------------
# General summary
# -------------------------------------------------------------------------

summary.to_csv(
    os.path.join(
        dashboard_dir,
        "general_summary.csv"
    ),
    index=False
)

# -------------------------------------------------------------------------
# Resource summary
# -------------------------------------------------------------------------

resource_summary_filter.to_csv(
    os.path.join(
        dashboard_dir,
        "resource_summary.csv"
    ),
    index=False
)

# -------------------------------------------------------------------------
# Basin summary
# -------------------------------------------------------------------------

basin_summary.to_csv(
    os.path.join(
        dashboard_dir,
        "basin_summary.csv"
    ),
    index=False
)

# -------------------------------------------------------------------------
# Basin x Resource
# -------------------------------------------------------------------------

basin_resource_summary.to_csv(
    os.path.join(
        dashboard_dir,
        "basin_resource_summary.csv"
    ),
    index=False
)

# -------------------------------------------------------------------------
# Formacion summary
# -------------------------------------------------------------------------

formacion_summary.to_csv(
    os.path.join(
        dashboard_dir,
        "formacion_summary.csv"
    ),
    index=False
)


# -------------------------------------------------------------------------
# Province summary
# -------------------------------------------------------------------------

province_summary.to_csv(
    os.path.join(
        dashboard_dir,
        "province_summary.csv"
    ),
    index=False
)

# -------------------------------------------------------------------------
# Company summary
# -------------------------------------------------------------------------

company_summary.to_csv(
    os.path.join(
        dashboard_dir,
        "company_summary.csv"
    ),
    index=False
)

print("\nDashboard tables saved successfully!")
print(dashboard_dir)