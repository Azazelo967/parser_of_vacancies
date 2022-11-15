from flask import Flask, render_template, request, redirect

app = Flask("JobScrapper")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/report')
def report():
    job = request.args.get('job')
    if job is None or not str(job):
        return redirect('/')
    else:
        job.lower()
    return render_template('report.html', job=job)


app.run(host="0.0.0.0")

# from hh_parser import hh_get_pages, hh_get_vacancies
# from sj_parser import sj_get_pages, sj_get_vacancies
# import csv
#
#
# # sj_pages = sj_get_pages("https://russia.superjob.ru/vacancy/search/?keywords=python&click_from=facet")
# # sj_vacancies = []
# # for page in sj_pages:
# #     sj_vacancies.extend(sj_get_vacancies(page))
#
# hh_vacancies = hh_get_vacancies("huawei")
#
# all_vacancies = hh_vacancies
# writer = csv.writer(open("test.csv", mode='w', encoding="UTF-8"))
# writer.writerow([*all_vacancies[0].keys()])
# for vacancy in all_vacancies:
#     writer.writerow([*vacancy.values()])
