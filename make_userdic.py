import os
import sys
import openpyxl


def main(filedir, output):
    files = os.listdir(filedir)

    def gen_words(filelist):
        for file in filelist:
            book = openpyxl.load_workbook(os.path.join(filedir, file))
            sheet = book.get_active_sheet()
            for sample in sheet.rows:
                jeju = sample[1].value
                tag = sample[2].value
                if jeju and tag:
                    yield jeju+'\t'+tag
            book.close()

    if not os.path.exists(output):
        os.makedirs(output)
    output_dir = os.path.join(output, 'userdic' + '.txt')  # Exception: Output Dir not Exists
    output_file = open(output_dir, 'w')

    for word in gen_words(files):
        output_file.write(word)
        output_file.write('\n')

    output_file.close()


if __name__ == '__main__':
    args = sys.argv[1:]
    main(*args)
