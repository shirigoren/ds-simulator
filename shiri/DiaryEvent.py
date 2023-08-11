import enum


class DiaryEventType(enum.Enum):
    NEW_DISASTER_SITE = 1
    ARRIVAL_TO_DISASTER_SITE = 2
    WORK_COMPLETED_AT_DISASTER_SITE = 3
    DRIVING_TO_NEW_DISASTER_SITE = 4  # ambulance capacity is not full
    DRIVING_TO_THE_MEDICAL_CENTER = 5  # there are no casualties in the car
    DRIVING_TO_HOSPITAL_WITH_CASUALTIES = 6  # there are casualties in the ambulance
    FINISH_WORK_AT_HOSPITAL = 7
    SIMULATION_END = 8


######################################################################################

class DiaryEvent(object):

    def __init__(self, time_now, event_type):
        self.time_now = time_now
        self.type = event_type


#######################################################################################

class NewDisasterSite(DiaryEvent):  # type 1

    def __init__(self, time_now, disaster_site):
        self.disaster_site = disaster_site
        DiaryEvent.__init__(self, time_now=time_now, event_type=DiaryEventType.NEW_DISASTER_SITE)


#######################################################################################

class ArrivalToDisasterSite(DiaryEvent):  # type 2

    def __init__(self, arrival_time, medical_unit, disaster_site):
        self.medical_unit = medical_unit
        self.disaster_site = disaster_site
        DiaryEvent.__init__(self, time_now=arrival_time, event_type=DiaryEventType.ARRIVAL_TO_DISASTER_SITE)


########################################################################################

class WorkCompletedAtDisasterSite(DiaryEvent):  # type 3

    def __init__(self, time_now, medical_unit, disaster_site):
        self.medical_unit = medical_unit
        self.time_now = time_now
        DiaryEvent.__init__(self, time_now=time_now, event_type=DiaryEventType.WORK_COMPLETED_AT_DISASTER_SITE)


########################################################################################

class DrivingToNewDisasterSite(DiaryEvent):  # type 4

    def __init__(self, time_now, medical_unit, new_disaster_site):
        self.medical_unit = medical_unit
        self.new_disaster_site = new_disaster_site
        DiaryEvent.__init__(self, time_now=time_now, event_type=DiaryEventType.DRIVING_TO_NEW_DISASTER_SITE)


########################################################################################

class DrivingToTheMedicalCenter(DiaryEvent):  # type 5

    def __init__(self, time_now, medical_unit):
        self.medical_unit = medical_unit
        DiaryEvent.__init__(self, time_now=time_now, event_type=DiaryEventType.DRIVING_TO_THE_MEDICAL_CENTER)


########################################################################################

class DRIVING_TO_HOSPITAL_WITH_CASUALTIES(DiaryEvent):  # type 6

    def __init__(self, time_now, medical_unit, hospital, casualties):
        self.medical_unit = medical_unit
        self.hospital = hospital
        self.casualties = casualties
        DiaryEvent.__init__(self, time_now=time_now, event_type=DiaryEventType.DRIVING_TO_HOSPITAL_WITH_CASUALTIES)


########################################################################################

class FINISH_WORK_AT_HOSPITAL(DiaryEvent):  # type 7

    def __init__(self, time_now, medical_unit, hospital):
        self.medical_unit = medical_unit
        self.hospital = hospital
        DiaryEvent.__init__(self, time_now=time_now, event_type=DiaryEventType.FINISH_WORK_AT_HOSPITAL)


########################################################################################
class SimulationEnd(DiaryEvent):  # type 8

    def __init__(self, time_now):
        DiaryEvent.__init__(self, time_now=time_now, event_type=DiaryEventType.SIMULATION_END)
