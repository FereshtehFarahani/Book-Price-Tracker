import pandas as pd
from urllib.parse import urljoin


def save_to_csv(data, filename):
    
    df = pd.DataFrame(data)
    df.to_csv(filename, header=True)
    print(f"Data saved to {filename}")

def build_full_url(current_url, next_page_href):
    return urljoin(current_url, next_page_href)
