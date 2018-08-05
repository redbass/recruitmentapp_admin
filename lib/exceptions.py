class BaseRecruitmentAppException(Exception):

    def __init__(self,
                 msg: str,
                 ref_id: str = None):
        super().__init__(msg)
        self.ref_id = ref_id


class AuthenticationError(BaseRecruitmentAppException):

    def __init__(self, msg: str = None, ref_id: str = None):
        super().__init__(msg or 'Authentication error', ref_id)
