"""
this class is for handling downloading all the files
"""
from pathlib import Path
from utils import logger,Consts
import wget






# this makes the local file paths for storing the data
def makePaths():


    if Path(str(Path().absolute()) + Consts.basepath).exists:
        # base bath
        logger.info("creating file structure for prgram...")

        Path(str(Path().absolute()) + Consts.basepath).mkdir(
            parents=True, exist_ok=True
        )

        # avi paths
        Path(str(Path().absolute()) + Consts.capturedimages).mkdir(
            parents=True, exist_ok=True
        )
        Path(str(Path().absolute()) + Consts.capturedvideos).mkdir(
            parents=True, exist_ok=True
        )
        Path(str(Path().absolute()) + Consts.models).mkdir(
            parents=True, exist_ok=True
        )

        logger.PipeLine_Ok("created paths successfully")

    else:
        logger.warning("the paths exist cannot create them uwu~")



# gets model for yolo
def getyolofiles():

    logger.warning("downloading yolo stuff.....")
    wget.download("https://pjreddie.com/media/files/yolov3.weights",str(Path().absolute()) + Consts.models+"yolo.weights")
    logger.info("downloaded file to "+str(Path().absolute()) + Consts.models+"yolo.weights")