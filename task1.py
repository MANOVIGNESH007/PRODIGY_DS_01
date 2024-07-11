import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def main():
    np.random.seed(0)
    ages = np.random.randint(18, 70, 100)
    genders = np.random.choice(['Male', 'Female'], size=100)
    
    df = pd.DataFrame({'Age': ages, 'Gender': genders})
    
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(df['Age'], bins=15, kde=True, color='skyblue')
    plt.title('Histogram of Ages')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    
    plt.subplot(1, 2, 2)
    gender_counts = df['Gender'].value_counts()
    sns.barplot(x=gender_counts.index, y=gender_counts.values, hue=gender_counts.index, palette='Set2', legend=False)
    plt.title('Bar Chart of Genders')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    
    plt.tight_layout()
    plt.savefig("Task1_Solution.png")
    plt.show()

if __name__ == "__main__":
    main()
