# -*- coding: utf-8 -*-
# full stop in unicode: u'\u3002'
# in utf-8: '\xe3\x80\x82'
#encoding: utf-8
#m=r'\xE3\x80\x82'.decode('string-escape')
period = '。'.decode('utf-8')
import re
input_file = "darwin.txt"
output_file = "summary.txt"
f = open(input_file)
f2 = open(output_file,"w")
rlist=f.readlines()
map(str.strip,rlist)
for x in rlist:
    print x
rlist1 = list()
rlist2 = list()
for lines in rlist:
#    print lines
#    rlist1.append(re.findall(b"^([^\xE3\x80\x82]*?)[\xE3\x80\x82])",lines))
     rlist1.append(re.findall("^([^。]*?[。])",lines))
#    rlist2.append(re.findall("[\xE3\x80\x82](.*[\xE3\x80\x82])$",lines))    
#     rlist1.append(re.findall(u"^([^\u3002]+?[\u3002])",lines))
#    rlist2.append(re.findall(u"[\u3002](.*[\u3002])$",lines))
i=0

#for rub in rlist:
#    print rub.decode('utf-8')
for sent in rlist1:
#    print i
#   print i,sent
    filter(lambda x: x,sent)
    print 'hahahaha'
    print ''.join(sent)
    i=i+1
#    for stri in sent:
#        i=i+1
#        print stri
#        f2.writelines(stri+'\n')
#        print '\n'
j=0
"""  
for sent in rlist2:
#    print i
#   print i,sent    
    filter(lambda x: x,sent)
    for stri in sent:
        j=j+1
#        f2.writelines(stri+'\n')
        print stri
        print '\n'
"""
#f2.writelines(rlist1)
#f2.writelines(rlist2)
print i
print j
print '***'
f2.close()
f.close()