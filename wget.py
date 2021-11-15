from re import findall
from requests import get
import re

def handle_by_header(Content_Type_Header):
    if Content_Type_Header == 'audio/aac':
        return '.aac'
    elif Content_Type_Header == 'application/octet-stream':
        return '.bin'
    elif Content_Type_Header == 'video/x-msvideo':
        return '.avi'
    elif Content_Type_Header == 'application/x-bzip':
        return '.bz'
    elif Content_Type_Header == 'text/css':
        return '.css'
    elif Content_Type_Header == 'text/csv':
        return '.csv'
    elif Content_Type_Header == 'application/msword':
        return '.doc'
    elif Content_Type_Header == 'application/zip':
        return '.zip'
    elif Content_Type_Header == 'application/x-7z-compressed':
        return '.7z'
    elif Content_Type_Header == 'image/x-icon':
        return '.ico'
    elif Content_Type_Header == 'application/java-archive':
        return '.jar'
    elif Content_Type_Header == 'text/html':
        return '.html'
    elif Content_Type_Header == 'image/jpeg':
        return '.jpg'
    elif Content_Type_Header == 'application/javascript':
        return '.js'
    elif Content_Type_Header == 'application/json':
        return '.json'
    elif Content_Type_Header == 'video/mpeg':
        return 'mpeg'
    elif Content_Type_Header == 'audio/ogg':
        return '.ogg'
    elif Content_Type_Header == 'application/pdf':
        return '.pdf'
    elif Content_Type_Header == 'application/x-rar-compressed':
        return '.rar'
    elif Content_Type_Header ==  	"application/x-sh":
        return '.sh'
    elif Content_Type_Header == 'application/x-tar':
        return '.tar'
    elif Content_Type_Header == 'audio/x-wav':
        return '.wav'
    elif Content_Type_Header =='audio/webm':
        return '.weba'
    elif Content_Type_Header == 'video/webm':
        return '.webm'
    elif Content_Type_Header == 'image/webp':
        return '.webp'
    else: return '.misc'
def __getheaders__(url):
     return get(url=url).headers
def __void__(a,e,i):
    if a: print(a)
    return 
def wget(options,callback=__void__):

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
    if not '.' in File:
        h = __getheaders__(options['url'])
        fh = h.get('Content-Type')
        hl = handle_by_header(fh)
        File = f'{File}{hl}'

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
    

