import urllib.request
import os, sys




content = ''
attempts = 0
protocol = 'http'
subdomain = 'web135/'
domain = 'j3'
'''
lvl3 = ['']
lvl4 = ['']
lvl5 = ['']
lvl6 = ['']
lvl7 = ['']
lvl8 = ['']'''
root_dir = '../inetpub/wwwroot/wwwlive'

links = ['', 
 'news', 
 'emergency-info',
 'county-departments', 
 'contact-us', 
 'elected-officials',
 'commissioners-and-directors',
 'other-appointed-officials',
 'advisory-boards',
 'directions',
 'subscribe',
 'foilform',
 'contact-us/e-mail-ce',
 'emergency-info/emergency-alert-sign-up',
 ]

'''while attempts < 3:
    try:
        for link in links:
            final_link = protocol +'://'+ subdomain + '.' + domain +'/'+ link
            print('Downloading Webpage: ' + final_link)
            response = urllib.request.urlopen( final_link , timeout = 5 )
            content = str(response.read().decode('utf-8'))
            f = open( link, 'w' )
            print('Writing to: ' + link)
            f.write( content )
            f.close()
            break
    except urllib.request.URLError as e:
        attempts += 1
        print (type(e))'''
        


for link in links:
    dir = root_dir +'/'+ link
    file = dir + '/'+ 'index.html'
    final_link = protocol +'://'+ subdomain + domain +'/'+ link
    print('Downloading Webpage: ' + final_link)
    try:
        response = urllib.request.urlopen( final_link , timeout = 15 )
        content = str(response.read().decode('utf-8'))
    except urllib.request.URLError as e:
        print (str(e))
    if not os.path.isdir(dir):
        os.mkdir( dir)
        print ("Created " + dir + " Folder")
    f = open( file , 'w' )
    print('Writing to: ' + dir)
    f.write( content )
    f.close()
    
