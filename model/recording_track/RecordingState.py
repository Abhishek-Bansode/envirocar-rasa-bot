import enum


class RecordingState(enum.Enum):
    RECORDING_INIT = "RECORDING_INIT"
    RECORDING_RUNNING = "RECORDING_RUNNING"
    RECORDING_STOPPED = "RECORDING_STOPPED"
