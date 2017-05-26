import json
import cv2
import logging

from .settings import HEALTH_BAR
from .state import State


class Frame(object):
    def __init__(self, matrix, borders=None):
        self.original_matrix = matrix
        if borders is None:
            self.borders = self.find_borders(matrix)
        self.frame = self.crop()

    def find_borders(self, matrix, color_thresh=0):
        # Frame is stretched so we either have black rows, black columns, or neither
        color_sum = matrix.sum(axis=2)
        m, n = matrix.shape

        if color_sum[0].sum() > color_thresh:
            # If first row is non-black, we have some black columns and no black rows
            rows_border = (0, m)
            j = 0
            for j in range(n):
                if color_sum[:, j].sum() > color_thresh:
                    break
            columns_border = (j, n-j)
        else:
            # Else, we have some black rows and no black columns
            columns_border = (0, n)
            i = 0
            for i in range(m):
                if color_sum[i, :].sum() > color_thresh:
                    break
            rows_border = (i, m-i)

        if rows_border[0] > m/2 or columns_border > n/2:
            logging.warning("Frame is black or malformed, assuming perfect fit")
            borders = None
        else:
            borders = (rows_border, columns_border)

        return borders

    def crop(self):
        if self.borders is None:
            return self.original_matrix

        row_borders, col_borders = self.borders
        return self.original_matrix[row_borders[0]:row_borders[1], col_borders[0]:col_borders[1], :]

    def crop_black(self, frame, color_thresh=0):
        col_over_thresh = [i for i, f in enumerate(frame.sum(axis=2).sum(axis=0)) if f > color_thresh]
        row_over_thresh = [i for i, f in enumerate(frame.sum(axis=2).sum(axis=1)) if f > color_thresh]

        return frame[row_over_thresh][:, col_over_thresh]


    def get_health(self):
        screen_height, screen_width = self.frame.shape[0:2]

        top = int(HEALTH_BAR["TOP"]*screen_height)
        bottom = int((HEALTH_BAR["TOP"] + HEALTH_BAR["HEIGHT"])*screen_height)
        height = bottom - top
        length = HEALTH_BAR["LENGTH"]*screen_width

        p1_left = int(HEALTH_BAR["P1_START"]*screen_width)
        p1_right = int((HEALTH_BAR["P1_START"] + HEALTH_BAR["LENGTH"])*screen_width)

        p2_left = int(HEALTH_BAR["P2_START"]*screen_width)
        p2_right = int((HEALTH_BAR["P2_START"] + HEALTH_BAR["LENGTH"])*screen_width)

        thresh = height*200

        p1_health = (self.frame[top:bottom, p1_left:p1_right, 1].sum(axis=0) >= thresh).sum() / length
        p2_health = (self.frame[top:bottom, p2_left:p2_right, 1].sum(axis=0) >= thresh).sum() / length

        return p1_health, p2_health


def preprocess(frame_matrix, borders, **kwargs):
    frame = Frame(frame_matrix, borders)
    health = frame.get_health()
    result = {
        "frame": frame,
        "own": {
            "health": health[0]
        },
        "enemy": {
            "health": health[1]
        }
    }
    return result

class Stream(object):
    def run(self, filename, callback, **kwargs):
        cap = cv2.VideoCapture(filename)
        i = 0
        borders = None
        while(cap.isOpened()):
            is_streaming, frame_matrix = cap.read()
            if not is_streaming:
                break

            # get the update to state singleton
            update_dict = preprocess(frame_matrix, borders)
            update_dict["frame_number"] = i

            # create or update the singleton
            State(update_dict)

            borders = update_dict["frame"].borders
            callback(**kwargs)
            i += 1

