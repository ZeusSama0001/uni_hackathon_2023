from django.http import JsonResponse
from django.http import HttpResponseServerError
from django.core.files.storage import FileSystemStorage
import json
from django.shortcuts import render

def upload_img(request):

    response = JsonResponse({'str_data':'hello world default'})

    if request.method == 'POST':

        img_file = request.FILES['scanner']
        fs = FileSystemStorage()
        filename = fs.save(img_file.name, img_file)
        uploaded_file_url = fs.url(filename)

        response = JsonResponse({'uploaded_file_url': uploaded_file_url})

    elif request.method == 'GET':
        pass

    return response

def show_result(request):

    if request.method == 'POST':

        file_name = 'scan_img.jpg'
        req_json = json.loads(request.body.decode("utf-8"))

        try:
            file_name = req_json['filename']
        except KeyError:
            HttpResponseServerError("Malformed data!")

        percent = iris_scan_orb_android(file_name)
        response = JsonResponse({'percent': percent})

    return response

def iris_scan_orb(request):

    from skimage import io
    from skimage.feature import (match_descriptors, ORB)
    from skimage.color import rgb2gray
    from .settings import MEDIA_ROOT

    img1 = rgb2gray(io.imread(MEDIA_ROOT + '/IRIS3.jpg'))  # Query
    img2 = rgb2gray(io.imread(MEDIA_ROOT + '/IRIS6.jpg'))  # Comparing to

    descriptor_extractor = ORB(n_keypoints=200)

    descriptor_extractor.detect_and_extract(img1)
    keypoints1 = descriptor_extractor.keypoints
    descriptors1 = descriptor_extractor.descriptors  # Query Descriptor

    descriptor_extractor.detect_and_extract(img2)
    keypoints2 = descriptor_extractor.keypoints
    descriptors2 = descriptor_extractor.descriptors  # Comparing To Descriptors

    matches12 = match_descriptors(descriptors1, descriptors2, cross_check=True)

    # print("Matched: ", len(matches12), " of ", len(descriptors1))
    percent = len(matches12) / len(descriptors1) * 100

    # print("Percent Match - ", percent, "%")

    """if percent > 80:
        print("Matched!")
    else:
        print("Not Matched!")"""

    return render(request, 'scan.html', {'percent': percent})

def iris_scan_orb_android(file_name):

    from skimage import io
    from skimage.feature import (match_descriptors, ORB)
    from skimage.color import rgb2gray
    from .settings import MEDIA_ROOT

    img1 = rgb2gray(io.imread(MEDIA_ROOT + '/'+ file_name))  # Query
    img2 = rgb2gray(io.imread(MEDIA_ROOT + '/IRIS9.jpg'))  # Comparing to

    descriptor_extractor = ORB(n_keypoints=200)

    descriptor_extractor.detect_and_extract(img1)
    keypoints1 = descriptor_extractor.keypoints
    descriptors1 = descriptor_extractor.descriptors  # Query Descriptor

    descriptor_extractor.detect_and_extract(img2)
    keypoints2 = descriptor_extractor.keypoints
    descriptors2 = descriptor_extractor.descriptors  # Comparing To Descriptors

    matches12 = match_descriptors(descriptors1, descriptors2, cross_check=True)

    percent = len(matches12) / len(descriptors1) * 100

    return percent