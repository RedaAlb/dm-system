from pydantic import BaseModel
from datetime import datetime


class Camera(BaseModel):
    camera_name: str
    camera_model: str

class Subject(BaseModel):
    subject_name: str

class TrialCamera(BaseModel):
    camera_id: str | None = None
    camera_position: tuple[float, float, float]
    sensor_type: str
    video_path: str

class CameraCalibration(BaseModel):
    calibration_data: dict
    cameras: list[TrialCamera]
    
class BodyPart(BaseModel):
    bodypart: str
    positon: tuple[float, float, float]
    rotation: tuple[float, float, float]

class Frame(BaseModel):
    frame_data: dict
    frame_number: int
    position: tuple[float, float, float]
    pose: list[BodyPart]

class TrialSubjects(BaseModel):
    subject_id: str | None = None
    motion_data: list[Frame]

class MotionCapture(BaseModel):
    motion_capture_data: dict
    subjects: list[TrialSubjects]

class Metric(BaseModel):
    metric_name: str
    metric_value: float

class TrialDetails(BaseModel):
    trial_date: datetime
    trial_name: str 
    trial_description: str
    trial_notes: str

class Trial(BaseModel):
    trial_details: TrialDetails
    camera_calibartion: CameraCalibration
    motion_capture: MotionCapture
    metrics: list[Metric]
    issue_ids: list[str]