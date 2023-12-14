import enum

class Status(enum.Enum):
    IDLE = 1
    TREATING_A_CASUALTY = 2 #raanan & yuval
    UPLOADING_A_CASUALTY = 3 #raanan & yuval


    ON_THE_WAY_TO_A_SITE_LOCATION = 4  # shiri
    WORKING_IN_SITE = 5
    ON_THE_WAY_TO_HOSPITAL = 6
    RETURN_TO_DISPATCH = 7
    IN_DISPATCH = 8
    AT_HOSPITAL = 9 #shiri



