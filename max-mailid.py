'''

**********************************this code give the code for finding the max number of mail id repeated.*******************************
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
'''
mailid = ['stephen.marquard@uct.ac.za', 'louis@media.berkeley.edu', 'zqian@umich.edu', 'rjlowe@iupui.edu', 'zqian@umich.edu', 'rjlowe@iupui.edu', 'cwen@iupui.edu', 'cwen@iupui.edu', 'gsilver@umich.edu', 'gsilver@umich.edu', 'zqian@umich.edu', 'gsilver@umich.edu', 'wagnermr@iupui.edu', 'zqian@umich.edu', 'antranig@caret.cam.ac.uk', 'gopal.ramasammycook@gmail.com', 'david.horwitz@uct.ac.za', 'david.horwitz@uct.ac.za', 'david.horwitz@uct.ac.za', 'david.horwitz@uct.ac.za', 'stephen.marquard@uct.ac.za', 'louis@media.berkeley.edu', 'louis@media.berkeley.edu', 'ray@media.berkeley.edu', 'cwen@iupui.edu', 'cwen@iupui.edu', 'cwen@iupui.edu']
# for line in handle:
#     if not line.startswith('From '):
#         continue
#     collect = line.split()
#     mailid.append(collect[1])
	
print(mailid)


count = dict()
for mail in mailid:
    count[mail] = count.get(mail, 0)+1

bigcount = 0
bigword = None
print(bigcount, type(bigcount))
for count,word in count.items():
    print(word, type(word))
    print(count)
    if word > bigcount :
        bigcount = word
        bigword = count

print(bigcount,bigword)  
    
