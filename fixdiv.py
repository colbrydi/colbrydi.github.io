
# coding: utf-8

# In[86]:


import os
path='../colbrydi.github.io/'
files = ['Blog.html', 'category/fun.html', 'category/professional.html']

test=False

for f in files:
    outfile=open('temp.html','w')
    print(path+f)
    fid = open(path+f)
    counter = 0
    article = 0
    for l in fid:
        if "<div class='article'>" in l:
            if article > 0:
                if counter > 0:
                    for i in range(counter+1):
                        if test:
                            print('*******<div>')
                        else:
                            outfile.writelines('</div>')
            article+=1
            counter=1
        else:
            if "/div" in l:
                counter -= 1
                if counter < 0:
                    counter=0
            elif 'div' in l:
                counter += 1
        if test:
            test=True
            #print(l)
        else:
            outfile.writelines(l)
            
    fid.close()
    outfile.close()
    if not test:
        print('saveing')
        os.rename("temp.html", path+f)

