from enum import StrEnum


class ProjectStatus(StrEnum):
    ACTIVE = 'ACTIVE'  # Actively developed
    INACTIVE = 'INACTIVE'  # Not active but still maintained
    ARCHIVED = 'ARCHIVED'  # Frozen intentionally
    UNMAINTAINED = 'UNMAINTAINED'  # Abandoned / no support expected
