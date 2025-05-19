
from time import sleep,time
from threading import Event
def read(path):
    val = system.tag.readBlocking([path])[0].value
    return val
        
def write(path,value):
	system.tag.writeBlocking([path], value)
	


def fl_m1(f1,f2,f3,r1,r2,r3):
	if(f1==r1 and f2==r2 and f3==r3):
		return True
	else:
		return False
		
def fl_m2(f1,f2,r1,r2):
	if(f1==r1 and f2==r2):
		return True
	else:
		return False
				
def motor_control(chem_no,status,writepath,mix_time_1,mix_time_2,startpath,intr_event,mixername):
	counter = 0
	if(status):
		if(chem_no ==1):
			
			print("chem_no", chem_no)
			system.tag.writeBlocking([writepath], True)
			start_time = time()
			print start_time
			while counter < mix_time_1:
				print 'entered while loop'
				print intr_event
				print counter
				print mix_time_1
				if intr_event.is_set():
					break
				elapsed_time = time() - start_time
				if elapsed_time >= counter + 1:
					counter += 1
				sleep(0.1)
			
			system.tag.writeBlocking([writepath], False)
			print intr_event
			print('mixer stop')
			if(counter>=mix_time_1):
				product = "CHEM-2821"
				name = mixername
				params = [name, 1, product] 
	 			myfunc.insertbatch(params)
			
		elif(chem_no ==2):
			print("chem_no", chem_no)
			system.tag.writeBlocking([writepath], True)
			start_time = time()
			while counter < mix_time_1:
				if intr_event.is_set():
					break
				elapsed_time = time() - start_time
				if elapsed_time >= counter + 1:
					counter += 1
				sleep(0.1)
			
			system.tag.writeBlocking([writepath], False)
			if(counter>=mix_time_1):
				product = "CHEM-3831"
				name = mixername
				params = [name, 1, product] 
	 			myfunc.insertbatch(params)
	 			
	 			
	 	elif(chem_no ==3):
			print("chem_no", chem_no)
			system.tag.writeBlocking([writepath], True)
			start_time = time()
			while counter < mix_time_1:
				if intr_event.is_set():
					break
				elapsed_time = time() - start_time
				if elapsed_time >= counter + 1:
					counter += 1
				sleep(0.1)
			
			system.tag.writeBlocking([writepath], False)
			if(counter>=mix_time_1):
				product = "CHEM-6861"
				name = mixername
				params = [name, 1, product] 
	 			myfunc.insertbatch(params)
		elif(chem_no ==4):
			print("chem_no", chem_no)
			system.tag.writeBlocking([writepath], True)
			start_time = time()
			while counter < mix_time_1:
				if intr_event.is_set():
					break
				elapsed_time = time() - start_time
				if elapsed_time >= counter + 1:
					counter += 1
				sleep(0.1)
			
			system.tag.writeBlocking([writepath], False)
			if(counter>=mix_time_1):
				product = "CHEM-7871"
				name = mixername
				params = [name, 1, product] 
	 			myfunc.insertbatch(params)
			
	system.tag.writeBlocking([startpath], False)
	
def checkintr(mixerpath,startpath,intr_event):
	mixer = myfunc.read(mixerpath)
	start = myfunc.read(startpath)
	while start:
		start = myfunc.read(startpath)
		
		print 'mixer true while loop in checkintr'
		if(start == False):
			intr_event.set()
			print('intrupt')
		mixer = myfunc.read(mixerpath)
		sleep(0.3)
		
	
		

		
def insertbatch(params):
	query = "INSERT INTO production (machine_name, no_batch, product) VALUES (?, ?, ?)"
	rows = system.db.runPrepUpdate(query, params)
	
		
		