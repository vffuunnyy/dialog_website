from fastapi import Request

from src.models.dto import NginxHeadersModel


def get_nginx_headers(request: Request) -> NginxHeadersModel:
    return request.state.headers
