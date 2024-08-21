#!/home/joanne/.venv/bin/python3

import PyPDF2
import argparse as ap
from sys import argv as av
import os

def name_output(OUTPUT_FILE, INPUT_FILE):
	OUTPUT_FILE = INPUT_FILE.replace("/pdf/", "/txt/")
	op = OUTPUT_FILE.rsplit("/txt/").
	ofp = op[0]
	off = op[1].replace(".pdf", ".txt")
	OUTPUT_FILE = ofp.join(off)
	return OUTPUT_FILE

def pdf2text(INPUT_FILE):
	OUTPUT_FILE = name_output(OUTPUT_FILE, INPUT_FILE)
	with open(INPUT_FILE, 'rb') as pdf_file:
		pdf_reader = PyPDF2.PdfReader(pdf_file)
		pdf_text = ''
		for page_num in range(len(pdf_reader.pages)):
			page = pdf_reader.pages[page_num]
			pdf_text += page.extract_text()
		# wd = os.getcwd()
		# path_out_file = wd + "/txt/" 
		# os.makedirs(os.path.dirname(path_out_file), exist_ok=True)
		with open(OUTPUT_FILE, 'w', encoding='utf-8') as out_file:
			out_file.write(pdf_text)
		return

def create_parser():
	av_len = len(av)
	print("num args: ")
	print(av_len)
	print("args: ")
	print(av)
	if av_len != 3:
		print("Must include -i INPUT_FILE and -o OUTPUT_FILE args")
	else:
		p = ap.ArgumentParser()
		# p.add_argument('-o', action='store', dest='OUTPUT_FILE', type=str,
						# help="OUTPUT_FILE - path to output file")
		p.add_argument('-i', action='store', dest='INPUT_FILE', type=str,
						help="INPUT_FILE - path to input file")
		return p.parse_args()
		pass
	return None

def main():
	args = create_parser()
	pdf2text(args.INPUT_FILE)
if __name__== '__main__':
    main()
