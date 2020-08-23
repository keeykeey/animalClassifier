from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os,time,sys

#info about API_key
KEY = os.environ['ANIMALCLASSIFIER_KEY']
SECRET_KEY = os.environ['ANIMALCLASSIFIER_SECRET_KEY']
WAITTIME = 1

searchText = sys.argv[1]

flickr = FlickrAPI(KEY,SECRET_KEY,format = 'parsed-json')
result = flickr.photos.search(
    text = searchText,
    per_page = 10,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']

#send to google cloud storae
tmpDir = './tempDir_sendToGCS'
if not os.path.exists(tmpDir):
    os.mkdir(tmpDir)

cloudStorageBucketName = 'real_or_picture'
for i,photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filePathForSending = tmpDir +'/' +  photo['id'] + '.jpg'
    urlretrieve(url_q,filePathForSending) 
    
    os.system("gsutil cp {} gs://{}".format(filePathForSending,cloudStorageBucketName))
    time.sleep(WAITTIME) 
