
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
    "produccin-de-pozos-de-gas-y-petrleo-2025.csv"
)

hc_data = pd.read_csv(path, low_memory=False)

# =============================================================================
# DATA QUALITY FUNCTION
# =============================================================================

def data_quality_report(
    df,
    name="Dataset",
    key_cols=["idpozo", "anio", "mes"],
    numeric_cols=["prod_pet", "prod_gas"]
):

    print("\n" + "="*80)
    print(f"DATA QUALITY REPORT: {name}")
    print("="*80)

    # Basic info
    print(f"\nRows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nData types:")
    print(df.dtypes)

    # -------------------------------------------------------------------------
    # Missing values
    # -------------------------------------------------------------------------

    print("\nMISSING VALUES")
    print("-"*80)

    na = df.isna().sum()
    na = na[na > 0].sort_values(ascending=False)

    if len(na) == 0:
        print("No missing values.")
    else:
        print(na)

    # -------------------------------------------------------------------------
    # Duplicates
    # -------------------------------------------------------------------------

    print("\nDUPLICATES")
    print("-"*80)

    print(
    f"Full duplicates: "
    f"{df.duplicated().sum():,}"
    )

    existing_keys = [
    col for col in key_cols
    if col in df.columns
    ]

    if len(existing_keys) > 0:

        print(
        f"Business key used: "
        f"{existing_keys}"
        )

        print(
        f"Business key duplicates: "
        f"{df.duplicated(subset=existing_keys).sum():,}"
        )

    else:

        print(
        "No business key columns found."
        )

    # -------------------------------------------------------------------------
    # Negative values
    # -------------------------------------------------------------------------

    print("\nNEGATIVE VALUES")
    print("-"*80)

    for col in numeric_cols:

        if col in df.columns:

            print(
                f"{col}: "
                f"{(df[col] < 0).sum():,}"
            )

    # -------------------------------------------------------------------------
    # Unique categorical values
    # -------------------------------------------------------------------------

    print("\nCATEGORICAL VARIABLES")
    print("-"*80)

    cat_cols = [
        "idempresa",
        "empresa",
        "tipopozo",
        "tipoestado",
        "cuenca",
        "provincia",
        "tipo_de_recurso",
        "formacion"
    ]

    for col in cat_cols:

        if col in df.columns:

            n = df[col].nunique()

            print(f"\n{col} ({n} unique values)")

            vals = sorted(
                df[col]
                .dropna()
                .astype(str)
                .unique()
            )

            if n <= 20:
                print(vals)
            else:
                print("First 20 values:")
                print(vals[:20])

    print("\n" + "="*80)


# =============================================================================
# CHECK RAW DATA
# =============================================================================

data_quality_report(
    hc_data,
    name="Raw data"
)

# =============================================================================
# FILTER DATA
# =============================================================================

petr_expl_data = hc_data[
    (hc_data["tipopozo"] == "Petrolífero") &
    (hc_data["tipoestado"] == "Extracción Efectiva")
].copy()

# =============================================================================
# CHECK FILTERED DATA
# =============================================================================

data_quality_report(
    petr_expl_data,
    name="Petrolífero + Extracción Efectiva"
)

# =============================================================================
# SAVE FILTERED DATA
# =============================================================================

output_path = os.path.join(
    base_dir,
    "hc_filterdata_petr_explefectiva.csv"
)

petr_expl_data.to_csv(
    output_path,
    index=False
)

print(f"Filtered data saved to:\n{output_path}")

# =============================================================================
# CALCULATE ANNUAL OIL PRODUCTION
# =============================================================================
# The source dataset contains monthly production records
# for a single calendar year. Therefore, annual production
# is obtained by summing monthly production for each well.


group_cols = [
    "idpozo",
    "idempresa",
    "empresa",
    "cuenca",
    "provincia",
    "formacion",
    "tipo_de_recurso"
]

petr_annual_data = (
    petr_expl_data
    .groupby(group_cols)
    .agg(
        n_meses=("mes", "nunique"),
        prod_pet_annual=("prod_pet", "sum")
    )
    .reset_index()
)

print("\nAnnual dataset shape:")
print(petr_annual_data.shape)

print(
    petr_annual_data[
        ["n_meses", "prod_pet_annual"]
    ].describe()
)


# =============================================================================
# CHECK FILTERED DATA
# =============================================================================

data_quality_report(
    petr_annual_data,
    name="Producción de petróleo anual"
)


# =============================================================================
# SAVE OIL ANNUAL PRODUCTION
# =============================================================================

output_path_annual = os.path.join(
    base_dir,
    "hc_petr_annual.csv"
)

petr_annual_data.to_csv(
    output_path_annual,
    index=False
)

print(f"Oil annual production saved to:\n{output_path_annual}")

# =============================================================================
# VIOLIN PLOT FUNCTION
# =============================================================================

def violin_plot(
    data,
    x,
    y,
    title,
    xlabel=None,
    ylabel=None
):

    order = sorted(data[x].dropna().unique())

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.violinplot(
        data=data,
        x=x,
        y=y,
        order=order,
        inner="box",
        ax=ax
    )

    sns.stripplot(
        data=data,
        x=x,
        y=y,
        order=order,
        color="black",
        alpha=0.2,
        size=2,
        ax=ax
    )

    ax.set_title(title)
    ax.set_xlabel(xlabel if xlabel is not None else x)
    ax.set_ylabel(ylabel if ylabel is not None else y)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# =============================================================================
# PLOTS
# =============================================================================

violin_plot(
    data=petr_annual_data,
    x="tipo_de_recurso",
    y="prod_pet_annual",
    title="Distribución de la producción anual de petróleo según el tipo de recurso",
    xlabel="Tipo de recurso",
    ylabel="Producción anual de petróleo (m³)"
)

violin_plot(
    data=petr_annual_data,
    x="cuenca",
    y="prod_pet_annual",
    title="Distribución de la producción anual de petróleo por cuenca",
    xlabel="Cuenca",
    ylabel="Producción anual de petróleo (m³)"
)

