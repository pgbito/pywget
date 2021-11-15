import pywget as wget
monke_url = 'https://c.tenor.com/9rkrXs9nbNQAAAAC/monkey-monkeys.gif'
def on_download(error,response,body):
    if error:
        raise Exception(error)
        
    
    else:
        print('Monkey gif downloaded.')
        
wget.wget(
    options={
        "url":monke_url,
        'dest':'./monkey.gif'
        },callback=on_download)
