import pandas as pd
import random

def generate_synthetic_data(num_rows=500):
    data = []
    
    for i in range(1, num_rows + 1):
        # Core inputs (from problem description)
        budget = random.randint(100000, 200000000)
        employees_impacted = random.randint(50, 5000)
        duration_months = random.randint(3, 48)
        
        # Readiness metrics (for predictive insights)
        training_hours = random.randint(10, 200)
        communication_score = round(random.uniform(1, 5), 1)
        leadership_alignment = random.choice([0, 1])  # 0=misaligned, 1=aligned
        
        # Financial assumptions (for ROI calculation)
        avg_salary = random.randint(40000, 120000)  # Assume industry average
        productivity_gain = round(random.uniform(0.05, 0.30), 2)  # 5-30% gains
        
        # Simulate success_flag with logical rules (better than random)
        success_flag = 1 if (
            (training_hours >= 40) & 
            (communication_score >= 3.5) & 
            (leadership_alignment == 1)
        ) else 0
        
        data.append({
            # Inputs (from problem description)
            "budget": budget,
            "employees_impacted": employees_impacted,
            "duration_months": duration_months,
            
            # Readiness metrics (for prediction)
            "training_hours": training_hours,
            "communication_score": communication_score,
            "leadership_alignment": leadership_alignment,
            
            # Target variable
            "success_flag": success_flag,
            
            # Financial assumptions (hidden from user)
            "_avg_salary": avg_salary,
            "_productivity_gain": productivity_gain
        })
    
    return pd.DataFrame(data)

# Generate and save data
df = generate_synthetic_data()
df.to_csv("hackathon_data.csv", index=False)