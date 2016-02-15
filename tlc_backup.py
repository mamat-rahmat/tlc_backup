import requests
import platform
import sys
from bs4 import BeautifulSoup

if(len(sys.argv) != 2):
    print('Wrong arguments. Usage : python tlc_backup.py your_PHPSESSID')
else:
    phpsessid = sys.argv[1]
    cookies = {'PHPSESSID' : phpsessid}
    submission_url = 'http://tokilearning.org/submission/'

    home_response = requests.get(submission_url, cookies=cookies)
    home_html = home_response.text
    soup = BeautifulSoup(home_html, 'html.parser')
    last = soup.find('li', class_='last').a['href'][34:]

    for i in range(1, int(last)+1):
        print('parsing page ', i);
        response = requests.get(submission_url + 'index?ajax=submissiongridview&Submission_page=' + str(i), cookies=cookies)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        submission_rs = soup.find_all('tr', class_=['odd', 'even'])

        for element in submission_rs:
            submission = element.contents
            verdict = submission[3].contents[0]

            if(verdict == 'Accepted') :
                problem = submission[0].a
                problem_id = problem['href'][9:]
                problem_name = problem.contents[0].replace('?', '')
                answer = submission[4].a
                answer_id = answer['href'][12:]
                print('> found solution to problem', problem_id, problem_name, 'with ID', answer_id)
                
                response = requests.get(submission_url + answer_id + '?action=download', cookies=cookies)
                if hasattr(response, 'content_disposition'):
                    content_disposition = response.headers['content-disposition']
                    if(content_disposition[-2:-1] == 'c'):
                        lang = 'c'
                    else:
                        lang = response.headers['content-disposition'][-4:-1]
                    content = response.text
                else:
                    answer_response = requests.get(submission_url + answer_id, cookies=cookies)
                    answer_html = answer_response.text
                    answer_soup = BeautifulSoup(answer_html, 'html.parser')
                    lang = answer_soup.find_all('div', class_='dtable')[1].div.contents[3].text
                    content = answer_soup.find('pre', class_='brush: '+lang).text

                if platform.platform().startswith('Windows'):
                    content = content.replace('\r\n', '\n')
                
                with open('{0}_{1}_{2}.{3}'.format(problem_id, problem_name, answer_id, lang), 'w') as text_file:
                    text_file.write(content)
