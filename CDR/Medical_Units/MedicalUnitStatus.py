import enum


class MedicalUnitStatus(enum.Enum):
    IDLE = 1
    ON_THE_WAY_TO_A_SITE_LOCATION = 2
    TREATING_A_CASUALTY = 3
    UPLOADING_A_CASUALTY = 4
    EVACUATING_A_CASUALTY_TO_HOSPITAL = 5
    HOSPITALIZATION_OF_PATIENTS = 6
