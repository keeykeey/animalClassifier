from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os,time,sys

#info about API_key
KEY = os.environ['ANIMALCLASSIFIER_KEY']
SECRET_KEY = os.environ['ANIMALCLASSIFIER_SECRET_KEY']
WAITTIME = 1

#save directories
animalName = sys.argv[1]
saveDir = "./" + animalName

flickr = FlickrAPI(KEY,SECRET_KEY,format = 'parsed-json')
result = flickr.photos.search(
    text = animalName,
    per_page = 10,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']

#save in local environment
'''
for i,photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = saveDir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath):continue
    urlretrieve(url_q,filepath)
    time.sleep(WAITTIME)
'''

#send to google cloud storae
tempDir = './tempDir_sendToGCS'
if not os.path.exists(tmpDir):
    os.mkfir('tmpDir)

cloudStorageBucketName = 'real_or_picture'
for i,photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filePathToSend = tmpDir +'/' +  photo['id'] + '.jpg'
    urlretrieve(url_q,filepath) 
    
    filePathAtGCS = cloudStorageBuckerName = '/' + photo['id'] + '.jpg'
    os.system("gsutil cp {} gs://{}".format(filePathToSend,filePathAtGCS))
    time.sleep(WAITTIME) 
