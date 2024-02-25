import enum

class Status(enum.Enum):
    IDLE = 1
    TREATING_A_CASUALTY = 2 #raanan & yuval
    UPLOADING_A_CASUALTY = 3 #raanan & yuval


    ON_THE_WAY_TO_A_SITE_LOCATION = 4  # shiri
    WORKING_ON_SITE = 5 #shiri
    ON_THE_WAY_TO_HOSPITAL = 6 #shiri
    RETURN_TO_DISPATCH = 7 #shiri
    AT_DISPATCH = 8 #shiri
    AT_HOSPITAL = 9 #shiri



