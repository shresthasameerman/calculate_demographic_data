
import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')

    race_count = df['race'].value_counts()

    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    percentage_bachelors = (df['education'] == 'Bachelors').sum() / len(df) * 100

    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = (advanced_education['salary'] == '>50K').sum() / len(advanced_education) * 100

    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = (lower_education['salary'] == '>50K').sum() / len(lower_education) * 100

    min_work_hours = df['hours-per-week'].min()

    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers['salary'] == '>50K').sum() / len(num_min_workers) * 100

    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = (df[df['native-country'] == highest_earning_country]['salary'] == '>50K').sum() / len(df[df['native-country'] == highest_earning_country]) * 100

    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Demographic Data Analysis\n")
        print("1. People of each race:\n", race_count)
        print("\n2. Average age of men:", round(average_age_men, 1))
        print("\n3. Percentage of people with a Bachelor's degree:", round(percentage_bachelors, 1))
        print("\n4. Percentage of people with advanced education earning >50K:", round(higher_education_rich, 1))
        print("\n5. Percentage of people without advanced education earning >50K:", round(lower_education_rich, 1))
        print("\n6. Minimum number of hours a person works per week:", min_work_hours)
        print("\n7. Percentage of people working min work hours and earning >50K:", round(rich_percentage, 1))
        print("\n8. Country with the highest percentage of people earning >50K:", highest_earning_country)
        print("\n   Percentage in that country:", round(highest_earning_country_percentage, 1))
        print("\n9. Most popular occupation for those earning >50K in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'higher_education_rich': round(higher_education_rich, 1),
        'lower_education_rich': round(lower_education_rich, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }
