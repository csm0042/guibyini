__author__ = 'chris.maue'

import logging


def callback(gui_object, instance, logfile):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                        filename=logfile, filemode='w')
    logging.info('[gui_callbacks] called with a value of %d' % instance)

    if instance == 1:
        #gui_object.clear_text(1)
        gui_object.write_text(1, '\nF1 Pressed')

    if instance == 2:
        #gui_object.clear_text(1)
        gui_object.write_text(1, '\nF2 Pressed')

    if instance == 3:
        #gui_object.clear_text(1)
        gui_object.write_text(1, '\nF3 Pressed')

    if instance == 4:
        #gui_object.clear_text(1)
        gui_object.write_text(1, '\nF4 Pressed')

    if instance == 5:
        #gui_object.clear_text(1)
        gui_object.write_text(1, '\nF5 Pressed')

    if instance == 6:
        #gui_object.clear_text(1)
        gui_object.write_text(1, '\nF6 Pressed')

    if instance == 7:
        #gui_object.clear_text(1)
        gui_object.write_text(1, '\nF7 Pressed')

    if instance == 8:
        #gui_object.clear_text(1)
        gui_object.write_text(1, '\nF8 Pressed')

    if instance == 9:
        #gui_object.clear_text(1)
        gui_object.write_text(1, '\nF9 Pressed')

    if instance == 10:
        #gui_object.clear_text(1)
        gui_object.write_text(1, '\nF10 Pressed')

    if instance == 11:
        #gui_object.clear_text(1)
        gui_object.write_text(1, '\nF11 Pressed')

    if instance == 12:
        gui_object.clear_text(1)
        gui_object.write_text(1, 'F12 Pressed')

    if instance == 13:
        gui_object.kill_root()


