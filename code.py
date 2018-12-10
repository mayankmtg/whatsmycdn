import requests
import sys
import re
import threading
from Queue import Queue



class simulate_get_check_cdn_thread(threading.Thread):
	def __init__(self, queue):
		super(simulate_get_check_cdn_thread, self).__init__()
		self.queue = queue
		self.daemon = True
	def run(self):
		while True:
			domain_name = self.queue.get()
			try:
				self.simulate_get_check_cdn(domain_name)
			except Exception,e:
				print "   Error: %s"%e
			self.queue.task_done()
		
	def simulate_get_check_cdn(self, domain_name):
		#print("Start: ", domain_name)
		URL = "http://www.whatsmycdn.com/?uri="+domain_name+"&location=GL"
		r = requests.get(url = URL)
		html_response = r.text
		is_cdn = False
		for html_line in html_response.split('\n'):
			title_search = re.search('<div class="six columns" style="margin-left: 2px; word-wrap:break-word;">(.*)</div>', html_line, re.IGNORECASE)
			# print(title_search)
			if title_search:
				title = title_search.group(1)
				if(title!='-'):
					is_cdn = True
					break
		if(is_cdn):
			print domain_name,

def check_domains(queue, numthreads = 40):
	for i in range(numthreads):
		t = simulate_get_check_cdn_thread(queue)
		t.start()
	queue.join()



with open('alexatop.csv') as f:

	queue = Queue()

	for line in f:
		domain_name = line.split(',')[1]
		queue.put(domain_name)
	check_domains(queue)
