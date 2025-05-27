import pandas as pd

def save_to_csv(data, filename):
    
    df = pd.DataFrame(data)
    df.to_csv(filename, header=True)
    print(f"Data saved to {filename}")