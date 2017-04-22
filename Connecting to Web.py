'''
import urllib
import urllib2

params = {'param1': 'value1'}

req = urllib2.Request("http://stackoverflow.com/questions/1401941/script-to-connect-to-a-web-page", urllib.urlencode(params))
res = urllib2.urlopen(req)

data = res.read()
'''
'''
import urllib2
aResp = urllib2.urlopen("http://google.com/");
print aResp.read();
'''
import webbrowser
new = 2 #for a new tab
url = "http://docs.python.org/library/webbrowser.html"
webbrowser.open(url,new=new)
