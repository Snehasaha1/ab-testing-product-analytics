import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency
from mysql_connection import get_connection
from scipy.stats import norm

connection = get_connection()

query = """
SELECT *
FROM ab_test_data;
"""

df = pd.read_sql(query, connection)

connection.close()

print("=" * 60)
print("Dataset Loaded")
print("=" * 60)

print(df.head())
print()
print(df.shape)

print("="*60)
print("PURCHASE CONVERSION RATE")
print("="*60)

conversion = (
    df.groupby("ExperimentGroup")["Purchased"]
      .mean()
      .reset_index()
)

conversion["ConversionRate"] = conversion["Purchased"] * 100

print(conversion)

print("=" * 60)
print("CHI-SQUARE TEST")
print("=" * 60)

contingency_table = pd.crosstab(
    df["ExperimentGroup"],
    df["Purchased"]
)

print(contingency_table)

chi2, p_value, dof, expected = chi2_contingency(contingency_table)

print()
print("=" * 60)
print("CHI-SQUARE TEST RESULTS")
print("=" * 60)

print(f"Chi-Square Statistic : {chi2:.4f}")
print(f"P-Value              : {p_value:.6f}")
print(f"Degrees of Freedom   : {dof}")

print()
print("Expected Frequencies")
print(expected)

print()
print("=" * 60)
print("INTERPRETATION")
print("=" * 60)

alpha = 0.05

if p_value < alpha:
    print("Reject the Null Hypothesis")
    print("The difference between Group A and Group B is statistically significant.")
    print("The new version (Group B) performs significantly better.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("There is no statistically significant difference between the two groups.")

    print("=" * 60)
print("AVERAGE REVENUE")
print("=" * 60)

revenue = (
    df.groupby("ExperimentGroup")["Revenue"]
      .mean()
      .reset_index()
)

print(revenue)

print("=" * 60)
print("INDEPENDENT T-TEST")
print("=" * 60)

group_A = df[df["ExperimentGroup"] == "A"]["Revenue"]
group_B = df[df["ExperimentGroup"] == "B"]["Revenue"]

t_stat, p_value = ttest_ind(
    group_A,
    group_B,
    equal_var=False
)

print(f"T Statistic : {t_stat:.4f}")
print(f"P Value     : {p_value:.6f}")

print()

if p_value < 0.05:
    print("Reject the Null Hypothesis")
    print("Average revenue is significantly different.")
    print("Group B generates significantly higher revenue.")
else:
    print("Fail to Reject the Null Hypothesis")
    print("No significant difference in revenue.")

    print("=" * 60)
print("REVENUE LIFT")
print("=" * 60)

revenue_A = revenue.loc[revenue["ExperimentGroup"] == "A", "Revenue"].values[0]
revenue_B = revenue.loc[revenue["ExperimentGroup"] == "B", "Revenue"].values[0]

revenue_lift = ((revenue_B - revenue_A) / revenue_A) * 100

print(f"Revenue Lift : {revenue_lift:.2f}%")

print()
print("=" * 60)
print("CONVERSION LIFT")
print("=" * 60)

conversion_A = conversion.loc[
    conversion["ExperimentGroup"] == "A",
    "ConversionRate"
].values[0]

conversion_B = conversion.loc[
    conversion["ExperimentGroup"] == "B",
    "ConversionRate"
].values[0]

conversion_lift = ((conversion_B - conversion_A) / conversion_A) * 100

print(f"Conversion Lift : {conversion_lift:.2f}%")

print()
print("=" * 60)
print("EXECUTIVE SUMMARY")
print("=" * 60)

print(f"Version A Conversion : {conversion_A:.2f}%")
print(f"Version B Conversion : {conversion_B:.2f}%")
print()

print(f"Average Revenue A : ${revenue_A:.2f}")
print(f"Average Revenue B : ${revenue_B:.2f}")
print()

print(f"Revenue Lift : {revenue_lift:.2f}%")
print(f"Conversion Lift : {conversion_lift:.2f}%")
print()

print("Recommendation:")

if p_value < 0.05:
    print("Deploy Version B to all users.")
else:
    print("Continue running the experiment.")

    print()
print("=" * 60)
print("DEVICE-WISE CONVERSION RATE")
print("=" * 60)

device_conversion = (
    df.groupby(["Device", "ExperimentGroup"])["Purchased"]
      .mean()
      .reset_index()
)

device_conversion["ConversionRate"] = (
    device_conversion["Purchased"] * 100
)

print(device_conversion)

print()
print("=" * 60)
print("BROWSER-WISE CONVERSION")
print("=" * 60)

browser_conversion = (
    df.groupby(["Browser", "ExperimentGroup"])["Purchased"]
      .mean()
      .reset_index()
)

browser_conversion["ConversionRate"] = (
    browser_conversion["Purchased"] * 100
)

print(browser_conversion)

print()
print("=" * 60)
print("COUNTRY-WISE CONVERSION")
print("=" * 60)

country_conversion = (
    df.groupby(["Country", "ExperimentGroup"])["Purchased"]
      .mean()
      .reset_index()
)

country_conversion["ConversionRate"] = (
    country_conversion["Purchased"] * 100
)

print(country_conversion)

print()
print("=" * 60)
print("TRAFFIC SOURCE CONVERSION")
print("=" * 60)

traffic_conversion = (
    df.groupby(["TrafficSource", "ExperimentGroup"])["Purchased"]
      .mean()
      .reset_index()
)

traffic_conversion["ConversionRate"] = (
    traffic_conversion["Purchased"] * 100
)

print(traffic_conversion)

print()
print("=" * 60)
print("CUSTOMER FUNNEL")
print("=" * 60)

total_users = len(df)
clicked = df["ClickedCTA"].sum()
cart = df["AddedToCart"].sum()
purchased = df["Purchased"].sum()

print(f"Visitors      : {total_users}")
print(f"Clicked CTA   : {clicked}")
print(f"Added To Cart : {cart}")
print(f"Purchased     : {purchased}")

print()

print(f"CTA Rate        : {clicked/total_users*100:.2f}%")
print(f"Cart Rate       : {cart/total_users*100:.2f}%")
print(f"Purchase Rate   : {purchased/total_users*100:.2f}%")

print()
print("=" * 60)
print("DROP-OFF ANALYSIS")
print("=" * 60)

drop1 = total_users - clicked
drop2 = clicked - cart
drop3 = cart - purchased

print(f"Users left before clicking CTA : {drop1}")
print(f"Users left before cart         : {drop2}")
print(f"Users left before purchase     : {drop3}")

print()
print("=" * 60)
print("95% CONFIDENCE INTERVAL")
print("=" * 60)

confidence = 0.95
z = norm.ppf((1 + confidence) / 2)

for group in ["A", "B"]:

    group_data = df[df["ExperimentGroup"] == group]

    n = len(group_data)

    p = group_data["Purchased"].mean()

    margin = z * ((p * (1 - p)) / n) ** 0.5

    lower = (p - margin) * 100
    upper = (p + margin) * 100

    print(f"Group {group}")
    print(f"Conversion Rate : {p*100:.2f}%")
    print(f"95% Confidence Interval : ({lower:.2f}% , {upper:.2f}%)")
    print()

    