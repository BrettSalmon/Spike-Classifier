import requests
import sys
import tarfile
import tqdm
import os


if not os.path.isfile('images.tar.gz'):
    link = "https://relics.stsci.edu/Spike-Classifier/images/"
    filename = "images.tar.gz"
    with open(filename, "wb") as f:
        print("##### Downloading %s" % filename)
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')
        
        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()
    sys.stdout.write("\n")
if 0:
   print("##### Unpacking tarball")
   tar = tarfile.open(filename)
   tar.extractall()
   tar.close()

