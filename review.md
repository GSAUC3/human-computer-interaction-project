## How mediapipe hand detection mechanism works?

Mediapipe uses a single-shot palm deteciton model and once that is done it performs precise key point localization of 21 3D palm coordinates in the detected hand region.

The mediapipe pipeline utilizes multiple models like, a palm detection model that returns an oriented hand bounding box from the full image. the cropped image region is fed to a hand landmark model defined by the palm detector and returns high-fidelity 3D hand key points. 