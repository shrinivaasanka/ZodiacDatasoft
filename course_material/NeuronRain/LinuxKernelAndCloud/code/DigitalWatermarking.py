##############################################################################################################################################
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
##############################################################################################################################################
# Course Authored By:
# -----------------------------------------------------------------------------------------------------------
# K.Srinivasan
# NeuronRain Documentation and Licensing: http://neuronrain-documentation.readthedocs.io/en/latest/
# Personal website(research): https://sites.google.com/site/kuja27/
# -----------------------------------------------------------------------------------------------------------

import cv2
import numpy as np
import imquality.brisque as brisque
import PIL.Image

def image_quality_analysis(imagefile,model_path,range_path):
    img = cv2.imread(imagefile,cv2.IMREAD_COLOR)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.Laplacian(grey, cv2.CV_64F).var()
    #score = cv2.QualityBRISQUE_compute(img, model_path, range_path) 
    #obj = cv2.quality.QualityBRISQUE_create(model_path, range_path)
    #score = obj.compute(img)
    pilimg=PIL.Image.open(imagefile)
    score = brisque.score(pilimg)
    print(imagefile + " - brisque IQA score:",score)
    print(imagefile + " - blur:",blur)

def watermark_image(imagefile=None, watermark=None, fileIO=False, img=None, alpha=0.2):
    if imagefile is not None:
        img = cv2.imread(imagefile, -1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    namewatermark = cv2.imread(watermark, -1)
    namewatermark = cv2.cvtColor(namewatermark, cv2.COLOR_BGR2BGRA)
    imgheight, imgwidth, imgc = img.shape
    nwmheight, nwmwidth, nwmc = namewatermark.shape
    overlay = np.zeros((imgheight, imgwidth, 4), dtype='uint8')
    for p in range(0, nwmheight):
        for q in range(0, nwmwidth):
            if namewatermark[p, q][3] != 0:
                heightoffset = imgheight - nwmheight - 100
                widthoffset = imgwidth - nwmwidth - 100
                # print(heightoffset+p,",",widthoffset+q)
                overlay[heightoffset + p, widthoffset +
                        q] = namewatermark[p, q]
    print("overlay shape:",overlay.shape)
    print("image shape:",img.shape)
    cv2.addWeighted(overlay, alpha, img, 1-alpha, 0, img)
    #img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    if fileIO:
        cv2.imwrite(imagefile+"_Watermarked.jpg", img)
        return img 
    else:
        return img 


def watermark_video(videofile, watermark, maxframes):
    namewatermark = cv2.imread(watermark, -1)
    namewatermark = cv2.cvtColor(namewatermark, cv2.COLOR_BGR2BGRA)
    vid = cv2.VideoCapture(videofile)
    cnt = 1
    while True and cnt <= maxframes:
        ret, frame = vid.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        frameheight, framewidth, framec = frame.shape
        nwmheight, nwmwidth, nwmc = namewatermark.shape
        overlay = np.zeros((frameheight, framewidth, 4), dtype='uint8')
        for p in range(0, nwmheight):
            for q in range(0, nwmwidth):
                if namewatermark[p, q][3] != 0:
                    heightoffset = frameheight - nwmheight - 100
                    widthoffset = framewidth - nwmwidth - 100
                    # print(heightoffset+p,",",widthoffset+q)
                    overlay[heightoffset + p, widthoffset +
                            q] = namewatermark[p, q]
        cv2.addWeighted(overlay, 0.05, frame, 0.95, 0, frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        cv2.imwrite(videofile+"_Frame%d.jpg" % (cnt), frame)
        cnt += 1


if __name__ == "__main__":
    # watermark_video("testlogs/Krishna_iResearch_NeuronRain_Repositories-2020-07-10_13.17.20.mp4","testlogs/DigitalWatermarking_Name.jpg",2)
    # watermark_image("testlogs/DWMExample1.jpg","testlogs/DigitalWatermarking_PSGTech.jpg")
    # watermark_image("testlogs/DWMExample2.jpg","testlogs/DigitalWatermarking_PSGTech.jpg")
    # watermark_image("testlogs/DWMExample1.jpg","testlogs/DigitalWatermarking_PSGTech.png")
    # watermark_image("testlogs/DWMExample2.jpg","testlogs/DigitalWatermarking_PSGTech.png")
    image_quality_analysis("testlogs/29Oct2023_LunarEclipse_Bandung_Wikipedia.jpg","testlogs/brisque_model_live.yml","testlogs/brisque_range_live.yml")
    image_quality_analysis("testlogs/29Oct2023_LunarEclipse_Kumbakonam_Wikipedia.jpg","testlogs/brisque_model_live.yml","testlogs/brisque_range_live.yml")
    overlayimg = watermark_image(
        imagefile="testlogs/CMA_CUMTA_Overlay_Maps/metro_network.jpg", watermark="testlogs/CMA_CUMTA_Overlay_Maps/mtc_network.jpg")
    overlayimg = watermark_image(
        watermark="testlogs/CMA_CUMTA_Overlay_Maps/rail_network.jpg", fileIO=False, img=overlayimg)
    overlayimg = watermark_image(
        watermark="testlogs/CMA_CUMTA_Overlay_Maps/road_network.jpg", fileIO=False, img=overlayimg)
    cv2.imwrite("testlogs/CMA_CUMTA_Overlay_Maps/metro_network_Watermarked.jpg", overlayimg)
