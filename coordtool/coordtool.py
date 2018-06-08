'''
Calculates heading and distance between two lat-lon coordinates
'''
#Import numpy for mathematical functions
import numpy as np

class coordtool():
    def __init__(self, home):
        '''Init function
        :param home: Reference home point, list of latitude and longitude
        '''
        self.home = home
    def distance(self, point):
        '''Calculate distance between home and given point
        :param point: Point of interest, list of latitude and longitude
        '''
        loc0 = self.home
        loc1 = point

        #Convert lat-lon to radians
        loc0 = np.deg2rad(loc0)
        loc1 = np.deg2rad(loc1)

        #Calculate delta
        dlat = loc1[0]-loc0[0]
        dlon = loc1[1]-loc0[1]

        #Haversine formula
        a = (np.sin(dlat/2)**2)+np.cos(loc0[0])*np.cos(loc1[0])*(np.sin(dlon/2)**2)
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
        d = 6371*c

        #Heading calculation
        theta = np.arctan2(np.sin(dlon)*np.cos(loc1[0]) , np.cos(loc0[0])*np.sin(loc1[0])-np.sin(loc0[0])*np.cos(loc1[0])*np.cos(dlon))

        return [d, theta]
