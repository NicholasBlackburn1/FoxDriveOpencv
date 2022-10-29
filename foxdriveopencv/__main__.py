"""
main uwu
"""
from utils import logger
import cv2

def main():
    logger.info("starting Computer Rec....")

    logger.PipeLine_Data("opencv version "+cv2.__version__)

    logger.PipeLine_Data("opencv build info "+ cv2.getBuildInformation())






if __name__ == '__main__':
    main()