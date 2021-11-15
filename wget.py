from re import findall
from requests import get
def wget(options,callback):
    if type(options) == str:
        options = {"url": options}
    options = options | {}
    if options['url'] is None or findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))",options['url']).__len__() == 0: callback('No url provided')
    parts = options['url'].split('/')
    File = parts[len(parts)-1]
    parts = File.split('?')
    File = parts[0]
    parts = File.split('#')
    File = parts[0]
    if options.get('dest') is None: options['dest'] = './'
    if options['dest'][len(options['dest'])-1:1] =='/':
        options['dest'] = options['dest'] + File
    def handle_request_callback(err,res,body):
        if err is not None:
             callback(err)
        else:
            data={
                "filepath":options['dest']
            }
            if res is not None and res.headers is not None:
                data["headers"]= res.headers
            callback(err,data,body)
    if True:
   
           try:
            if options.get('timeout') is not None: timeout=options['timeout']
            else: timeout=2000
            res=get(options['url'], timeout=timeout)
            if type(res.content) == bytes: mode='wb'
            else: mode='w'
            with open(options['dest'], mode=mode) as f:
                f.write(res.content)
            handle_request_callback(None,res,res.content)
           except Exception as err:
            callback(err,None,None)
    

