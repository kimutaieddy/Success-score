import pandas as pd
import numpy as np
import random

def generate_synthetic_data(num_rows=500):
    data = []
    
    for i in range(1, num_rows + 1):
        project_id = f"PRJ-{i:03d}"
        budget = random.randint(100000, 200000000)
        duration_months = random.randint(3, 48)
        employees_impacted = random.randint(50, 5000)
        training_hours = random.randint(10, 200)
        communication_score = round(random.uniform(1, 5), 1)
        success_flag = random.choice([0, 1])
        leadership_alignment = random.choice([0, 1])
        project_management = random.choice([0, 1])
        historical_success_rate = round(random.uniform(0, 100), 2)
        risk_mitigation = round(random.uniform(0, 100), 2)

        data.append({
            "project_id": project_id,
            "budget": budget,
            "duration_months": duration_months,
            "employees_impacted": employees_impacted,
            "training_hours": training_hours,
            "communication_score": communication_score,
            "success_flag": success_flag,
            "leadership_alignment": leadership_alignment,
            "project_management": project_management,
            "historical_success_rate": historical_success_rate,
            "risk_mitigation": risk_mitigation
        })
    
    return pd.DataFrame(data)

# Generate synthetic data
df = generate_synthetic_data()

# Save to CSV
df.to_csv("synthetic_data.csv", index=False)

# Print sample output
print(df.head())
