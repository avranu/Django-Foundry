"""
	
	Metadata:
	
		File: response.py
		Project: Django Foundry
		Created Date: 04 May 2023
		Author: Jess Mann
		Email: jess.a.mann@gmail.com
	
		-----
	
		Last Modified: Thu May 04 2023
		Modified By: Jess Mann
	
		-----
	
		Copyright (c) 2023 Jess Mann
"""
from rest_framework import response

#
# Generic Responses
#
class Response(response.Response):
	def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type=None):
		super().__init__(data, status, template_name, headers, exception, content_type)

class SuccessResponse(Response):
	def __init__(self, data=None, status=200, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'message': 'Success'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class ErrorResponse(Response):
	def __init__(self, data=None, status=500, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'An Error Occurred'}
		super().__init__(data, status, template_name, headers, exception, content_type)

#
# HTTP CODE 2xx
#
class OkResponse(SuccessResponse):
	def __init__(self, data=None, status=200, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'message': 'OK'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class DataResponse(OkResponse):
	def __init__(self, data=dict, status=200, template_name=None, headers=None, exception=False, content_type=None):
		super().__init__(data, status, template_name, headers, exception, content_type)

class PaginatedResponse(DataResponse):
	def __init__(self, data=dict, status=200, template_name=None, headers=None, exception=False, content_type=None):
		data = {
			'count': 0,
			'next': None,
			'previous': None,
			'results': [],
			**data,
		}
		super().__init__(data, status, template_name, headers, exception, content_type)

class DataModifiedResponse(OkResponse):
	def __init__(self, data=None, status=201, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'message': 'Data Modified'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class CreatedResponse(DataModifiedResponse):
	def __init__(self, data=None, status=201, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'message': 'Created'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class DeletedResponse(DataModifiedResponse):
	def __init__(self, data=None, status=204, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'message': 'Deleted'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class UpdatedResponse(DataModifiedResponse):
	def __init__(self, data=None, status=204, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'message': 'Updated'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class AcceptedResponse(OkResponse):
	def __init__(self, data=None, status=202, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'message': 'Accepted'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class NonAuthoritativeInformationResponse(OkResponse):
	def __init__(self, data=None, status=203, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'message': 'Non-Authoritative Information'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class NoContentResponse(OkResponse):
	def __init__(self, data=None, status=204, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'message': 'No Content'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class ResetContentResponse(OkResponse):
	def __init__(self, data=None, status=205, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'message': 'Reset Content'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class PartialContentResponse(OkResponse):
	def __init__(self, data=None, status=206, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'message': 'Partial Content'}
		super().__init__(data, status, template_name, headers, exception, content_type)

#
# ERROR CODES 5xx
#
class InternalErrorResponse(ErrorResponse):
	def __init__(self, data=None, status=500, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Internal Server Error'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class NotImplementedResponse(InternalErrorResponse):
	def __init__(self, data=None, status=501, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Not Implemented'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class BadGatewayResponse(InternalErrorResponse):
	def __init__(self, data=None, status=502, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Bad Gateway'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class ServiceUnavailableResponse(InternalErrorResponse):
	def __init__(self, data=None, status=503, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Service Unavailable'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class GatewayTimeoutResponse(InternalErrorResponse):
	def __init__(self, data=None, status=504, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Gateway Timeout'}
		super().__init__(data, status, template_name, headers, exception, content_type)

#
# ERROR CODES 4xx
#
class BadRequestResponse(ErrorResponse):
	def __init__(self, data=None, status=400, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Bad Request'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class UnauthorizedResponse(BadRequestResponse):
	def __init__(self, data=None, status=401, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Unauthorized'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class NotFoundResponse(BadRequestResponse):
	def __init__(self, data=None, status=404, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': '404: Not Found'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class ForbiddenResponse(BadRequestResponse):
	def __init__(self, data=None, status=403, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Forbidden'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class NotAllowedResponse(BadRequestResponse):
	def __init__(self, data=None, status=405, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Method Not Allowed'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class ConflictResponse(BadRequestResponse):
	def __init__(self, data=None, status=409, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Conflict'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class GoneResponse(BadRequestResponse):
	def __init__(self, data=None, status=410, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Gone'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class LengthRequiredResponse(BadRequestResponse):
	def __init__(self, data=None, status=411, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Length Required'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class PreconditionFailedResponse(BadRequestResponse):
	def __init__(self, data=None, status=412, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Precondition Failed'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class RequestEntityTooLargeResponse(BadRequestResponse):
	def __init__(self, data=None, status=413, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Request Entity Too Large'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class RequestURITooLongResponse(BadRequestResponse):
	def __init__(self, data=None, status=414, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Request URI Too Long'}
		super().__init__(data, status, template_name, headers, exception, content_type)

#
# ERROR CODES 3xx
#
class MultipleChoicesResponse(ErrorResponse):
	def __init__(self, data=None, status=300, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Multiple Choices'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class MovedPermanentlyResponse(MultipleChoicesResponse):
	def __init__(self, data=None, status=301, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Moved Permanently'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class FoundResponse(MultipleChoicesResponse):
	def __init__(self, data=None, status=302, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Found'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class SeeOtherResponse(MultipleChoicesResponse):
	def __init__(self, data=None, status=303, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'See Other'}
		super().__init__(data, status, template_name, headers, exception, content_type)

#
# ERROR CODES 1xx
#
class ContinueResponse(ErrorResponse):
	def __init__(self, data=None, status=100, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Continue'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class SwitchingProtocolsResponse(ContinueResponse):
	def __init__(self, data=None, status=101, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Switching Protocols'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class ProcessingResponse(ContinueResponse):
	def __init__(self, data=None, status=102, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Processing'}
		super().__init__(data, status, template_name, headers, exception, content_type)

class EarlyHintsResponse(ContinueResponse):
	def __init__(self, data=None, status=103, template_name=None, headers=None, exception=False, content_type=None):
		if not data:
			data = {'error': 'Early Hints'}
		super().__init__(data, status, template_name, headers, exception, content_type)

