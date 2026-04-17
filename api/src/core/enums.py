from enum import Enum

class RobotType(str, Enum):
    THOR_SINGLE_ARM = "thor_single_arm"
    THOR_DUAL_ARM = "thor_dual_arm"
    FRANKA_SINGLE_ARM = "franka_single_arm"
    FRANKA_DUAL_ARM = "franka_dual_arm"
