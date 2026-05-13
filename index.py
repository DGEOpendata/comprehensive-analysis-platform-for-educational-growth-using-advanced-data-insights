python
import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    """Load dataset from a CSV file."""
    return pd.read_csv(filepath)

def visualize_enrollment_trends(data, start_year, end_year):
    """Visualize student enrollment trends over a range of years."""
    filtered_data = data[(data['Year'] >= start_year) & (data['Year'] <= end_year)]
    enrollment_by_year = filtered_data.groupby('Year')['Student Enrollment'].sum()

    plt.figure(figsize=(10, 6))
    enrollment_by_year.plot(kind='line', marker='o')
    plt.title('Student Enrollment Trends from {} to {}'.format(start_year, end_year))
    plt.xlabel('Year')
    plt.ylabel('Student Enrollment')
    plt.grid(True)
    plt.show()

# Load the educational dataset
data = load_data('Abu_Dhabi_Educational_Institutions_Data.csv')

# Visualize the student enrollment trends
visualize_enrollment_trends(data, start_year=2015, end_year=2026)
