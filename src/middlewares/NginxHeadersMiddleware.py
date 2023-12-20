from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response

from src.models.dto import NginxHeadersModel


class NginxHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        headers = NginxHeadersModel(
            host=request.headers.get("host"),
            x_forwarded_for=request.headers.get("x-forwarded-for"),
            x_real_ip=request.headers.get("x-forwarded-for").split(",")[0],
            x_forwarded_proto=request.headers.get("x-forwarded-proto"),
            user_agent=request.headers.get("user-agent"),
        )

        request.state.headers = headers

        return await call_next(request)
