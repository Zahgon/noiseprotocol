from typing import List

from noise.constants import TOKEN_PSK


class Pattern(object):
    """
    TODO document
    """
    def __init__(self):
        # As per specification, if both parties have pre-messages, the initiator is listed first. To reduce complexity,
        # pre_messages shall be a list of two lists:
        # the first for the initiator's pre-messages, the second for the responder
        self.pre_messages = [
            [],
            []
        ]

        # List of lists of valid tokens, alternating between tokens for initiator and responder
        self.tokens = []

        self.name = ''
        self.one_way = False
        self.psk_count = 0

    def has_pre_messages(self):
        pass

    def get_initiator_pre_messages(self) -> list:
        return self.pre_messages[0].copy()

    def get_responder_pre_messages(self) -> list:
        return self.pre_messages[1].copy()

    def apply_pattern_modifiers(self, modifiers: List[str]) -> None:
        # Applies given pattern modifiers to self.tokens of the Pattern instance.
        pass

    def get_required_keypairs(self, initiator: bool) -> list:
        required = []
        if initiator:
            if self.name[0] in ('K', 'X', 'I'):
                required.append('s')
            if self.one_way or self.name[1] == 'K':
                required.append('rs')
        else:
            if self.name[0] == 'K':
                required.append('rs')
            if self.one_way or self.name[1] in ['K', 'X']:
                required.append('s')
        return required


class OneWayPattern(Pattern):
    def __init__(self):
        super(OneWayPattern, self).__init__()
        self.one_way = True
