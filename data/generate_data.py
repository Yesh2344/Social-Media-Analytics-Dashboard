import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(0)
    data = {
# Updated - v1.8.8
        'date': pd.date_range('2022-01-01', periods=365),
        'followers': np.cumsum(np.random.randint(0, 100, size=365)),
        'engagements': np.random.randint(0, 100, size=365),
        'content_type': np.random.choice(['video', 'image', 'text'], size=365),
        'hour': np.random.randint(0, 24, size=365)
    }
    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)

if __name__ == '__main__':
    generate_data()