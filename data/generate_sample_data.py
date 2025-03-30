import pandas as pd

# Sample maternal health data
data = {
    "country": ["Kenya", "Nigeria", "Ghana", "Tanzania", "Uganda"],
    "year": [2020, 2021, 2022, 2023, 2024],
    "maternal_mortality_rate": [342, 576, 312, 450, 389],
    "antenatal_care_coverage": [75.5, 63.2, 78.8, 72.4, 69.0],
    "skilled_birth_attendance": [84.1, 62.0, 76.3, 81.5, 79.0],
    "contraceptive_prevalence": [58.2, 44.0, 55.6, 50.1, 48.5],
    "adolescent_birth_rate": [89, 102, 78, 95, 88]
}

df = pd.DataFrame(data)

# Save as CSV
df.to_csv("data/maternal_health.csv", index=False)

print("✅ Sample dataset created: maternal_health.csv")