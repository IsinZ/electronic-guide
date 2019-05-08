import cv2
from abc import ABC, abstractmethod

class BookRecognizer(ABC):
    @staticmethod
    def create(name, parameters):
        if name == "bfmatcher":
            return BFMatcherBookRecognizer(parameters)
        else:
            raise Exception()
        
    @abstractmethod
    def recognize(self, frame):
        """Recognize book"""
        

class BFMatcherBookRecognizer(BookRecognizer):
    
    def __init__(self, parameters):
        self.parameters = parameters
        
        detectors = {"ORB":1, "SIFT":2, "SURF":3}
        try:
            detectors[self.parameters['detector']]
        except(KeyError):
            print("Wrong detector name")
        else:
            if (self.parameters['detector'] == "ORB"):
                self.detector = cv2.ORB_create() 
            elif (self.parameters['detector'] == "SIFT"):
                self.detector = cv2.xfeatures2d.SIFT_create()
            elif (self.parameters['detector'] == "SURF"):
                self.detector = cv2.xfeatures2d.SURF_create()
                
        self.matcher = cv2.BFMatcher()
        self.descriptors = self.detect(self.parameters['books'])
        self.coeff = self.parameters['coefficient']
        self.kneighbours = self.parameters['kneighbours']
    
    def detect(self, books):
        descriptors = []
        for b in books:
            f = cv2.imread(b)
            gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
            _, desBook = self.detector.detectAndCompute(gray, None)
            descriptors.append(desBook)
        return descriptors
    
            
    def recognize(self, frame):
        arr = []
        ORB = cv2.ORB_create()
        frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, desFrame = ORB.detectAndCompute(frameGray, None)

        for t in self.descriptors:
            matches = self.matcher.knnMatch(t, desFrame, self.kneighbours)
            good = []
            for m,n in matches:
                if m.distance < n.distance * self.coeff: 
                    good.append(m)
                    
            arr.append(len(good))
        
        return arr
