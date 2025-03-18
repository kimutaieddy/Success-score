import pandas as pd
import numpy as np
import random
# Create a list of random names

def generate_synthetic_data(num_rows=200):
    data = []
    
    for i in range(1, num_rows + 1):
        project_id = f"PRJ-{i:03d}"
        budget = random.randint(100000, 2000000)
        duration_months = random.randint(3, 24)
        employees_impacted = random.randint(50, 500)
        training_hours = random.randint(10, 100)
        communication_score = round(random.uniform(1, 5), 1)
        success_flag = random.choice([0, 1])
        
        data.append({
            "project_id": project_id,
            "budget": budget,
            "duration_months": duration_months,
            "employees_impacted": employees_impacted,
            "training_hours": training_hours,
            "communication_score": communication_score,
            "success_flag": success_flag
        })
    
    return pd.DataFrame(data)

# Generate synthetic data
df = generate_synthetic_data()

# Save to CSV
df.to_csv("synthetic_data.csv", index=False)

# Print sample output
print(df.head())
