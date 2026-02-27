from .keibuan import KeibuanPersonality
from .psikolog import PsikologPersonality
from .teman import TemanPersonality

PERSONALITIES = {
    "ibu": KeibuanPersonality(),
    "psikolog": PsikologPersonality(),
    "teman": TemanPersonality(),
}