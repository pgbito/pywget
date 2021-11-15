

import sys

from pywget import wget


def firstNonFlag(args):
  i =0
  for i in range(len(args)):
    if(args[i].charAt(0) != '-'):
      return args[i];
    i+=1
    
  
  return "";

argv = sys.argv
FileName = argv.pop(0)

def  help() :
    return '\n  '.join([
        '',
        'Usage: ' + FileName + ' [options] [url]...',
        '',
       
        '',
        'Options:',
        '',
        '  -h, --help           output usage information',
        '  -v, --version        output version number',
        '',
        'Usage:',
        '',
        '# Download file',
        '$ ' + FileName + ' https://github.com/NodeOS/NodeOS/archive/master.zip',
        ''
    ]) + '\n';



def callback():
  try:
    print('')
  except Exception as excp:
    print(excp)
 
if (
    argv.index('--help') != -1 or
    argv.index('-h') != -1
):
    print(help());
elif (argv.index('--version') != -1 or argv.index('-v') != -1):
    print(Version)
elif (len(argv)):
    destinationIndex = argv.index('--destination') + argv.index('-d') + 2;

    args = {};
    if(destinationIndex):
      args['dest'] = argv[destinationIndex];

      argv.insert(destinationIndex-1,2)
    
    args.url = firstNonFlag(argv);
    if(args.url.length > 0):
      print("Downloading...");
      wget(args, callback);
    else:
      print(help());
    
else:print(help());


