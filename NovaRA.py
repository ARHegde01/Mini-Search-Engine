from collections import defaultdict
import json
from pymongo import MongoClient
from tkinter import *
#from tkinter import ttk
import urllib
from bs4 import BeautifulSoup
import webbrowser

WEBPAGE_FOLDER = "WEBPAGES_RAW"

def tfidf_acquire( token_docInfo_pair):
	return token_docInfo_pair[1]["tf-idf"]
	
class Search:

	def __init__(self, dName, corpuss):
		self.mHost = MongoClient('localhost', 27017)
		self.database = self.mHost[dName]
		self.data = self.database[corpuss] 
		self.owner = Tk()
		screen_height = self.owner.winfo_screenheight()
		screen_width = self.owner.winfo_screenwidth()
		self.owner.geometry(str(screen_width-100) + "x" + str(screen_height-100))
		self.owner.resizable(0, 0)
		self.ch = int(screen_height/2-50)
		self.cw = int(screen_width/2-50)
		self.qSearch = None
		self.qString = None
		self.newPage()

	def reset_window(self):
		for tab in self.owner.winfo_children():
			tab.destroy()

	def newPage(self):
		self.reset_window()
		window = Frame(self.owner)
		sName = Label(window, text="Nova RA", font=("Times New Roman", 64))
		sName.pack(pady=50)
		self.qSearch = Entry(window, font=("Times New Roman", 64))
		self.qSearch.pack(pady=50)
		dive_button = Button(window, text='Dive', command=self.results, font=("Times New Roman", 50))
		dive_button.pack(side=LEFT, padx=50, pady=50)
		exit_button = Button(window, text='Exit', command=self.owner.quit, font=("Times New Roman", 50))
		exit_button.pack(side=RIGHT, padx=50, pady=50)
		window.place(relx=0.5, rely=0.5, anchor=CENTER)

	def results(self):
		self.qString = self.qSearch.get()
		self.reset_window()
		bg_color = "white" 
		fg_color = "black" 
		header = Label(self.owner, text="Results for '{}'".format(self.qString), bg=bg_color, fg=fg_color)
		header.grid(row=0, column=0, columnspan=3, pady=(20, 10))
		header.config(font=("Times New Roman", 32), anchor="center")
		link_data = self.get_doc_ids(self.qString.lower())
		if link_data:
			for CR, itf_ID in enumerate(link_data, start=1):
				nHeader = Label(self.owner, text=f"{CR}) ", fg=fg_color)
				nHeader.grid(row=CR, column=0, sticky="W")
				nHeader.config(font=("Times New Roman", 24))
				jsonlink = json.load(open("WEBPAGES_RAW/bookkeeping.json"))
				url = jsonlink[itf_ID]
				file_split = itf_ID.split("/")
				fname = f"{WEBPAGE_FOLDER}/{file_split[0]}/{file_split[1]}"
				with open(fname, 'r', encoding='utf-8') as tFile:
					b4 = BeautifulSoup(tFile, 'lxml')
					tTag = b4.find('title')
					if tTag and tTag.string:
						header = tTag.string.strip()
					else:
						header = url
				links = Label(self.owner, text=header, fg="green", cursor="hand1", bg=bg_color)
				links.grid(row=CR, column=1, sticky="W", padx=10)
				links.config(font=("Times New Roman", 24), wraplength=self.owner.winfo_screenwidth()//2, anchor="w")
		else:
			error = Label(self.owner, text="No results found.", bg=bg_color, fg=fg_color)
			error.grid(row=1, column=1)
			error.config(font=("Courier", 24))
		nstitle = Button(self.owner, text="Dive Again", command=self.newPage, bg=bg_color, fg=fg_color)
		nstitle.grid(row=CR+1, column=1, sticky="W", pady=(20, 0))
		nstitle.config(font=("Times New Roman", 24))

	def get_doc_ids(self, query_string: str) -> list:
		doc_freq_tfidf = {}
		results = []
		for query_term in query_string.split():
			query_result = self.data.find({"_id": query_term})
			token_dict = next(query_result, None)
			if token_dict is None:
				continue
			docs_dict = token_dict["Doc_info"]
			for doc_id, attributes in sorted(docs_dict.items(), key=tfidf_acquire, reverse=True):
				freq_tfidf = (1, docs_dict[doc_id]["tf-idf"] * docs_dict[doc_id]["weight_multiplier"])
				if doc_id in doc_freq_tfidf:
					freq_tfidf = (doc_freq_tfidf[doc_id][0] + 1, doc_freq_tfidf[doc_id][1] + freq_tfidf[1])
				doc_freq_tfidf[doc_id] = freq_tfidf
		for doc_id, freq_tfidf in sorted(doc_freq_tfidf.items(), key=lambda x: (-x[1][0], -x[1][1])):
			if len(results) >= 20:
				break
			results.append(doc_id)
		return results

	def pqueryResults(self, docid_tfidf_list: list):
		for i, (docid, tf_idf) in enumerate(docid_tfidf_list[:10]):
			print(f"{i+1}) {docid} {tf_idf[0]} {tf_idf[1]}")


if __name__ == "__main__":
	print("Running Nova RA")
	search_program = Search("II_Database", "FileCorpus")
	mainloop( )