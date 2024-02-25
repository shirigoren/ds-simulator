import enum


class DiaryEventType(enum.Enum):
    NEW_DISASTER_SITE = 1
    ARRIVAL_TO_DISASTER_SITE = 2
    FINISH_AT_DS = 3
    ARRIVAL_TO_DISPATCH = 4
    ARRIVAL_TO_HOSPITAL = 5
    FINISH_AT_HOSPITAL = 6
    SIMULATION_END = 7

######################################################################################

class DiaryEvent(object):

    def __init__(self, time_now, event_type):
        self.time_now = time_now
        self.event_type = event_type


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

class FinishWorkDisasterSite(DiaryEvent):  # type 3

    def __init__(self, time_now, medical_unit, disaster_site):
        self.medical_unit = medical_unit
        self.disaster_site = disaster_site
        # TODO: calculate actual time to treat. Disaster site simulation (Raanan&Yuval).
        self.time_now = time_now + 2
        DiaryEvent.__init__(self, time_now=time_now, event_type=DiaryEventType.FINISH_AT_DS)

#######################################################################################

# class ArrivalToDispatch(DiaryEvent):  # type 4
#
#     def __init__(self, time_now, medical_unit):
#         self.medical_unit = medical_unit
#         DiaryEvent.__init__(self, time_now=time_now, event_type=DiaryEventType.ARRIVAL_TO_DISPATCH)
#

########################################################################################

class ArrivalToHospital(DiaryEvent):  # type 5

    def __init__(self, time_now, medical_unit, hospital, casualties):
        self.medical_unit = medical_unit
        self.hospital = hospital
        self.casualties = casualties
        DiaryEvent.__init__(self, time_now=time_now, event_type=DiaryEventType.ARRIVAL_TO_HOSPITAL)


########################################################################################

class FinishWorkAtHospital(DiaryEvent):  # type 6

    def __init__(self, time_now, medical_unit, hospital):
        self.medical_unit = medical_unit
        self.hospital = hospital
        DiaryEvent.__init__(self, time_now=time_now, event_type=DiaryEventType.FINISH_AT_HOSPITAL)


########################################################################################
class SimulationEnd(DiaryEvent):  # type 7

    def __init__(self, time_now):
        DiaryEvent.__init__(self, time_now=time_now, event_type=DiaryEventType.SIMULATION_END)
