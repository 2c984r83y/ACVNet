from .kitti_dataset_1215 import KITTIDataset
from .sceneflow_dataset import SceneFlowDatset
from .dsec_png_dataset import DSEC_png_Dataset
__datasets__ = {
    "sceneflow": SceneFlowDatset,
    "kitti": KITTIDataset,
    "dsec_png": DSEC_png_Dataset
}
