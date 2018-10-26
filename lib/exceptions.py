class BaseRecruitmentAppException(Exception):

    def __init__(self,
                 msg: str,
                 ref_id: str = None):
        super().__init__(msg)
        self.ref_id = ref_id


class AuthenticationError(BaseRecruitmentAppException):

    def __init__(self, msg: str = None, ref_id: str = None):
        super().__init__(msg or 'Authentication error', ref_id)


class APICallError(BaseRecruitmentAppException):
    pass


class APIValidationError(BaseRecruitmentAppException):

    def __init__(self, core_response_body):
        super().__init__(msg=core_response_body.get('message'),
                         ref_id=core_response_body.get('ref_id'))
