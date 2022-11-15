import csv


def save_to_csv(vacancies: list):
    writer = csv.writer(open("vacancies.csv", mode='w', encoding="UTF-8"))
    writer.writerow([*vacancies[0].keys()])
    for vacancy in vacancies:
        writer.writerow([*vacancy.values()])