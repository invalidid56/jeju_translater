import openpyxl
import re
import sys
import os


def main(corpora, output):
    for corpus in os.listdir(corpora):
        file = os.path.join(corpora, corpus)

        workbook = openpyxl.Workbook()
        sheet = workbook.active

        with open(file, 'r', encoding='utf-16') as text:
            stopwords = [
                re.compile('--'),
                re.compile('구술'),
            ]

            corpus = text.read().splitlines()
            corpus = ''.join(corpus)
            isspeech = re.compile('\d{6}[^(-)]+[(][^(-)]+[)]')

            in_bracket = re.compile('[(][^(-)]+[)]')
            in_text = re.compile('(@|#)[^(-)]+[(]')

            for speech in isspeech.finditer(corpus):
                line = speech.group()
                if stopwords[0].search(line) or stopwords[1].search(line):
                    continue
                else:
                    jeju = in_text.search(line)
                    stan = in_bracket.search(line)
                    if jeju and stan:
                        sheet.append([stan.group()[1:-1], jeju.group()[2:-1]])
                    else:
                        continue

        if not os.path.exists(output):
            os.makedirs(output)
        filename = file[file.rfind('/')+1:file.find('.')]   # TODO: EXCEPTION
        workbook.save(os.path.join(output, filename+'.xlsx'))


if __name__ == '__main__':
    args = sys.argv[1:]
    main(*args)
